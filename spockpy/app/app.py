# imports - standard imports
try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk

# imports - module imports
from spockpy.config import AppConfig

class App(object):
	class Frame(tk.Frame):
		def __init__(self, master = None):
			self.master = master

			tk.Frame.__init__(self, master)

			self.createUI()

		def createUI(self):
			pass

	def __init__(self,
				 windowSize = AppConfig.WINDOW_SIZE):
		self.windowSize = windowSize
		width, height   = self.windowSize

		self.root       = tk.Tk()
		self.root.title('%s v%s' % (AppConfig.NAME, AppConfig.VERSION))
		self.root.geometry('{width}x{height}'.format(
			width  = width,
			height = height
		))

		self.frame      = App.Frame(self.root)

	def run(self):
		self.root.mainloop()
