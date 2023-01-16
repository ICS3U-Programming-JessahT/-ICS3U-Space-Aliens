#!/usr/bin/env python3

# Created By: Jessah
# Date: January 10, 2023
# Space aliens

import stage
import ugame


def game_scene():
    #  import background image
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # sheet
    background = stage.Grid(image_bank_background, 10, 8)
    person = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # display the image
    game = stage.Stage(ugame.display, 60)
    game.layers = [person] + [background]
    game.render_block()
    # loop the game
    while True:
        # user input, buttons on pyBadge
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            print("A")
        if keys & ugame.K_O:
            print("B")
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        if keys & ugame.K_RIGHT:
            person.move(person.x + 1, person.y)
        if keys & ugame.K_LEFT:
            person.move(person.x - 1, person.y)
        if keys & ugame.K_UP:
            person.move(person.x, person.y - 1)
        if keys & ugame.K_DOWN:
            person.move(person.x, person.y + 1)
        # game logic
        # redraw sprite
        game.render_sprites([person])
        game.tick()


if __name__ == "__main__":
    game_scene()
