from pygame import *
import os


def load_animation_frames(folder_path, name):
    frames = []
    frame_count = len(os.listdir(folder_path))
    for i in range(frame_count):
        frame_path = os.path.join(folder_path, f"{name}_{i}.png")
        if os.path.exists(frame_path):
            frames.append(image.load(frame_path))
    return frames


sheet_frames = {
    "player": {"death": load_animation_frames('assets/player/death', 'Death'),
               "run": load_animation_frames('assets/player/run', 'Run'),
               "jump": load_animation_frames('assets/player/jump', 'Jump')}
}

BACKGROUND_IMAGE = image.load('assets/background/Background.png')
FOREGROUND_IMAGE = image.load('assets/background/Foreground.png')
