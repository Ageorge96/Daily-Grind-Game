class Screen:
    def __init__(self, width, height, data={}):
        self.width = width
        self.height = height
        self.theme = 'style/theme.json'
        self.data = data