# Automatic Number Plate Recognition (ANPR) System

## Introduction
Vehicle monitoring and security management are essential for industries, corporate campuses, and public facilities. Traditional systems, such as manual verification or RFID tags, are often slow, error-prone, and expensive to maintain.  

During my internship at **Indian Oil Corporation Ltd (IOCL)**, I developed an **Automatic Number Plate Recognition (ANPR) System** that leverages **deep learning, computer vision, and Optical Character Recognition (OCR)** to detect and read license plates in real time.  

The solution replaced manual workflows with an automated system capable of handling real-world variations in fonts, lighting, and plate sizes.

---

## System Design and Workflow

The ANPR pipeline combines **modern deep learning models** with **classical image-processing techniques** for maximum efficiency:

1. **License Plate Detection with YOLOv8**  
   - Uses **YOLOv8** (You Only Look Once, Version 8) for real-time license plate detection from CCTV or IP camera feeds.  
   - Outputs bounding boxes around detected plates, which are cropped for further processing.  

2. **Image Preprocessing with OpenCV**  
   - **Grayscale Conversion**: Reduces RGB to a single intensity value, simplifying computation.  
   - **Sharpening**: Enhances character edges for clearer recognition.  
   - **Adaptive Thresholding**: Makes characters stand out under variable lighting conditions.  

3. **Character Segmentation**  
   - Segments the preprocessed plate into individual characters using contour detection and bounding boxes.  
   - Each character is isolated for independent recognition, improving accuracy.  

4. **Text Recognition with EasyOCR**  
   - Segmented characters are passed through **EasyOCR**, a PyTorch-based deep learning OCR engine.  
   - CNN layers extract visual features, RNN layers handle sequential dependencies, and a CTC decoder converts predictions into readable text.  
   - Characters are combined into the full license plate string.  

5. **Post-processing and Validation with Regex**  
   - Validates outputs against the standard Indian license plate format (e.g., `XX00XX0000`).  
   - Helps correct OCR misreads like O ↔ 0 or I ↔ 1.  

6. **Data Logging with SQL**  
   - Recognized plate numbers, timestamps, and metadata are stored in a relational database.  
   - Enables anomaly detection, historical queries, and integration with monitoring systems.  

---

## Technologies Used

- **YOLOv8** – Real-time object detection for license plates.  
- **OpenCV** – Image preprocessing and character segmentation.  
- **EasyOCR** – Deep learning–based OCR engine built on PyTorch.  
- **Python** – Integrates detection, preprocessing, OCR, and database modules.  
- **SQL** – Stores recognized plates with metadata.  
- **Regex** – Ensures plate numbers match valid formats.  

---

## Detailed Working of Core Components

### YOLOv8 (Detection)
- Processes the entire image in a single forward pass of the neural network.  
- Anchor-free detection heads allow real-time performance with high accuracy.  
- Detects multiple vehicles and license plates simultaneously.  

### OpenCV (Preprocessing & Segmentation)
- **Grayscale**: Simplifies RGB to intensity values for faster processing.  
- **Sharpening**: Highlights edges and character boundaries.  
- **Adaptive Thresholding**: Handles uneven lighting conditions.  
- **Contour Detection**: Isolates each character for recognition.  

### EasyOCR (Recognition)
- CNN layers extract features from each character.  
- RNN layers (LSTM) handle sequential dependencies in characters.  
- CTC decoder converts predictions into readable text strings.  

### SQL Database (Storage)
- Stores structured records: `plate_number`, `timestamp`, `vehicle_id`, etc.  
- Allows queries such as *all entries for today* or *duplicate detection*.  

### Regex (Validation)
- Validates recognized text against patterns like `[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}`.  
- Ensures only valid license plate numbers are logged.  

---

## Results and Impact

- **~90% recognition accuracy** in controlled conditions.  
- **~3 seconds per plate** average processing time.  
- At IOCL, replaced slow RFID/manual verification workflows.  
- Improved **security monitoring**, reliability, and operational efficiency.  
- Laid the foundation for **anomaly detection** in vehicle entry systems.  

---

## Future Improvements

- End-to-end **deep segmentation models** for more accurate recognition.  
- Cloud deployment for **scalability** and API integration.  
- Integration with **national traffic databases** for toll collection, law enforcement, and smart city applications.  

---

## Installation

### Prerequisites
- Python 3.8+  
- `pip` or `pip3`  
- (Optional) GPU with CUDA for real-time performance  

### Clone & Setup
```bash
git clone https://github.com/c0ckr0ach/ocr-licensePlate.git
cd ocr-licensePlate
