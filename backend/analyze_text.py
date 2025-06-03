import spacy

# Load the biomedical NER model
nlp = spacy.load("en_ner_bc5cdr_md")
def extract_medical_entities(text):
    doc = nlp(text)
    for ent in doc.ents:
        print(f"Entity: {ent.text}, Label: {ent.label_}")
if __name__ == "__main__":
    sample_text = "Aspirin is used to treat pain, and it can prevent heart attacks. It may cause bleeding disorders."
    extract_medical_entities(sample_text)
