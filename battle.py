def start():
    import pygame as pgm

    pgm.init()
    w, h = 640, 480
    root = pgm.display.set_mode((w, h))
    pgm.display.set_caption("BATTLE")
    root.fill((255, 255, 255))

    class Man:

        def __init__(self):
            self.size = 10
            self.x, self.y = self.size, self.size
            self.color = (0, 0, 0)

        def draw(self):
            pgm.draw.circle(root, self.color, (self.x, self.y), self.size)

    class Weapon:

        def __init__(self, owner):
            self.x, self.y = owner.x, owner.y
            self.size = owner.size // 2
            self.color = (255, 0, 0)

        def draw(self):
            pgm.draw.rect(root, self.color, pgm.Rect(self.x, self.y, self.size * 4, self.size))

    hero = Man()
    weapon = Weapon(hero)
    hero.draw()
    weapon.draw()

    running = True
    while running:
        for event in pgm.event.get():
            if event.type == pgm.QUIT:
                running = False

        pgm.display.flip()

    pgm.quit()
