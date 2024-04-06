# класс, отвечающий за вычисление крайних точек объектов
class Rect:
    def __init__(self):
        pass

    # @property
    # def topleft(self):
    #     return self.center[0] - self.width // 2, self.center[1] - self.height // 2
    #
    # def collide(self, rect: 'Rect') -> bool:
    #     return True

    def collision_pos(self, center, width, height):  # метод, в котором вычисляются крайние точки объекта
        x0, y0 = center

        x1 = x0 - width // 2
        y1 = y0 - height // 2

        x2 = x0 + width // 2
        y2 = y0 - height // 2

        x3 = x0 - width // 2
        y3 = y0 + height // 2

        x4 = x0 + width // 2
        y4 = y0 + height // 2

        return [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
