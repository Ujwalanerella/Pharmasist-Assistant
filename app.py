from flask import Flask, request, jsonify
import pytesseract
import cv2
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    text = pytesseract.image_to_string(image)
    return text

def extract_medication_details(text):
    doc = nlp(text)
    drugs = [ent.text for ent in doc.ents if ent.label_ in ["DRUG", "QUANTITY"]]
    return drugs

@app.route("/process-prescription", methods=["POST"])
def process_prescription():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]
    image_path = "temp_prescription.jpg"
    image.save(image_path)

    extracted_text = extract_text_from_image(image_path)
    medications = extract_medication_details(extracted_text)

    return jsonify({"extracted_text": extracted_text, "medications": medications})

if __name__ == "__main__":
    app.run(debug=True)
