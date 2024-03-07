import pygame

class UserInput():
    def __init__(self):
        self.input = []

    def input_image_and_position(self, image):
        self.input.append(image)

    def is_valid(self):
        if len(self.input) == 2 and self.input[0]["image"] == self.input[1]["image"]:
            return True
        return False