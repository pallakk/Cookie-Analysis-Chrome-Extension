from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

HEALTH_KEYWORDS = ["age", "weight", "diagnosis", "medication", "treatment", "symptom", "illness"]

@app.route('/analyze', methods=['POST'])
def analyze():
    cookies = request.json.get("cookies", [])
    combined_text = " ".join(cookies).lower()
    doc = nlp(combined_text)
    
    flagged = [kw for kw in HEALTH_KEYWORDS if kw in combined_text]
    return jsonify({"sensitive": bool(flagged), "terms": flagged})
