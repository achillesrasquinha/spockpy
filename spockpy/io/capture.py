# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
import cv2

# imports - module imports
from spockpy.config import BaseConfig

class Capture(cv2.VideoCapture):
	def __init__(self, device = spockpy.BaseConfig.DEFAULT_CAPTURE_DEVICE_ID, *args, **kwargs):
		self.super    = super(Capture, self)
		self.deviceID = device

		self.super.__init__(device = device, *args, **kwargs)

	def read(self):
		_, frame = self.super.read()

		return frame
