# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
import numpy as np
import cv2

# imports - module imports
from spockpy.io    import Capture
from spockpy._util import _resize_image
from spockpy.event import keycode

def _get_roi(size, ratio = 0.25, position = 'tr'):
	width, height = np.asarray(size) * ratio

	if   position == 'tl':
		x, y = 0, 0
	elif position == 'tr':
		x, y = size[0] - width, size[1]
	elif position == 'bl':
		x, y = 0, size[1] - height
	elif position == 'br':
		x, y = size[0] - width, size[1] - height

	return (x, y, width, height)

class HoverPad(object):
	'''
	HoverPad object

	Parameters

	:param size: the size of the HoverPad instance containing the width and height in pixels, defaults to 320x240
	:type size: :obj:`tuple`

	:param deviceID: the device ID of your capture device, defaults to 0.
	:type deviceID: :obj:`int`

	Example

	>>> import spockpy
	>>> pad = spockpy.HoverPad(size = (480, 320))
	'''
	TITLE = 'spockpy.HoverPad'

	def __init__(self, size = (320, 240), deviceID = 0, position = 'tr'):
		self.size     = size
		self.capture  = Capture()
		self.position = position

		self.roi      = _get_roi(self.size, position)

	def _mount_roi(self, image, color = (74, 20, 140), thickness = 1):
		x, y, w, h    = self.roi

		cv2.rectangle(image, (x, y), (w, h), thickness)

	'''
	Displays the HoverPad object instance onto the screen. To close the HoverPad, simply press the ESC key
	
	Example

	>>> import spockpy
	>>> pad = spockpy.HoverPad()
	>>> pad.show()
	'''
	def show(self):
		while cv2.waitKey(10) not in [keycode.ESCAPE, keycode.Q, keycode.q]:
			image = self.capture.read()
			image = cv2.flip(image, 1)

			image = self._mount_roi(image)

			image = _resize_image(image, self.size, maintain_aspect_ratio = True)
			array = np.asarray(image)

			cv2.imshow(HoverPad.TITLE, array)

		cv2.destroyWindow(HoverPad.TITLE)