import pygame

class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.active = False


    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        if not self.active:
            pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        else:
            pygame.draw.rect(win, (255, 133, 153), (self.x,self.y,self.width,self.height),0)
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 22)
            if not self.active:
                text = font.render(self.text, 1, (0,0,0))
            else:
                text = font.render(self.text, 1, (255,255,255))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False