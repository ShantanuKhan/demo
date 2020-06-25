class Circle:
    id = 0
    radius = 0
    color = ""

    def __init__(self, id, radius, color):
        self.id = id
        self.radius = radius
        self.color = color
    
    def circumference(self):
        return 2.14 * 2 * self.radius