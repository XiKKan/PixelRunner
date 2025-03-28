from entities.player import *
from utils.constants import *
from utils.image_movment import *
from load_assets import *


def main():
    pygame.init()
    current_size = SCREEN_SIZE
    screen = display.set_mode(current_size, RESIZABLE, vsync=1)
    clock = time.Clock()
    running = True

    parallax = ParallaxBackground(LAYERS_DATA)
    player = Player(85, 60,)
    player_sprites = sprite.Group()
    player_sprites.add(player)

    while running:
        delta_time = clock.tick(FPS) / 1000.0
        scaled = False
        for Event in pygame.event.get():
            if Event.type == QUIT:
                running = False
            elif Event.type == VIDEORESIZE:
                current_size = display.get_window_size()
                screen = display.set_mode(current_size, RESIZABLE, vsync=1)
                scaled = True

        screen.fill(BACKGROUND_COLOR)

        parallax.scale_image(current_size)
        parallax.update(delta_time, scaled)
        parallax.draw(screen)
        scale_factor = parallax.get_scale_factor()
        player_sprites.update()
        player.update_animation(scale_factor[0], scale_factor[1])
        player.rect.x = player.normalized_position_x * scale_factor[0]
        if not player.is_jump:
            player.rect.y = player.normalized_position_y * scale_factor[1]

        player_sprites.draw(screen)

        player_sprites.draw(screen)
        player.jump()
        player.change_track(delta_time)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
