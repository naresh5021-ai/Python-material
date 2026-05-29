
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<Point x={self.x} y={self.y}>"

p1 = Point(10, 10)
p2 = Point(100, 100)
for p in [p1, p2]:
    print(f"Object {p}")




        