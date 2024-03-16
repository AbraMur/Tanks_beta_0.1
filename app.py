import pygame
import config
from grid import Grid
from tank import Tank
from rect import Rect
from bullet import Bullet


# основной класс в котором происходят все события
class App(object):
    def __init__(self):  # метод инициализации
        self.screen = pygame.display.set_mode((config.WIN_WIDTH, config.WIN_HEIGHT))  # чтобы окошечко было
        self.running = True  # переменная что бы работал главный цикл
        self.clock = pygame.time.Clock()

        self.objects = []  # набор объектов

        self.grid = Grid()  # переменная класса сетки
        self.objects.append(self.grid)  # добавляет объект сетка в список
        self.grid.create_perlin_map()
        self.grid_dict = self.grid.get()

        self.rect = Rect()  # переменная класса rect

        self.tank = Tank(self, (100, 100))  # экземпляр танка
        self.tank_box = self.rect.collision_pos((100, 100), config.tank_width, config.tank_height)  # получаем точки танка
        self.objects.append(self.tank)  # добавляет объект танк в список

        self.bullets = []  # список выпущенных снарядов

    def update(self, dt):  # метод
        for obj in self.objects:
            obj.update(dt)
        for bull in self.bullets:
            bull.fly(dt)

    def event_handler(self, event):  # обработчик событий
        if event.type == pygame.QUIT:
            self.stop()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.stop()
            if event.key == pygame.K_g:
                self.bullets.append(Bullet((self.tank.x, self.tank.y), self, self.tank.rotate, self.tank))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(self.grid.globloc(event.pos[0], event.pos[1]))

    def input(self):  # метод, который проверяет нажатие клавиш
        for obj in self.objects:
            obj.input(pygame.key.get_pressed())

    def run(self):  # метод, который отвечает за бесконечный цикл программы
        while self.running:
            for event in pygame.event.get():
                self.event_handler(event)

            dt = self.clock.tick(config.FPS)/1000  # вычисляем delta time

            self.input()
            self.border_map()
            self.update(dt)
            self.draw()

    def border_map(self):  # метод, в котором проверяется выход снаряда за карту
        for bull in self.bullets:
            if bull.x > 150 or bull.x < 0:
                self.bullets.pop(self.bullets.index(bull))
            if bull.y > 150 or bull.y < 0:
                self.bullets.pop(self.bullets.index(bull))

    def draw(self):  # метод отрисовки
        self.screen.fill(config.WHITE)

        for obj in self.objects:
            obj.draw(self.screen)
        pygame.display.update()

        for bull in self.bullets:
            bull.draw(self.screen)

    def stop(self):  # останавливаем работу кода
        self.running = False


if __name__ == '__main__':
    game = App()
    game.run()
