import os
import json
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get Together API key from environment variable
TOGETHER_API_KEY = "Enter_your_Together_API_key_here"  # os.getenv('TOGETHER_API_KEY')
if not TOGETHER_API_KEY:
    print("WARNING: TOGETHER_API_KEY environment variable not set")

@app.route('/', methods=['GET', 'POST'])
def index():
    questions = []
    error = None
    
    if request.method == 'POST':
        topic = request.form.get('topic', '')
        role = request.form.get('role', '')
        
        if not topic or not role:
            error = "Please provide both topic and role"
        else:
            try:
                questions = generate_interview_questions(topic, role)
            except Exception as e:
                error = f"Error generating questions: {str(e)}"
    
    return render_template('index.html', questions=questions, error=error)

def generate_interview_questions(topic, role):
    """Generate interview questions using Together API based on topic and role"""
    if not TOGETHER_API_KEY:
        raise ValueError("Together API key is not set. Please set the TOGETHER_API_KEY environment variable.")
    
    # API endpoint for Together AI
    url = "https://api.together.xyz/v1/completions"
    
    # Headers
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Create prompt
    prompt = f"""Generate 10 technical interview questions for a {role} position focusing on {topic}.
    
    The questions should be challenging but relevant to the role and topic.
    Format the response as a JSON array of objects with the following structure:
    [
        {{
            "question": "The question text",
            "answer": "A brief answer or key points to look for",
            "difficulty": "Easy/Medium/Hard"
        }},
        ...
    ]
    
    Make the questions specific to {topic} and appropriate for {role} level expertise.
    """
    
    # Request payload
    payload = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "prompt": prompt,
        "max_tokens": 2048,
        "temperature": 0.7,
        "top_p": 0.9
    }
    
    # Make the API request
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"API call failed with status {response.status_code}: {response.text}")
    
    response_data = response.json()
    
    # Extract the generated text
    generated_text = response_data.get('choices', [{}])[0].get('text', '')
    
    # Find JSON array in the response
    try:
        # Look for JSON array in the text
        start_idx = generated_text.find('[')
        end_idx = generated_text.rfind(']') + 1
        
        if start_idx == -1 or end_idx == 0:
            raise ValueError("JSON array not found in response")
            
        json_text = generated_text[start_idx:end_idx]
        questions = json.loads(json_text)
        
        # Ensure we have at most 10 questions
        return questions[:10]
    except json.JSONDecodeError:
        raise Exception("Failed to parse generated questions as JSON")

if __name__ == '__main__':
    app.run(debug=True)