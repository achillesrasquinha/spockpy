# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
from flask import Flask, render_template

# imports - module imports
from spockpy.app.config import ServerConfig
from spockpy.io import HoverPad

app = Flask(__name__,
	static_folder   = ServerConfig.Path.ABSPATH_ASSETS,
	template_folder = ServerConfig.Path.ABSPATH_TEMPLATES
)
pad = HoverPad(verbose = True)
pad.show()

@app.route(ServerConfig.URL.BASE)
def index():
	template = render_template('pages/index.html', title = 'Home', navbar = True)

	return template