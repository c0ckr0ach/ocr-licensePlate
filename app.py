from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello, Flask!"

@app.route('/run_python_script', methods=['POST'])
def run_script():
    try:
        # Run the py_test.py script using subprocess
        subprocess.run(['python', 'py_test'], check=True)
        result = "Python script executed successfully"
        return jsonify({"message": result})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

