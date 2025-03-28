from game.load_assets import *
WINDOW_HEIGHT, WINDOW_WIDHT = 640, 480
SCREEN_SIZE = (WINDOW_HEIGHT,WINDOW_WIDHT)
BACKGROUND_COLOR = (30,30,30)
LAYERS_DATA = [
    {
        "image": BACKGROUND_IMAGE,
        "speed": 250
    },
    {
        "image": FOREGROUND_IMAGE,
        "speed": 150
    }
]
FPS = 60
