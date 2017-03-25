# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
import numpy as np
import cv2

# imports - module imports
from spockpy.io    import Capture
from spockpy._util import _resize_image
from spockpy.event import keycode

class HoverPad(object):
	'''
	HoverPad object

	:param size: the size of the HoverPad instance containing the width and height in pixels, defaults to 320x240
	:type size: :obj:`tuple`

	:param deviceID: the device ID of your capture device, defaults to 0.
	:type deviceID: :obj:`int`
	'''
	TITLE = 'spockpy.HoverPad'

	def __init__(self, size = (320, 240), deviceID = 0):
		self.size    = size
		self.capture = cv2.VideoCapture(device = deviceID)

	'''
	Displays the HoverPad object instance onto the screen. To close the HoverPad, simply press the ESC key
	'''
	def show(self):
		while cv2.waitKey(0) not in [keycode.ESCAPE, keycode.Q, keycode.q]:
			array = self.capture.read()
			# image = _resize_image(image, self.size, maintain_aspect_ratio = True)
			# array = np.asarray(image)

			cv2.imshow(HoverPad.TITLE, array)

		cv2.destroyWindow(HoverPad.TITLE)