# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
import cv2
from PIL import Image

class Capture(object):
	def __init__(self, device = 0):
		self.deviceID = device
		self.capture  = cv2.VideoCapture(self.deviceID)

	def read(self):
		_, frame = self.capture.read()
		image    = Image.fromarray(frame)

		return image