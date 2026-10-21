class Widget:
    def __init__(self, master, bg):
        self.master = master
        self.bg = bg

class Frame(Widget):
    def __init__(self, master, bg, width):
        super().__init__(master, bg)  # runs Widget.__init__
        self.width = width

class Button(Widget):
    pass