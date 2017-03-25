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
from spockpy.config import BaseConfig
from spockpy.io import Capture

class HoverPad(object):
	TITLE = 'HoverPad'

	class Frame(tk.Frame):
		def __init__(self, master = None, size = BaseConfig.HOVERPAD_SIZE):
			self.super   = super(App.Frame, self)
			self.master  = master
			self.size    = size

			self.super.__init__(master)

			self.creatUI()

		def createUI(self):
			currentRow    = 0

			width, height = self.size
			self.video    = tk.Label(self.master,
								     width  = width,
								     height = height)
			self.video.grid(currentRow, 0, stick = tk.E + tk.W + tk.N + tk.S)

	def __init__(self,
				 size  = BaseConfig.HOVERPAD_SIZE):
		self.size    = size

		self.root    = tk.TK()
		self.root.title(HoverPad.TITLE)
		self.root.geometry('{width}x{height}'.format(
			width  = width,
			height = height
		))

		self.frame   = HoverPad.Frame(master = self.root)

		self.thead   = threading.Thread(target = self._captureloop)
		self.capture = Capture()

	def _captureloop(self):
		while True:
			frame   = self.capture.read()
			image   = Image.fromarray(frame)
			imagetk = ImageTk.PhotoImage(image)

			self.frame.video.configure(image = imagetk)

	def show(self):
		self.root.mainloop()