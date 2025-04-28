# Interview Question Generator

A modern Flask web application that generates tailored interview questions based on topic and role using the Together AI API.

![Last Updated](https://img.shields.io/badge/Last%20Updated-April%202025-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)
![Flask](https://img.shields.io/badge/Flask-2.3.3-lightblue)

## Overview

This application allows users to generate relevant and challenging interview questions tailored to specific roles and technical topics. It leverages the Together AI API with the Mixtral-8x7B-Instruct model to create contextually appropriate questions and answers, making it ideal for interview preparation or assessment creation.

## Features

- 🎯 Generate 10 targeted interview questions based on role and topic
- 🧠 AI-powered question generation using Together's Mixtral model
- 🔄 Automatic categorization by difficulty level (Easy/Medium/Hard)
- 💡 Includes suggested answers for each question
- 🎨 Modern, responsive UI with glass morphism design
- ✨ Interactive elements with smooth animations
- 📱 Mobile-friendly interface

## Installation

### Prerequisites

- Python 3.10+
- Flask
- python-dotenv
- requests

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd protostudio
   ```

2. Install the required packages:
   ```bash
   pip install flask python-dotenv requests
   ```

3. Create a `.env` file in the project root and add your Together API key:
   ```
   TOGETHER_API_KEY=your_together_api_key_here
   ```

## Usage

1. Start the Flask development server:
   ```bash
   flask run
   ```

2. Access the application in your web browser at:
   ```
   http://127.0.0.1:5000
   ```

3. Enter your desired topic (e.g., "Python", "React", "Machine Learning") and role (e.g., "Junior Developer", "Senior Engineer") to generate tailored interview questions.

## Project Structure

```
protostudio/
├── app.py                 # Main Flask application file
├── Software Questions.csv # Database of sample questions
├── static/
│   ├── script.js          # Frontend JavaScript
│   └── styles.css         # CSS styling
├── templates/
│   └── index.html         # HTML template
└── .env                   # Environment variables (not tracked in git)
```

## API Integration

This project uses the Together AI API to generate interview questions. The API call is configured to use the Mixtral-8x7B-Instruct model with carefully tuned parameters for optimal question generation.

### Together AI API Parameters:

- **Model**: mistralai/Mixtral-8x7B-Instruct-v0.1
- **Temperature**: 0.7 (balances creativity and coherence)
- **Top-p**: 0.9 (maintains diverse outputs while filtering unlikely tokens)
- **Max Tokens**: 2048 (provides sufficient space for 10 detailed questions)
