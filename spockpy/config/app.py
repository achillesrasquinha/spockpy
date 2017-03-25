# imports - compatibility imports
from __future__ import absolute_import

# imports - module imports
from spockpy.config import Config
from spockpy._util  import _round_int

def _get_video_panel_size(length):
	size = _round_int(length * 0.25)

	return (size, size)

class AppConfig(Config):
	WINDOW_WIDTH     = 1024
	WINDOW_HEIGHT    = 768
	WINDOW_SIZE      = (WINDOW_WIDTH, WINDOW_HEIGHT)

	VIDEO_PANEL_SIZE = _get_video_panel_size(WINDOW_WIDTH)