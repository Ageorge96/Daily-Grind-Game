from minigames.woodcutting import *


def test_game_running():
    Woodcutting = WoodcuttingScreen(1000, 650)
    Woodcutting.render()
    print(Woodcutting)
    assert 1 == 2