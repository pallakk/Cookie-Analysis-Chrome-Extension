import re
import spacy

# Load spaCy biomedical model
nlp = spacy.load("en_ner_bc5cdr_md")

# Custom medical dictionary
medical_terms = {"diabetes", "insulin", "cancer", "asthma", "remedy"}
risky_phrases = [
    ("cure", "herbal"),
    ("treat", "without"),
    ("no side effects",),
    ("miracle", "cure"),
    ("guaranteed", "results")
]
credible_sources = ["pubmed", "cdc", "who", "mayo clinic", ".gov", ".edu"]

# Tokenizer
def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

# Rule-based medical term match
def find_medical_terms(tokens):
    return list({token for token in tokens if token in medical_terms})

# Rule-based risky claim detection
def detect_risky_patterns(text):
    lower = text.lower()
    return [" ".join(pattern) for pattern in risky_phrases if all(word in lower for word in pattern)]

# Check if any trusted source is cited
def check_credible_sources(text):
    lower = text.lower()
    return [source for source in credible_sources if source in lower]

# Calculate a credibility score (0–100)
def compute_score(medical_terms, risky_phrases, credible_refs):
    score = 100
    score -= len(risky_phrases) * 20
    score -= len(medical_terms) * 5
    score += len(credible_refs) * 15
    return max(0, min(score, 100))

def analyze_text(text):
    tokens = tokenize(text)
    matched_terms = find_medical_terms(tokens)
    flagged_phrases = detect_risky_patterns(text)
    cited_sources = check_credible_sources(text)

    # spaCy NER
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

    credibility = compute_score(matched_terms, flagged_phrases, cited_sources)

    return {
        "custom_medical_terms": matched_terms,
        "risky_language_detected": flagged_phrases,
        "credible_sources_found": cited_sources,
        "spacy_entities": entities,
        "credibility_score": credibility
    }
