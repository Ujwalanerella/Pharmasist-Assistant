# Pharmacist's Assistant

## Overview
The project is an AI-powered pharmacist assistant that extracts text from handwritten prescriptions and provides a REST API for processing prescriptions using Optical Character Recognition (OCR).

## Features
- Uses Tesseract OCR to read handwritten text from prescription images.
- Flask-based API for uploading and processing prescriptions.
- Returns extracted text as a JSON response.

## Requirements
- Python 3.x
- OpenCV
- Flask
- pytesseract

## Installation
### Clone the repository:
```sh
git clone <repository_link>
cd pharmacist-assistant
```

### Create a virtual environment (optional but recommended):
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies:
```sh
pip install -r requirements.txt
```

### Make sure you have installed and configured Tesseract:
1. Download and install from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
2. Add Tesseract to your system path.

## Running the Application
```sh
python app.py
```

## API Usage
- **Endpoint:** `/process_prescription`
- **Method:** `POST`
- **Request:** Upload an image.
- **Response:** JSON object containing the extracted text.

### Example Request:
```sh
curl -X POST -F "image=@prescription.jpg" http://127.0.0.1:5000/process_prescription
```

## Repository Contents
- **app.py** → The script that processes prescriptions.
- **README.md** → Instructions about setup, usage, and future improvements.
