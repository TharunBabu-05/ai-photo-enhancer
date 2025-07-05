import os
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import cv2
from werkzeug.utils import secure_filename

from utils.image_utils import upscale_image 

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
ENHANCED_FOLDER = 'enhanced'

# Create directories if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENHANCED_FOLDER, exist_ok=True)

@app.route('/enhance', methods=['POST'])
def enhance_image_route():
    if 'photo' not in request.files:
        return 'No file part', 400
    file = request.files['photo']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = secure_filename(file.filename)
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(input_path)

        # Enhance the image using Real-ESRGAN
        enhanced_image = upscale_image(input_path)

        if enhanced_image is not None:
            output_filename = f'enhanced_{filename}'
            output_path = os.path.join(ENHANCED_FOLDER, output_filename)
            cv2.imwrite(output_path, enhanced_image)
            return send_file(output_path, mimetype='image/jpeg')
        else:
            return 'Failed to enhance image', 500

@app.route('/')
def home():
    return jsonify({"status": "ok", "message": "AI Photo Enhancer backend is running!"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)