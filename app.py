import os
import json
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

# Load env variables
load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)

app = Flask(__name__)

def get_gemini_response(prompt, is_json=False):
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        text = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(text) if is_json else text
    except Exception as e:
        return {"error": str(e)} if is_json else f"Error: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/timeline', methods=['POST'])
def generate_timeline():
    data = request.json
    scenario = data.get('scenario', 'I want to vote for the first time.')
    
    prompt = f"""
    You are an expert on the democratic election process. The user is in the following scenario: "{scenario}".
    Generate a 4-step chronological timeline of what they need to do from today until election day.
    Return ONLY a valid JSON array of objects. Format:
    [
      {{"step": 1, "title": "Step Name", "description": "Short explanation."}},
      ...
    ]
    """
    timeline_data = get_gemini_response(prompt, is_json=True)
    return jsonify(timeline_data)

@app.route('/api/sandbox', methods=['POST'])
def democracy_sandbox():
    data = request.json
    question = data.get('question', '')
    
    prompt = f"""
    Explain this election-related term or question simply to a new voter: "{question}".
    Return EXACTLY 3 short, easy-to-understand bullet points. No introductory text.
    """
    answer = get_gemini_response(prompt, is_json=False)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)