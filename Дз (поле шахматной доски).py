def same_color(x1, y1, x2, y2):
    if (x1 + y1) % 2 == (x2 + y2) % 2:
        return True
    else:
        return False

x1, y1 = map(int, input("Введите координаты первой клетки (x1 y1): ").split())
x2, y2 = map(int, input("Введите координаты второй клетки (x2 y2): ").split())

if same_color(x1, y1, x2, y2):
    print(f"Клетки ({x1},{y1}) и ({x2},{y2}) - одного цвета")
else:
    print(f"Клетки ({x1},{y1}) и ({x2},{y2}) - разного цвета")
