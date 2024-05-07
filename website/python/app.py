from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS
CORS(app)

def calculate_score(client_id):
    
    score = hash(client_id) % 100 / 1000  # Dummy score between 0 and 1
    return score
    


if __name__ == "__main__":
    app.run(debug=True)
