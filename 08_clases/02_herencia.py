class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = [0] * num_sides

    def input_sides(self):
        self.sides = [float(input(f'Side {i+1}: ')) for i in range(self.num_sides)]

    def disp_sides(self):
        for i in range(self.num_sides):
            print(f'El lado {i+1} es: {self.sides[i]}')

poly = Polygon(4)
poly.input_sides()
poly.disp_sides()

class Triangle(Polygon):
    pass


class Escaleno(Polygon, Triangle):
    pass