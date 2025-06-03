from flask import Flask, request, jsonify
import spacy

# Load the scispaCy biomedical model
nlp = spacy.load("models/en_ner_bc5cdr_md")

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze_text():
    data = request.get_json()
    text = data.get("text", "")
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return jsonify(entities)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
