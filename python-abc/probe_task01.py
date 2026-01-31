#!/usr/bin/python3
from task_01_duck_typing import Circle, Rectangle, Shape

def probe():
    print("Circle is subclass of Shape:", issubclass(Circle, Shape))
    print("Rectangle is subclass of Shape:", issubclass(Rectangle, Shape))

    # Negative / zero inputs
    for r in [5, 0, -1, "5"]:
        try:
            Circle(r)
            print("Circle(", r, ") OK")
        except Exception as e:
            print("Circle(", r, ") ->", type(e).__name__, e)

    for w, h in [(4,7), (0,7), (-1,2), ("4",7)]:
        try:
            Rectangle(w,h)
            print("Rectangle(", w, ",", h, ") OK")
        except Exception as e:
            print("Rectangle(", w, ",", h, ") ->", type(e).__name__, e)

if __name__ == "__main__":
    probe()
