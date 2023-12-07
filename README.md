
# Camera Barcode Scanner

This Python script provides a simple yet effective way to detect and decode barcodes in real-time using your device's camera. It uses OpenCV for video capturing and processing, and Pyzbar for barcode detection and decoding.

## Features
- **Real-Time Detection**: Scans and decodes barcodes in real-time using a webcam or camera.
- **Cooldown Mechanism**: Prevents the same barcode from being scanned repeatedly within a short period (set to 3 seconds by default).

## Installation

To run this script, you need to install Python on your machine along with OpenCV and Pyzbar libraries. You can install these libraries using pip:

```bash
pip install opencv-python-headless
pip install pyzbar
```

## Usage

1. Run the script in your Python environment.
2. Point your camera at a barcode to scan it.
3. The script will detect the barcode, decode it, and print the information to the console.
4. To exit, press 'q' while the camera window is active.

## Code Explanation

- `cv2.VideoCapture(0)`: Initializes the camera. '0' refers to the default camera.
- `while cap.isOpened()`: Continuously captures frames from the camera as long as it is open.
- `pyzbar.decode(frame)`: Decodes any barcodes found in the current frame.
- Cooldown Logic: The script keeps track of the last scanned barcode and the time it was scanned. If the same barcode is scanned again within 3 seconds, it will be ignored.
- Display: The script draws a rectangle around detected barcodes and displays the decoded text on the screen.
- Exit: Press 'q' to quit the program.

## Note
Ensure your camera is functioning properly before running the script. The script does not record video, it only processes frames in real-time for barcode detection.

## BaseCode
https://aratech.es/programacion/reconocimiento-de-codigos-de-barras-en-tiempo-real-con-python-y-opencv
