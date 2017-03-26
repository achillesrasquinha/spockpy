# imports - compatibility packages
from __future__ import absolute_import

# imports - standard packages
import numpy as np

# imports - airdraw
from airdraw import AppConfig

def _get_version_string():
    version = '.'.join(map(str, AppConfig.VERSION))

    return version

def _to_grayscale(r, g, b):
    gray = 0.2126 * r + 0.715 * g + 0.0722 * b

    return gray

def _image_to_input(image):
    image = image.convert('RGB')
    arr   = np.array(image)
    r,g,b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    bw    = _to_grayscale(r, g, b)

    bw[bw <  128] = 0
    bw[bw >= 128] = 1

    bw    = bw.flatten()

    return bw
