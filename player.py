from enum import Enum

import arcade

from fish_animation import FishAnimation

class Direction(Enum):
    """
    Simple direction enum for left and right.
    """
    LEFT = 0
    RIGHT = 1


class Player:
    """
    Player class for the fish!
    """
    MOVEMENT_SPEED = 5
    PLAYER_LIVES = 3
    def __init__(self, spritesheet_path, scale):
        self.scale = scale
        self.left_animation = FishAnimation(spritesheet_path, scale=self.scale)
        self.right_animation = FishAnimation(spritesheet_path, flip=True, scale=self.scale)
        self.current_animation = None

        self.direction = Direction.LEFT
        if self.direction == Direction.LEFT:
            self.current_animation = self.left_animation
        else:
            self.current_animation = self.right_animation

        self.lives = Player.PLAYER_LIVES
        self.animation_list = arcade.SpriteList()

    def draw(self):
        self.animation_list.draw()

    def update(self, delta_time):
        self.current_animation.scale = self.scale
        self.current_animation.center_x += self.current_animation.change_x
        self.current_animation.center_y += self.current_animation.change_y

        self.current_animation.on_update(delta_time)

        self.animation_list.clear()
        self.animation_list.append(self.current_animation)

    def change_direction(self, new_direction):
        """
        Used to update the animation according to the direction.
        :param new_direction: The new direction.
        :return: None
        """
        old_direction = self.direction
        if old_direction == new_direction:
            return
        self.direction = new_direction
        if self.direction == Direction.LEFT:
            self.left_animation.center_x = self.current_animation.center_x
            self.left_animation.center_y = self.current_animation.center_y
            self.current_animation = self.left_animation
        else:
            self.right_animation.center_x = self.current_animation.center_x
            self.right_animation.center_y = self.current_animation.center_y            
            self.current_animation = self.right_animation      
