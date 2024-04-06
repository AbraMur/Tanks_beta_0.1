import random
import pygame
from config import *
from numpy import floor
from perlin_noise import PerlinNoise


# класс сетки
class Grid(object):
    ''' ВАЖНО ПОНИМАТЬ, ЧТО СЕТКА ИМЕЕТ ВИД dict[(local_x, local_y)] = ((global_x, global_y), height)
    key = (local_x, local_y) values = ((global_x, global_y), height) '''

    def __init__(self):  # создаем переменную "сетки", указываем её тип (словарь)
        self.grid = dict()

        self.heights = []  # набор высот

    def update(self, dt):  # ???
        pass

    def input(self, key_pressed):  # ???
        pass

    def draw(self, screen):  # метод отрисовки сетки
        for i in range(numbers_width_grid + 1):
            for j in range(numbers_height_grid + 1):
                inf = self.grid[(i, j)]
                color = (abs(inf[1] * 100), abs(inf[1] * 100), abs(inf[1] * 100))
                if inf[1]:
                    pygame.draw.circle(screen, color, inf[0], 3)
                    rect = pygame.Rect(inf[0][0] - 3, inf[0][1] + 3, cell_sise, cell_sise)
                    pygame.draw.rect(screen, color, rect)

    def completion(self, heights: list):  # генерируем сетку, где ключ у нас локальные координаты,
        # а значения это глобальные координаты и высота (переводим локальные координаты в глобальные + получаем высоты)
        for i in range(numbers_width_grid + 1):
            for j in range(numbers_height_grid + 1):
                self.grid[(i, j)] = (x_global_coord_grid + width * i / numbers_width_grid - width / (
                            numbers_width_grid * 2),
                                     y_global_coord_grid + height * j / numbers_height_grid - height / (
                                                 numbers_height_grid * 2)), \
                                    heights[i][j]

    def collide(self):
        pass

    def globloc(self, glob_x, glob_y):  # переводим глобальные координаты в локальные
        loc_x = int(glob_x / width * numbers_width_grid)
        loc_y = int(glob_y / width * numbers_height_grid)
        return loc_x, loc_y

    def generate_perlin_noise(self, seed):  # метод генерации высот
        # генерация основного шума и параметризация
        noise = PerlinNoise(octaves=2, seed=seed)  # 4522
        elevation = 1  # высота
        chunk_size = 24  # размер чанка
        terrain_width = max(numbers_width_grid, numbers_height_grid) + 1  # размер карты

        # генерация матрицы для представления ландшафта
        landscale = [[0 for i in range(terrain_width)] for i in range(terrain_width)]

        for position in range(terrain_width ** 2):
            # вычисление высоты y в координатах (x, z)
            x = floor(position / terrain_width)
            z = floor(position % terrain_width)
            y = floor(noise([x / chunk_size, z / chunk_size]) * elevation)
            landscale[int(x)][int(z)] = int(y)

        altitude_L = list(landscale)  # высота

        return altitude_L

    def create_perlin_map(self):
        seed = random.randint(1000, 3000)
        heights = self.generate_perlin_noise(seed)
        self.completion(heights)

    def get(self):  # получаем сетку по запросу
        return self.grid
