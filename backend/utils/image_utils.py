import cv2
import numpy as np
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

def upscale_image(img_path):
    """Upscales an image using Real-ESRGAN."""
    # Determine the model name and path
    model_name = 'RealESRGAN_x4plus'
    model_path = f'models/realesrgan/weights/{model_name}.pth'

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
