import base64
import io
import math
import random
from PIL import Image, ImageDraw


class ToolsService:
    def __init__(self, rand_generator):
        self.rand = rand_generator

    def get_random(self, min_val, max_val):
        # В Python randrange не включает верхнюю границу, как в вашей JS логике
        if min_val >= max_val:
            return min_val
        return self.rand.randint(min_val, max_val - 1)

    def get_random_array_value(self, array):
        return self.rand.choice(array)

    def get_from_warm_colors(self):
        """Генерирует случайный теплый цвет в формате RGB."""
        r = self.rand.randint(180, 255)
        g = self.rand.randint(100, 200)
        b = self.rand.randint(0, 100)
        return (r, g, b)


class PicsService:

    def __init__(self, hash_value):
        # Инициализируем генератор случайных чисел на основе переданного хэша
        self.rand = random.Random(hash_value)
        self.tools = ToolsService(self.rand)

        self.fillers = ["circle", "rect", "line"]
        self.width = 200
        self.height = 200
        self.temp_images = []

        # Создаем холст и объект рисования (аналог Canvas и Context)
        self.image = None
        self.draw = None

    def draw_circle(self):
        x = self.tools.get_random(0, self.width)
        y = self.tools.get_random(0, self.height)
        r = self.tools.get_random(10, 14)

        line_width = self.tools.get_random(5, 10)
        color = self.tools.get_from_warm_colors()

        # В Pillow круг рисуется по границам квадрата (bounding box)
        self.draw.ellipse(
            [x - r, y - r, x + r, y + r], outline=color, width=line_width
        )

    def draw_rect(self):
        size = self.tools.get_random(0, 15)
        x = self.tools.get_random(0, self.width)
        y = self.tools.get_random(0, self.height)

        line_width = self.tools.get_random(5, 10)
        color = self.tools.get_from_warm_colors()

        self.draw.rectangle(
            [x, y, x + size, y + size], outline=color, width=line_width
        )

    def draw_line(self):
        coords = self.get_good_line()
        line_width = self.tools.get_random(5, 10)
        color = self.tools.get_from_warm_colors()

        self.draw.line(
            [coords["x1"], coords["y1"], coords["x2"], coords["y2"]],
            fill=color,
            width=line_width,
        )

    def generate_figures(self):
        figures = []
        length = self.tools.get_random(10, 20)

        for _ in range(length):
            filler = self.tools.get_random_array_value(self.fillers)
            figures.append(filler)

        return figures

    def get_good_line(self):
        length = 150
        x1, x2, y1, y2 = 0, 0, 0, 0
        cond = False

        while not cond:
            x1 = self.tools.get_random(0, self.width)
            x2 = self.tools.get_random(0, self.width)
            y1 = self.tools.get_random(0, self.height)
            y2 = self.tools.get_random(0, self.height)
            length = self.distance(x1, y1, x2, y2)
            cond = 40 < length < 100

        return {"x1": x1, "y1": y1, "x2": x2, "y2": y2}

    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def _to_data_url(self):
        """Вспомогательный метод для конвертации Pillow Image в DataURL (base64)."""
        buffered = io.BytesIO()
        self.image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return f"data:image/png;base64,{img_str}"

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

            if self.rand.random() < 0.25:
                self.temp_images.append(self._to_data_url())

    def finally_get_pic_url(self, size):
        self.width = size
        self.height = size

        # Создаем прозрачный (или черный/белый) холст нужного размера
        self.image = Image.new("RGBA", (self.width, self.height), (0, 0, 0, 0))
        self.draw = ImageDraw.Draw(self.image)

        self.draw_figures()

        return {"pre": self.temp_images, "final": self._to_data_url()}


# --- Пример использования ---
if __name__ == "__main__":
    # Любая строка, число или хэш в качестве сида
    user_hash = "my_unique_hash_string_123"

    # Создаем сервис для конкретного хэша
    service = PicsService(hash_value=user_hash)

    # Генерируем картинку размером 300x300
    result = service.finally_get_pic_url(300)

    # Результат содержит DataURL строки, как и в JS
    print(f"Сгенерировано промежуточных кадров: {len(result['pre'])}")
    print(f"Финальный DataURL (кусок): {result['final'][:60]}...")

    # Для проверки: сохраним финальное изображение на диск
    service.image.save("result_by_hash.png")
    print("Картинка также успешно сохранена в файл 'result_by_hash.png'")

