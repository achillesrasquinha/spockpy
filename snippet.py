# import spockpy
# import cv2

# pad = spockpy.HoverPad(
# 	size     = (640, 480),
# 	position = 'tl',
# 	deviceID = 1,
# 	verbose  = True
# )
# pad.show()

# while True:
# 	event = pad.get()
	
# 	if event.type == spockpy.Event.SPOCK:
# 		print('Spock!')
# 	elif event.type == spockpy.Event.PAPER:
# 		print('Paper!')
# 	elif event.type == spockpy.Event.ROCK:
# 		print('Rock!')
# 	elif event.type == spockpy.Event.SCISSOR:
# 		print('Scissor!')
# 	else:
# 		print('None!')

# # imports - compatibility imports
# from __future__ import absolute_import

# # imports - standard imports
# try:
#     import Tkinter as tk
# except ImportError:
#     import tkinter as tk
# import collections
# import threading

# # imports - third-party imports
# import cv2
# from PIL import Image, ImageTk

# # imports - module imports
# from spockpy.io     import HoverPad
# from spockpy.config import AppConfig
# from spockpy.event  import Event, keycode
# from spockpy._util  import _resize_image

# class App(object):
#     class Frame(tk.Frame):
#         def __init__(self,
#                      master     = None,
#                      windowSize = AppConfig.WINDOW_SIZE):
#             self.master = master

#             tk.Frame.__init__(self, master)

#             self.createUI()

#         def createUI(self):
#             width, height = AppConfig.WINDOW_SIZE
#             # currentRow    = 0

#             # size          = AppConfig.VIDEO_PANEL_SIZE
#             # self.video    = tk.Label(self.master,
#             #                          width  = size[0],
#             #                          height = size[1])

#             # self.video.grid(row    = currentRow,
#             #                 column = 0,
#             #                 sticky = tk.E + tk.W)
#             self.panel      = collections.defaultdict()
#             self.panel['L'] = tk.Frame(self.master, width = width/2 - 10)
#             self.panel['L'].grid(row = 0,
#                                           column = 0,
#                                           sticky = tk.E + tk.W)

#             self.image      = collections.defaultdict()
#             self.image['L'] = tk.Label(self.panel['L'])
#             self.image['L'].grid(row = 0,
#                                  column = 0,
#                                  sticky = tk.E + tk.W)


#             self.button   = tk.Button(self.master, text = 'Play')
#             self.button.grid(row    = 0,
#                              column = 1,
#                              sticky = tk.E + tk.W)
#             self.panel['R'] = tk.Frame(self.master, width = width/2 - 10)
#             self.panel['R'].grid(row = 0,
#                                           column = 2,
#                                           sticky = tk.E + tk.W)
#             self.image['R'] = tk.Label(self.panel['R'])
#             self.image['R'].grid(row = 0,
#                                  column = 0,
#                                  sticky = tk.E + tk.W)


#     def __init__(self,
#                  deviceID   = 0,
#                  position   = 'tl',
#                  windowSize = AppConfig.WINDOW_SIZE):
#         self.deviceID    = deviceID
#         self.position    = position

#         self.windowSize  = windowSize
#         width, height    = self.windowSize

#         self.root        = tk.Tk()
#         self.root.title('%s v%s' % (AppConfig.NAME, AppConfig.VERSION))
#         self.root.geometry('{width}x{height}'.format(
#             width  = width,
#             height = height
#         ))

#         self.frame       = App.Frame(
#             master       = self.root,
#             windowSize   = self.windowSize
#         )

#         self.hoverpad    = HoverPad(
#             deviceID = self.deviceID,
#             position = self.position,
#             size     = (640, 480),
#             verbose  = True,
#         )
#         self.thread      = threading.Thread(target = self.videoloop)

#     def run(self):
#         self.thread.start()
#         self.root.mainloop()

#     def videoloop(self):
#         self.hoverpad.show()

#         while True:
#             event = self.hoverpad.get()
            
#             if   event.type == Event.SPOCK:
#                 print('Spock!')
#             elif event.type == Event.PAPER:
#                 print('Paper!')
#             elif event.type == Event.ROCK:
#                 print('Rock!')
#             elif event.type == Event.SCISSOR:
#                 print('Scissor!')
#             else:
#                 print('None!')
