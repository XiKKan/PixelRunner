from game.load_assets import *
from game.utils.math_numb import _get_scale_factor_x_y, _get_speed


class ParallaxLayer:
    def __init__(self, image, speed):
        self.original_image = image
        self.speed = speed
        self.scaled_image = None
        self.image_x = 0.0
        self.new_image_x = float(display.get_window_size()[0])
        self.scale_factor = 0.0
        self.scale_factor_x = 0.0
        self.scale_factor_y = 0.0

    def reset_position(self):
        self.image_x = 0.0
        self.new_image_x = float(self.scaled_image.get_width())

    def update_position(self, is_scaled):
        if is_scaled:
            if self.new_image_x - (self.image_x + self.scaled_image.get_width()) > 0:
                self.new_image_x = self.image_x + self.scaled_image.get_width()

    def _scale_image(self, current_size):
        self.scaled_image = transform.scale(self.original_image, current_size)
        scale_x_y = _get_scale_factor_x_y(self.scaled_image.get_width(), self.scaled_image.get_height(),
                                          self.original_image.get_width(), self.original_image.get_height())
        self.scale_factor_x = scale_x_y[0]
        self.scale_factor_y = scale_x_y[1]

    def update(self, dt):
        dt_minimal = min(dt, 0.1)
        self.image_x -= round(_get_speed(self.speed, self.scale_factor_x) * dt_minimal)
        self.new_image_x -= round(_get_speed(self.speed, self.scale_factor_x) * dt_minimal)
        if self.new_image_x < display.get_window_size()[0] - self.scaled_image.get_width():
            self.reset_position()

    def draw(self, surface):
        surface.blit(self.scaled_image, (int(self.image_x), 0))
        surface.blit(self.scaled_image, (int(self.new_image_x), 0))


class ParallaxBackground:
    def __init__(self, layer_data):
        self.layers = []
        for layer in layer_data:
            new_layer = ParallaxLayer(layer["image"], layer["speed"])
            self.layers.append(new_layer)

    def scale_image(self, current_size):
        for layer in self.layers:
            layer._scale_image(current_size)

    def update(self, dt, is_scaled):
        for layer in self.layers:
            layer.update_position(is_scaled)
            layer.update(dt)

    def draw(self, surface):
        for layer in self.layers:
            layer.draw(surface)

    def get_scale_factor(self):
        return self.layers[1].scale_factor_x, self.layers[1].scale_factor_y
