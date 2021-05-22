""" Implementation of a player (Fighter) """

class Fighter(pygame.sprite.Sprite):

    def __init__(self, x, y, images):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages(images)
        self.image = self.i01
        self.imageNum = 0
        self.frameRefreshRate = 2
        self.frameStatus = 0
        self.frameStatusRRate = 10
        self.frame = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.isplayerone = True
        self.idle = True
        self.hp = False
        self.mp = False
        self.lp = False
        self.hpc = False
        self.mpc = False
        self.lpc = False
        self.ko = False
        self.win = False

    def loadImages(self, images):
        self.i00 = pygame.image.load(images[0]).convert_alpha()
        self.i01 = pygame.image.load(images[1]).convert_alpha()
        self.i02 = pygame.image.load(images[2]).convert_alpha()
        self.i03 = pygame.image.load(images[3]).convert_alpha()
        self.i11 = pygame.image.load(images[4]).convert_alpha()
        self.i12 = pygame.image.load(images[5]).convert_alpha()
        self.i13 = pygame.image.load(images[6]).convert_alpha()
        self.i21 = pygame.image.load(images[7]).convert_alpha()
        self.i22 = pygame.image.load(images[8]).convert_alpha()
        self.i23 = pygame.image.load(images[9]).convert_alpha()
        self.images = (
            self.i00, self.i01, self.i02, self.i03, self.i11, self.i12, self.i13, self.i21, self.i22, self.i23)

    def update(self):
        self.status()
        if self.isplayerone:
            self.image = self.images[self.imageNum]
        else:
            self.image = pygame.transform.flip(self.images[self.imageNum], True, False)

    def draw(self, Surface):
        Surface.blit(self.image, (self.rect.x, self.rect.y))

    def status(self):
        if self.idle:
            self.frame += 1
            if self.frame >= self.frameRefreshRate:
                if (self.imageNum >= 0) and (self.imageNum < 3):
                    self.imageNum += 1
                else:
                    self.imageNum = 0
                self.frame = 0
        if self.hp:
            self.frameStatus += 1
            self.imageNum = 4
            if self.frameStatus > self.frameStatusRRate:
                self.imageNum = 0
                self.frameStatus = 0
                self.hp = False
        if self.mp:
            self.frameStatus += 1
            self.imageNum = 5
            if self.frameStatus > self.frameStatusRRate:
                self.imageNum = 0
                self.frameStatus = 0
                self.mp = False
        if self.lp:
            self.frameStatus += 1
            self.imageNum = 6
            if self.frameStatus > self.frameStatusRRate:
                self.imageNum = 0
                self.frameStatus = 0
                self.lp = False
        if self.hpc:
            self.frameStatus += 1
            self.imageNum = 7
            if self.frameStatus > self.frameStatusRRate:
                self.imageNum = 0
                self.frameStatus = 0
                self.hpc = False
        if self.mpc:
            self.frameStatus += 1
            self.imageNum = 8
            if self.frameStatus > self.frameStatusRRate:
                self.imageNum = 0
                self.frameStatus = 0
                self.mpc = False
        if self.lpc:
            self.frameStatus += 1
            self.imageNum = 9
            if self.frameStatus > self.frameStatusRRate:
                self.imageNum = 0
                self.frameStatus = 0
                self.lpc = False