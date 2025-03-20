from flask import Flask, jsonify, request, render_template
import text_processor as tp
import traceback
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Initialize flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['GET', 'POST'])
def process_text():
    if request.method == 'GET':
        return jsonify({"message": "Use POST with JSON data"}), 200
    
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({"error": "No text provided"}), 400
        
        text = data['text']

        # Call the text processing function from text_processor.py
        result = tp.process_text(text)

        response = app.response_class(
            response=json.dumps(result, ensure_ascii=False, indent=4),
            status=200,
            mimetype="application/json"
        )
        return response
    
    except Exception as e:
        print("ERROR in Flask route:")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
    
@app.route('/lookup_hsk', methods=['GET'])
def lookup_hsk():
    word = request.args.get('word', '')
    if not word:
        return jsonify({"error": "No word provided"}), 400
    
    word_data = tp.hsk_dict.get(word, {})
    if not word_data:
        return jsonify({"message": f"'{word}' not found in HSK"}), 404
    
    return jsonify(word_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)