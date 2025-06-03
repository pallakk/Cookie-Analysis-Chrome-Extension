from flask import Flask, request, jsonify
import re

app = Flask(__name__)

HEALTH_TERMS = [
    r'\bdiabetes\b', r'\bcancer\b', r'\bheart\b',
    r'\bblood pressure\b', r'\bpregnant\b', r'\bssn\b',
    r'\ballergy\b', r'\btumor\b', r'\bcholesterol\b',
    r'\bepilepsy\b', r'\bmental health\b', r'\bdepression\b'
]

def extract_sensitive(text):
    found_terms = []
    for term in HEALTH_TERMS:
        if re.search(term, text, re.IGNORECASE):
            found_terms.append(term)
    return found_terms

@app.route("/scan", methods=["POST"])
def scan():
    data = request.json
    text = data.get("text", "")
    matches = extract_sensitive(text)
    credibility_score = max(0, 100 - len(matches) * 10)
    return jsonify({
        "matches": matches,
        "credibility_score": credibility_score
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
