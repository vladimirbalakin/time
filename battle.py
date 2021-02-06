def start():
    import pygame as pgm

    pgm.init()
    w, h = 640, 480
    root = pgm.display.set_mode((w, h))
    pgm.display.set_caption("BATTLE")
    root.fill((255, 255, 255))

    class Man:
        class Weapon:

            def __init__(self, owner):
                self.x, self.y = owner.x, owner.y
                self.size = owner.size // 2
                self.color = (255, 0, 0)
                self.kind = 8
                if owner.kind < 50:
                    self.kind *= -1

            def init(self, owner):
                self.x, self.y = owner.x, owner.y
                self.size = owner.size // 2
                self.color = (255, 0, 0)
                self.kind = 8
                if owner.kind < 50:
                    self.kind *= -1

            def draw(self):
                if self.kind > 0:
                    pgm.draw.rect(root, self.color, pgm.Rect(self.x, self.y, self.size * self.kind, self.size))
                else:
                    pgm.draw.rect(root, self.color, pgm.Rect(self.x + self.size * self.kind, self.y,
                                                             abs(self.size * self.kind), self.size))

        def __init__(self):
            self.size = 20
            self.kind = 100
            self.x, self.y = self.size, h - self.size
            self.color = (0, 0, 0)
            self.weapon = self.Weapon(self)

        def go_evil(self, is_enemy=False):
            self.color = (0, 0, 255)
            if is_enemy:
                self.kind = 0
                self.x = w - self.size

        def draw(self):
            pgm.draw.circle(root, self.color, (self.x, self.y), self.size)
            self.weapon.init(self)
            self.weapon.draw()

    hero = Man()
    enemy = Man()
    enemy.go_evil(True)
    hero.draw()
    enemy.draw()

    running = True
    while running:
        for event in pgm.event.get():
            if event.type == pgm.QUIT:
                running = False

        pgm.display.flip()

    pgm.quit()
