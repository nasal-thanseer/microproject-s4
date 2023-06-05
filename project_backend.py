import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

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

# Scrape course data from a website
course_url = 'https://www.example.com/courses'  # Replace with the actual URL of the course listing page
courses, course_descriptions = scrape_courses(course_url)

# User preferences
user_preferences = 'I want to learn machine learning and data analysis.'

# Get course recommendations and reasons
recommendations, reasons = recommend_courses(user_preferences, courses, course_descriptions)

# Print recommended courses with reasons
print('Recommended courses:')
for i, course in enumerate(recommendations):
    print(f'{i+1}. {courses[course]}')
    print(f'Reason: {reasons[i]}')
    print()
