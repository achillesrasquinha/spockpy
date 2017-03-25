# imports - compatibility imports
from __future__ import absolute_import

# imports - app imports
from spockpy.app import app
from spockpy.app.config import ServerConfig

if __name__ == '__main__':
	host = ServerConfig.HOST
	port = ServerConfig.PORT

	app.run(host = host, port = port, threaded = True)