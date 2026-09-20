
import io
import math
import random
from PIL import Image, ImageDraw

class PicsService:

    def __init__(self, e81):
        self.e81 = e81
        self.fillers = ["circle", "rect", "line"]
        self.width = 200
        self.height = 200
        self.temp_images = []

        # Создаем холст и объект рисования (аналог Canvas и Context)
        self.image = None
        self.draw = None

    def get_random(self, min_val, max_val):
        # В Python randrange не включает верхнюю границу, как в вашей JS логике
        if min_val >= max_val:
            return min_val
        return self.e81.randomFromRange(min_val, max_val - 1)

    def get_random_array_value(self, array):
        return self.e81.getOneByEightBall(array)

    def get_from_warm_colors(self):
        """Генерирует случайный теплый цвет в формате RGB."""
        r = self.e81.randomFromRange(180, 255)
        g = self.e81.randomFromRange(100, 200)
        b = self.e81.randomFromRange(0, 100)
        return (r, g, b)
    
    def draw_circle(self):
        x = self.get_random(0, self.width)
        y = self.get_random(0, self.height)
        r = self.get_random(10, 14)

        line_width = self.get_random(5, 10)
        color = self.get_from_warm_colors()

        # В Pillow круг рисуется по границам квадрата (bounding box)
        self.draw.ellipse(
            [x - r, y - r, x + r, y + r], outline=color, width=line_width
        )

    def draw_rect(self):
        size = self.get_random(0, 15)
        x = self.get_random(0, self.width)
        y = self.get_random(0, self.height)

        line_width = self.get_random(5, 10)
        color = self.get_from_warm_colors()

        self.draw.rectangle(
            [x, y, x + size, y + size], outline=color, width=line_width
        )

    def draw_line(self):
        coords = self.get_good_line()
        line_width = self.get_random(5, 10)
        color = self.get_from_warm_colors()

        self.draw.line(
            [coords["x1"], coords["y1"], coords["x2"], coords["y2"]],
            fill=color,
            width=line_width,
        )

    def generate_figures(self):
        figures = []
        length = self.get_random(10, 20)

        for _ in range(length):
            filler = self.get_random_array_value(self.fillers)
            figures.append(filler)

        return figures

    def get_good_line(self):
        length = 150
        x1, x2, y1, y2 = 0, 0, 0, 0
        cond = False

        while not cond:
            x1 = self.get_random(0, self.width)
            x2 = self.get_random(0, self.width)
            y1 = self.get_random(0, self.height)
            y2 = self.get_random(0, self.height)
            length = self.distance(x1, y1, x2, y2)
            cond = 40 < length < 100

        return {"x1": x1, "y1": y1, "x2": x2, "y2": y2}

    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def draw_figures(self):
        figures = self.generate_figures()
        self.temp_images = []

        for figure in figures:
            if figure == "circle":
                self.draw_circle()
            elif figure == "rect":
                self.draw_rect()
            elif figure == "line":
                self.draw_line()

    def get_pic(self, size):
        self.width = size
        self.height = size

        # Создаем прозрачный (или черный/белый) холст нужного размера
        self.image = Image.new("RGBA", (self.width, self.height), (0, 0, 0, 0))
        self.draw = ImageDraw.Draw(self.image)

        self.draw_figures()

        return {"status": "ok"}

    def do_stuff(self):
        # Генерируем картинку размером 300x300
        self.get_pic(300)

        # Для проверки: сохраним финальное изображение на диск
        self.image.save("result_by_hash.png")
        print("Картинка также успешно сохранена в файл 'result_by_hash.png'")

