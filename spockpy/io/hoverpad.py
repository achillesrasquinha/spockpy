# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk
import threading

# imports - third-party imports
from PIL import Image, ImageTk

# imports - module imports
from spockpy._util import _resize_image
from spockpy.config import BaseConfig
from spockpy.io import Capture

class HoverPad(object):
	TITLE = 'HoverPad'

	class Frame(tk.Frame):
		def __init__(self, master = None, size = BaseConfig.HOVERPAD_SIZE):
			self.master  = master
			self.size    = size

			tk.Frame.__init__(self, self.master)

			self.createUI()

		def createUI(self):
			currentRow    = 0

			width, height = self.size
			self.video    = tk.Label(self.master,
								     width  = width,
								     height = height)
			self.video.grid(row = currentRow, column = 0, sticky = tk.E + tk.W + tk.N + tk.S)

	def __init__(self,
				 size = BaseConfig.HOVERPAD_SIZE):
		self.size     = size

		self.root     = tk.Tk()
		self.root.title(HoverPad.TITLE)

		width, height = self.size
		self.root.geometry('{width}x{height}'.format(
			width  = width,
			height = height
		))

		self.frame    = HoverPad.Frame(master = self.root)

		self.thread   = threading.Thread(target = self._captureloop)
		self.capture  = Capture()

	def _captureloop(self):
		while True:
			image   = self.capture.read()
			image   = _resize_image(image, self.size, ratio = True)
			image   = image.convert('L')
			imagetk = ImageTk.PhotoImage(image)

			self.frame.video.configure(image = imagetk)

	def show(self):
		self.thread.start()
		self.root.mainloop()