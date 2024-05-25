from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_text():
    data = request.json
    text = data.get('text', '')

    # Example processing: convert text to uppercase
    processed_text = text.upper()

    return jsonify({'processed_text': processed_text})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
