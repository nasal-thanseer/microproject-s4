from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)

# Questions and corresponding answers
questions = [
    {
        'question': 'What is your preferred programming language?',
        'answer': None
    },
    {
        'question': 'What is your preferred field of study?',
        'answer': None
    },
    {
        'question': 'What is your preferred level of difficulty?',
        'answer': None
    }
]

# Function to scrape course data from a website
def scrape_courses(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    courses = {}
    course_descriptions = {}

    # Extract course titles and descriptions
    course_elements = soup.select('.course-card')
    for element in course_elements:
        course_id = element['data-id']
        course_title = element.select_one('.course-title').text.strip()
        course_description = element.select_one('.course-description').text.strip()

        courses[course_id] = course_title
        course_descriptions[course_id] = course_description

    return courses, course_descriptions

# Course recommendation function
def recommend_courses(preferences, courses, course_descriptions):
    # Create TF-IDF vectorizer
    tfidf = TfidfVectorizer()

    # Fit and transform the course descriptions
    course_vectors = tfidf.fit_transform(course_descriptions.values())

    # Transform user preferences
    user_vector = tfidf.transform([preferences])

    # Compute cosine similarity
    cosine_similarities = linear_kernel(user_vector, course_vectors).flatten()

    # Sort courses based on similarity scores
    related_courses_indices = cosine_similarities.argsort()[::-1]

    # Get top 3 related courses
    recommended_courses = [list(courses.keys())[i] for i in related_courses_indices[:3]]
    reasons = [course_descriptions[course] for course in recommended_courses]

    return recommended_courses, reasons

# API endpoint for course recommendation
@app.route('/recommend', methods=['POST'])
def course_recommendation():
    # Get user answer from the request
    answer = request.json['answer']

    # Update the current question with the user's answer
    current_question = questions[len(questions) - 1]
    current_question['answer'] = answer

    # Check if all questions have been answered
    if all(question['answer'] is not None for question in questions):
        # Generate final recommendations
        answers = [question['answer'] for question in questions]

        # Scrape course data from a website
        course_url = 'https://www.example.com/courses'  # Replace with the actual URL of the course listing page
        courses, course_descriptions = scrape_courses(course_url)

        # Get course recommendations and reasons
        user_preferences = ' '.join(answers)
        recommendations, reasons = recommend_courses(user_preferences, courses, course_descriptions)

        # Prepare the response
        response = {
            'recommendations': recommendations,
            'reasons': reasons
        }

        # Reset the questions
        for question in questions:
            question['answer'] = None

    else:
        # Find the next unanswered question
        next_question = next(question for question in questions if question['answer'] is None)
        response = {'question': next_question['question']}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
