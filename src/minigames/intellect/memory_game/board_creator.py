import pygame
import random

image_list = ["banana.png", "bear.png", "cherry.png", "chocolate.png", "cookie.png", "green_apple.webp"]


class BoardCreator():
    def __init__(self):
        self.images_on_board = []
        self.selected_images = []
    @staticmethod
    def random_image(self):
        return random.choice(image_list)
    
    def generate_board(self, cards):
        images = image_list * 2  # Duplicate the image list to create pairs
        random.shuffle(images)  
        for position in cards:
            display_image = images.pop()  # Take an image from the shuffled list
            self.images_on_board.append({"position": position, "image": display_image})

    def add_selected_images(self, image):
        self.selected_images.append(image)
    
    
   

            
