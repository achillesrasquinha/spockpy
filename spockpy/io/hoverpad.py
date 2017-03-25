# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
import threading

# imports - third-party imports
import numpy as np
import cv2
from PIL import Image

# imports - module imports
from spockpy.io    import Capture
from spockpy._util import _resize_image
from spockpy.event import keycode

def _round_int(value):
	result = int(np.rint(value))

	return result

def _get_roi(size, ratio = 0.42, position = 'tr'):
	width, height = _round_int(size[0] * ratio), _round_int(size[1] * ratio)

	if   position == 'tl':
		x, y = 0, 0
	elif position == 'tr':
		x, y = size[0] - width, 0
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

	:param 

	Example

	>>> import spockpy
	>>> pad = spockpy.HoverPad(size = (480, 320))
	'''
	TITLE = 'spockpy.HoverPad'

	def __init__(self, size = (320, 240), deviceID = 0, position = 'tr'):
		self.size     = size
		self.capture  = Capture()
		self.position = position

		self.roi      = _get_roi(size = self.size, position = position)

		self.thread   = threading.Thread(target = self._showloop)

	def _mount_roi(self, array, color = (74, 20, 140), thickness = 2):
		x, y, w, h    = self.roi

		cv2.rectangle(array, (x, y), (x + w, y + h), color, thickness)

		return array

	'''
	Displays the HoverPad object instance onto the screen. To close the HoverPad, simply press the ESC key
	
	Example

	>>> import spockpy
	>>> pad = spockpy.HoverPad()
	>>> pad.show()
	'''
	def show(self):
		self.thead.start()
		
	def _showloop(self):
		while cv2.waitKey(10) not in [keycode.ESCAPE, keycode.Q, keycode.q]:
			image = self.capture.read()
			image = image.transpose(Image.FLIP_LEFT_RIGHT)

			image = _resize_image(image, self.size, maintain_aspect_ratio = True)
			
			array = np.asarray(image)
			array = self._mount_roi(array)

			cv2.imshow(HoverPad.TITLE, array)

		cv2.destroyWindow(HoverPad.TITLE)