class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x,y,j):
        self.x = x
        self.y = y
        self.g = j

    def get_coords(self):
        return (self.x, self.y)



pt = Point()
pt.set_coords(1,2, 4)
print(pt.__dict__)
print(pt.get_coords())
