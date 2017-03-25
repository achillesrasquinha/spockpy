from spockpy.config import BaseConfig

def _get_video_panel_size(length):
	size = int(length * 0.25)

	return (size, size)

class AppConfig(BaseConfig):
	WINDOW_WIDTH     = 1024
	WINDOW_HEIGHT    = 768
	WINDOW_SIZE      = (WINDOW_WIDTH, WINDOW_HEIGHT)

	VIDEO_PANEL_SIZE = _get_video_panel_size(WINDOW_WIDTH)