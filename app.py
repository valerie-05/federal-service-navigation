from flask import Flask, render_template, request, jsonify, session
from supabase import create_client, Client
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')

supabase_url = os.getenv('VITE_SUPABASE_URL')
supabase_key = os.getenv('VITE_SUPABASE_ANON_KEY')
supabase: Client = create_client(supabase_url, supabase_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/api/chat', methods=['POST'])
def chat_message():
    data = request.json
    message = data.get('message', '')

    try:
        response = requests.post(
            f"{supabase_url}/functions/v1/chat",
            headers={
                'Authorization': f'Bearer {supabase_key}',
                'Content-Type': 'application/json'
            },
            json={'message': message}
        )
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tts', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data.get('text', '')

    try:
        response = requests.post(
            f"{supabase_url}/functions/v1/text-to-speech",
            headers={
                'Authorization': f'Bearer {supabase_key}',
                'Content-Type': 'application/json'
            },
            json={'text': text}
        )
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/resources', methods=['GET'])
def get_resources():
    try:
        response = supabase.table('resources').select('*').execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/conversations', methods=['GET'])
def get_conversations():
    try:
        response = supabase.table('conversations').select('*').order('created_at', desc=True).execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
