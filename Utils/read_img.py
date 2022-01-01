from PIL import Image
from io import BytesIO
import numpy as np

def read_image(img_encoded) :
    image = Image.open(BytesIO(img_encoded))
    return np.array(image) 