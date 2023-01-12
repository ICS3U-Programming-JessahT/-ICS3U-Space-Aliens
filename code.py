#!/usr/bin/env python3

# Created By: Jessah
# Date: January 10, 2023
# Space aliens

import stage
import ugame


def game_scene():
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background, 10, 8)

    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()
    while True:
        pass


if __name__ == "__main__":
    game_scene()
