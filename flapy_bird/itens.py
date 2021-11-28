class Itens:
    
    def __init__(self, win, x, y, w, h, img, r):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.r = r
        self.visible = True
        self.img = img
        self.win = win
    
    def show(self):
        if self.visible:
            self.win.blit(self.img, (self.x, self.y))

