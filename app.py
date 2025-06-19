from flask import Flask, request, jsonify, render_template
from utils import generate_motivation_letter

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        data = request.json  # expect JSON input
        letter = generate_motivation_letter(data)
        return jsonify({"letter": letter})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
