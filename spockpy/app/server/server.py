# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
from flask import Flask, Response, render_template
import numpy as np

# imports - module imports
from spockpy.app.config import ServerConfig
from spockpy.io import HoverPad
from spockpy._util import _image_to_byte_array

DEVICE_ID = 1
VERBOSE   = True

app = Flask(__name__,
	static_folder   = ServerConfig.Path.ABSPATH_ASSETS,
	template_folder = ServerConfig.Path.ABSPATH_TEMPLATES
)
pad = HoverPad(deviceID = DEVICE_ID, verbose = VERBOSE)
pad.show()

@app.route(ServerConfig.URL.BASE)
def index():
	template = render_template('pages/index.html', title = 'Home', navbar = True)

	return template

def generate_video_stream():
	while True:
		image  = pad.get_image()
		bytes_ = _image_to_byte_array(image)

		yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + bytes_ + b'\r\n')

@app.route(ServerConfig.URL.VIDEO_STREAM)
def videostream():
	return Response(generate_video_stream(), mimetype = 'multipart/x-mixed-replace; boundary=frame')