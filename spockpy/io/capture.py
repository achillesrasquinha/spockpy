# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
import cv2

# imports - module imports
from spockpy.config import BaseConfig

class Capture(object):
	def __init__(self, device = BaseConfig.DEFAULT_CAPTURE_DEVICE_ID, *args, **kwargs):
		self.super    = super(Capture, self)
		self.deviceID = device

		self.capture  = cv2.VideoCapture(self.deviceID)

	def read(self):
		_, frame = self.capture.read()

		return frame
