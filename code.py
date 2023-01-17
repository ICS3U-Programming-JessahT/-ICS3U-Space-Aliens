#!/usr/bin/env python3

# Created By: Jessah
# Date: January 10, 2023
# Space aliens

import stage
import ugame
import constants


def game_scene():
    #  import background image
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # sheet
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    person = stage.Sprite(image_bank_sprites, 5, 75, 110)

    # display the image
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [person] + [background]
    game.render_block()
    # loop the game
    while True:
        # user input, buttons on pyBadge
        # passes is used so the only buttons but left and right work while playing
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            # used so when sprite goes right it doesn't go out of bounds
            if person.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                person.move(person.x + 1, person.y)
            else:
                person.move(constants.SCREEN_X - constants.SPRITE_SIZE, person.y)
        if keys & ugame.K_LEFT:
            # used so when sprite goes left it doesn't go out of bounds
            if person.x >= 0:
                person.move(person.x - 1, person.y)
            else:
                person.move(0, person.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
        # game logic
        # redraw sprite
        game.render_sprites([person])
        game.tick()


if __name__ == "__main__":
    game_scene()
