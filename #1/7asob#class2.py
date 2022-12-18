class point:
    def __init__(self, x, y, z,):
        self.x = x 
        self.y = y 
        self.z = z 

    def __add__(self, other):
        return point(self.x + other.x ,self.y + other.y, self.z + other.z)
    
    def __str__(self,):

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y and self.z < other.z


pt1 = point(12, 6, -5)
pt2 = point(5, -7, 14)

print(dir(int()))

