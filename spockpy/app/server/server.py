# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
import json

# imports - third-party imports
from flask import Flask, Response, render_template, request
import numpy as np

# imports - module imports
from spockpy.app.config import ServerConfig
from spockpy.io import HoverPad
from spockpy.event import Event
from spockpy._util import _image_to_bytes, _base64_str_to_image

import spockpy

HOVERPAD_SIZE      = (640, 480)
HOVERPAD_DEVICE_ID = 0
HOVERPAD_VERBOSE   = True

app = Flask(__name__,
	static_folder   = ServerConfig.Path.ABSPATH_ASSETS,
	template_folder = ServerConfig.Path.ABSPATH_TEMPLATES
)
pad = HoverPad(deviceID = HOVERPAD_DEVICE_ID, size = HOVERPAD_SIZE, verbose = HOVERPAD_VERBOSE)
pad.show()

def _get_gesture_name(event):
	type_ = event.type

	if event.type == Event.ROCK:
		return 'rock'
	if event.type == Event.SCISSOR:
		return 'scissor'
	if event.type == Event.PAPER:
		return 'paper'
	if event.type == Event.NONE:
		return 'none'

@app.route(ServerConfig.URL.BASE)
def index():
	template = render_template('pages/index.html', title = 'Home', navbar = True)

	return template

def generate_video_stream():
	while True:
		image  = pad.get_image()
		bytes_ = _image_to_bytes(image, format_ = '.png')

		yield (b'--frame\r\n'
               b'Content-Type: image/png\r\n\r\n' + bytes_ + b'\r\n')

@app.route(ServerConfig.URL.VIDEO_STREAM)
def videostream():
	return Response(generate_video_stream(), mimetype = 'multipart/x-mixed-replace; boundary=frame')

@app.route(ServerConfig.URL.DETECT, methods = ['POST'])
def detect():
	# data     = request.json
	# print(data)
	data     = request.values['image']
	image    = _base64_str_to_image(data)

	array    = np.asarray(image)

	event    = spockpy.detect(array)

	gesture  = _get_gesture_name(event)

	response = { 'type': gesture }

	return json.dumps(response)