**Real-Time License Plate Detection and Recognition**
**Overview**
This project implements a real-time license plate detection and recognition system using machine learning. The system uses YOLO (You Only Look Once) with a custom license plate dataset for object detection. Once the license plate is detected, OpenCV extracts each individual letter from the plate. These separate images are then sent to the EasyOCR module, which reads the characters and outputs the recognized license plate in the terminal. Additionally, a frontend UI is implemented using Flask to allow users to upload images or videos for license plate detection and recognition.

**Features**
Real-Time License Plate Detection: Utilizes YOLO for fast and accurate license plate detection.
Character Extraction: Employs OpenCV to segment and extract individual characters from the detected license plate.
OCR for Character Recognition: Uses EasyOCR to read and recognize the extracted characters.
Local Deployment: Runs the application locally using Flask.

**Installation**
Prerequisites
Python 3.7 
pip (Python package installer)

**Dependencies**
flask
opencv-python
easyocr
yolov5

**Setting Up YOLO**
Clone the YOLO repository:
git clone https://github.com/ultralytics/yolov5.git
cd yolov5

**Running the Application**
Start the Flask server:
python app.py
Open your web browser and navigate to http://127.0.0.1:5000 to access the frontend UI.

**Acknowledgements**
YOLOv5 by Ultralytics
EasyOCR
OpenCV
