from game.utils.constants import *
import pygame


class Player(sprite.Sprite):
    def __init__(self, scale_width, scale_height):
        sprite.Sprite.__init__(self)
        self.scale_width = scale_width
        self.scale_height = scale_height
        self.first_track_position = (100, 160)
        self.second_track_position = (100, 190)
        self.normalized_position_x, self.normalized_position_y = self.first_track_position[0], self.first_track_position[1]
        self.animation = sheet_frames["player"]
        self.current_frame = 0
        self.image = self.animation["run"][self.current_frame]
        self.rect = self.image.get_rect(center=(self.normalized_position_x, self.normalized_position_y))
        self.last_animation_update = time.get_ticks()
        self.animation_speed = 100
        self.jump_count = 7
        self.move_speed = 300
        self.track_number = 0
        self.is_jump = False

    def resize(self, scale_factor_x, scale_factor_y):
        self.image = transform.scale(self.image,
                                     (self.scale_width * scale_factor_x, self.scale_height * scale_factor_y))

    def change_sprite(self, frames_files):
        now = time.get_ticks()
        if now - self.last_animation_update > self.animation_speed * 1.2:
            self.last_animation_update = now
            self.current_frame = (self.current_frame + 1) % len(frames_files)
            self.image = frames_files[self.current_frame]
            self.image = transform.scale(self.image, (self.scale_width, self.scale_height))

    def change_track(self,dt):
        keys = key.get_pressed()
        if keys[K_DOWN]:
            self.track_number = 1
        if keys[K_UP]:
            self.track_number = 0
        if self.track_number:
            if self.normalized_position_y < self.second_track_position[1]:
                self.normalized_position_y += self.move_speed * dt
            self.track_number = 1
        if not self.track_number:
            if self.normalized_position_y > self.first_track_position[1]:
                self.normalized_position_y -= self.move_speed * dt
            self.track_number = 0

    def jump(self):
        keys = key.get_pressed()
        if keys[pygame.K_SPACE] and not self.is_jump:
            self.is_jump = True
        if self.is_jump:
            if self.jump_count >= -7:
                if self.jump_count < 0:
                    self.rect.y += ((self.jump_count ** 2) / 2)
                else:
                    self.rect.y -= ((self.jump_count ** 2) / 2)
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = 7

    def animation_for_action(self):
        if self.is_jump:
            self.change_sprite(self.animation["jump"])
        else:
            self.change_sprite(self.animation["run"])

    def update_animation(self, adapting_parameter_x, adapting_parammeter_y):
        self.animation_for_action()
        self.resize(adapting_parameter_x, adapting_parammeter_y)
