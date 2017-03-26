# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
import cv2
from PIL import Image

class Capture(object):
	'''
	Capture object

	:param deviceID: device ID of your capture device, defaults to 0
	:type deviceID: :obj:`int`

	Example

	>>> import spockpy
	>>> cap = spockpy.Capture()
	'''
	def __init__(self, deviceID = 0):
		self.deviceID = deviceID
		self.capture  = cv2.VideoCapture(self.deviceID)
	
	def read(self):
		'''
		Reads the current input stream from a capture device and returns a `PIL.Image` object

		>>> import spockpy
		>>> cap   = spockpy.Capture()
		>>> image = cap.read()
		>>> image.show()
		'''
		_, frame = self.capture.read()
		image    = Image.fromarray(frame)

		return image