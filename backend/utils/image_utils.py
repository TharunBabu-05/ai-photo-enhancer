import os
import cv2
import numpy as np
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

def upscale_image(img_path):
    """Upscales an image using Real-ESRGAN."""
    # Determine the model name and path
    model_name = 'RealESRGAN_x4plus'
    
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to the backend directory
    backend_dir = os.path.dirname(current_dir)
    # Construct the model path
    model_path = os.path.join(backend_dir, 'models', 'realesrgan', 'weights', f'{model_name}.pth')
    
    # Check if model exists, if not, download it
    if not os.path.exists(model_path):
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        print(f"Model not found at {model_path}, downloading...")
        from realesrgan.utils import download_pretrained_models
        download_pretrained_models(model_name)
        # The downloaded model might be in a different location, try to find it
        if not os.path.exists(model_path):
            # Try to find the model in the default location
            home_dir = os.path.expanduser('~')
            alt_model_path = os.path.join(home_dir, '.cache', 'torch', 'hub', 'checkpoints', f'{model_name}.pth')
            if os.path.exists(alt_model_path):
                model_path = alt_model_path

    # Use RRDBNet for this model
    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)

    # Initialize the RealESRGANer
    upsampler = RealESRGANer(
        scale=4,
        model_path=model_path,
        model=model,
        tile=0,
        tile_pad=10,
        pre_pad=0,
        half=False  # Use full precision for CPU
    )

    # Read the image
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

    # Enhance the image
    try:
        output, _ = upsampler.enhance(img, outscale=4)
        return output
    except RuntimeError as error:
        print('Error', error)
        print('If you encounter CUDA out of memory, try to set --tile with a smaller number.')
        return None
