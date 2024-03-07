import pygame
import sys
import os
from app import *

def test_jump():
    jump()
    assert is_jumping == True
    assert jump_count == 10

def test_collision_detection():
    hurdles = [Hurdle(100)]
    global player_x, player_y
    player_x = 100
    player_y = 650 - player_height  # Player at the bottom of the screen
    assert check_collision(hurdles) == True

