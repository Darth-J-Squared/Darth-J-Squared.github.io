from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS
CORS(app)

def calculate_score(client_id):
    
    score = hash(client_id) % 100 / 1000  # Dummy score between 0 and 1
    return score

@app.route('/calculate_score', methods=['POST'])
def calculate_score_route():
    try:
        # Read JSON data from request
        data = request.json
        print("data", data)
        client_id = data.get('ID')

        if client_id is not None:
            # Calculate score
            score = calculate_score(client_id)

            # Return score as JSON
            return jsonify({"score": score})
        else:
            return jsonify({"error": "Client ID not provided"}), 400
    except Exception as e:
        # Return error as JSON
        return jsonify({"error": str(e)}), 500
    

if __name__ == "__main__":
    app.run(debug=True)
