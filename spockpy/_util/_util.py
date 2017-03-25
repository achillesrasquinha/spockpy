# imports - third-party imports
import numpy as np
from PIL import Image
import cv2

def _resize_image(image, size, maintain_aspect_ratio = False):
    copy = image.copy()

    copy.thumbnail(size, Image.ANTIALIAS)

    return copy

def _round_int(value):
    result = int(np.rint(value))

    return result

def _to_grayscale(array):
    gray = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)

    return gray

def _get_opencv_version():
    version = cv2.__version__
    version = version.split('.')

    major, minor, patch = int(version[0]), int(version[1]), int(version[2])

    return (major, minor, patch)

def _mount_roi(array, roi, color = (0, 255, 0), thickness = 1):
    x, y, w, h = roi

    cv2.rectangle(array, (x, y), (x + w, y + h), color = color, thickness = thickness)

    return array