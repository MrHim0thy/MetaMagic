from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Dummy prediction function
def predict_meta(deck_data):
    archetypes = [
        "Jeskai Control", "Golgari Midrange", "Mono-Red Aggro", 
        "Dimir Rogues", "Selesnya Enchantments"
    ]
    weights = [random.uniform(0.1, 0.4) for _ in archetypes]
    total = sum(weights)
    probs = [round(w / total, 2) for w in weights]
    prediction = list(zip(archetypes, probs))
    return sorted(prediction, key=lambda x: x[1], reverse=True)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    content = file.read().decode('utf-8')  # placeholder for processing

    prediction = predict_meta(content)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
