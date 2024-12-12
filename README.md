# Course Recommendation Model

This repository contains the source code for a **Course Recommendation System**. The project includes a backend implementation for course recommendations and a front-end interface for user interaction. The system guides users in choosing courses based on their preferences and inputs.

## Features

- **Interactive Chat Interface:** A user-friendly web interface for interacting with the recommendation system.
- **Dynamic Recommendations:** Personalized course suggestions with reasons, powered by the backend.
- **Easy Deployment:** Designed to be deployed locally or on a web server with minimal setup.

## Project Structure

- **`backend.py`:** Handles the server-side logic, including:
  - Processing user inputs.
  - Generating course recommendations.
  - Managing the flow of questions and responses.

- **`index-2.html`:** Implements the front-end interface for the chat-based interaction, featuring:
  - Real-time communication with the backend.
  - User-friendly chat layout and design.
  - Dynamic message handling for recommendations and feedback.

## Getting Started

### Prerequisites

- **Python 3.8+**
- **Flask** (or any other Python-based web framework)
- Basic knowledge of HTML, CSS, and JavaScript.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nasal-thanseer/course-recommendation-model.git
   cd course-recommendation-model
   ```

2. **Set up the backend:**
   - Install Python dependencies:
     ```bash
     pip install flask
     ```
   - Run the server:
     ```bash
     python backend.py
     ```

3. **Set up the front-end:**
   - Open `index-2.html` in any browser or serve it using a simple HTTP server:
     ```bash
     python -m http.server 8080
     ```

4. **Access the system:**
   - Navigate to `http://localhost:8080` in your browser.

## Usage

1. Open the front-end page (`index-2.html`) in your browser.
2. Start interacting with the chat interface.
3. Follow the questions and get personalized course recommendations.

## File Details

### Backend
- **`backend.py`**
  - Listens for user inputs and processes responses.
  - Generates course recommendations dynamically.
  - Endpoints:
    - `/recommend` - Processes user inputs and returns recommendations.
    - `/questions` - Fetches the next question.

### Frontend
- **`index-2.html`**
  - Styled for a split-screen layout with an interactive chat box.
  - Uses JavaScript to handle user inputs and backend responses dynamically.

## Future Enhancements

- Add a database for storing user preferences and course data.
- Integrate AI/ML models for more accurate recommendations.
- Deploy on a cloud platform like AWS or Heroku.

## Contributing

We welcome contributions! Please fork the repository, make changes, and submit a pull request.

