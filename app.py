from flask import Flask, render_template, request, jsonify, send_file
import anthropic
import os
from dotenv import load_dotenv
from io import BytesIO

# Load environment variables from .env file
load_dotenv()
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY:
    raise ValueError("Claude API key not found! Please set ANTHROPIC_API_KEY in your .env file.")

app = Flask(__name__, template_folder='my_templates')
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_story():
    data = request.get_json()
    prompt = data.get('prompt', '').strip()
    genre = data.get('genre', 'Any')
    length = int(data.get('length', 200))  # Default to 200 words

    if not prompt:
        return jsonify({"error": "Prompt cannot be empty."}), 400

    genre_text = f" Genre: {genre}." if genre and genre != "Any" else ""
    # Set max_tokens generously (roughly 1.5 tokens per word for English)
    max_tokens = int(length * 1.5)

    system_prompt = (
        f"You are a creative story writer. Generate a compelling story of about {length} words based on the user's prompt."
        f"{genre_text} Please be as close as possible to the requested word count. Respond only with the story text."
    )

    print("Prompt:", prompt)
    print("Genre:", genre)
    print("Word count:", length)
    print("System prompt:", system_prompt)
    print("Max tokens:", max_tokens)

    try:
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=max_tokens,
            temperature=0.9,
            system=system_prompt,
            messages=[
                {"role": "user", "content": [{"type": "text", "text": prompt}]}
            ]
        )
        story = response.content[0].text
        return jsonify({"story": story})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/export', methods=['POST'])
def export_story():
    data = request.get_json()
    story = data.get('story', '')
    if not story:
        return jsonify({"error": "No story to export."}), 400
    buffer = BytesIO()
    buffer.write(story.encode('utf-8'))
    buffer.seek(0)
    return send_file(
        buffer,
        as_attachment=True,
        download_name='story.txt',
        mimetype='text/plain'
    )

if __name__ == '__main__':
    print("🚀 Starting Flask app... Visit http://127.0.0.1:5000/ in your browser.")
    app.run(debug=True)
