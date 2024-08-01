from flask import Flask, jsonify, request, render_template, send_file
from PIL import Image
import torch
import io
import cv2
import numpy as np

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

app = Flask(__name__)

model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)

def draw_boxes(results, img):
    # Convert PIL image to OpenCV format
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    for result in results.xyxy[0].tolist():
        xmin, ymin, xmax, ymax, confidence, cls = result
        label = f"{model.names[int(cls)]} {confidence:.2f}"
        cv2.rectangle(img_cv, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 3)
        cv2.putText(img_cv, label, (int(xmin), int(ymin) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Convert back to PIL Image
    img_pil = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
    return img_pil

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']
    img_bytes = file.read()
    img = Image.open(io.BytesIO(img_bytes))

    # Perform inference
    results = model(img)
    
    # Draw bounding boxes and labels on the image
    img_with_boxes = draw_boxes(results, img)

    # Save the image with bounding boxes to a BytesIO object
    img_io = io.BytesIO()
    img_with_boxes.save(img_io, 'JPEG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)