import math
import pygame


# класс, отвечающий за все, что связано с танком (анимации, движение и т.п.)
class Tank:
    def __init__(self, app, pos):  # метод инициализации танка
        self.x, self.y = pos  # позиция танка

        self.angle = 0  # угол поворота
        self.vel = 0  # текущая скорость
        self.rotation_vel = 0  # направление поворота

        self.rotation_speed = 25  # скорость поворота
        self.speed = 100  # максимальная скорость вперед
        self.front_speed = -25  # максимальная скорость назад
        self.acceleration = 1  # ускорение

        self.base_image = pygame.image.load('assets/tank/Straight/Sprite-0001.png').convert_alpha()  # изображение танка
        self.base_image = pygame.transform.rotate(self.base_image, -90)  # повернутое изображение танка

    def update(self, dt):  # метод, отвечающий за изменение положения в пространстве
        self.angle += self.rotation_vel * dt
        rad = math.radians(-self.angle)
        dy = math.sin(rad) * self.vel * dt
        dx = math.cos(rad) * self.vel * dt

        self.x += dx
        self.y += dy

    def input(self, key_pressed):  # метод, отвечающий за нажатие клавиш
        moved = False
        rotated = False
        if key_pressed[pygame.K_a]:
            rotated = True
            self.rotate(left=True)
        if key_pressed[pygame.K_d]:
            rotated = True
            self.rotate(right=True)
        if key_pressed[pygame.K_w]:
            moved = True
            self.move_forward()
        if key_pressed[pygame.K_s]:
            moved = True
            self.move_front()
        if not moved:
            self.reduce_speed()
        if not rotated:
            self.rotate(stop=True)

    def move_forward(self):  # метод, отвечающий за движение вперёд
        self.vel = min(self.vel + self.acceleration, self.speed)

    def move_front(self):  # метод, отвечающий за движение назад
        self.vel = max(self.vel - self.acceleration, self.front_speed)

    def rotate(self, left=False, right=False, stop=False):  # метод, отвечающий за поворот танка
        if left:
            self.rotation_vel = self.rotation_speed
        if right:
            self.rotation_vel = -self.rotation_speed
        if stop:
            self.rotation_vel = 0

    def reduce_speed(self):  # метод, отвечающий за инерцию
        self.vel = max(self.vel - self.acceleration * 2, 0)

    def draw(self, screen):  # метод отрисовки танка
        rotated_img = pygame.transform.rotate(self.base_image, self.angle)
        rect = rotated_img.get_rect(center=(self.x, self.y))
        screen.blit(rotated_img, rect)
