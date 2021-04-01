

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def get(self):
        return (self.x, self.y)


class Rectangle:

    def __init__(self, bottom_left: Point, top_right: Point):
        self._bottom_left = bottom_left
        self._top_right = top_right
        self._width = self._top_right.x - self._bottom_left.x
        self._height = self._top_right.y - self._bottom_left.y

    def contains(self, point: Point):
        return ((self._bottom_left.x <= point.x <= self._top_right.x) and
               (self._bottom_left.y <= point.y <= self._top_right.y))

    def is_intersect(self, rect):
        return not (rect._bottom_left.x > self._top_right.x or
                    rect._top_right.x < self._bottom_left.x  or
                    rect._bottom_left.y > self._top_right.y or
                    rect._top_right.y < self._bottom_left.y) 



class QuadTree:

    def __init__(self, rect: Rectangle, capacity: int=4):
        self._rect = rect
        self._members = []
        self._capacity = capacity
        self.is_divided = False


    def subdivide(self):
        ne_bottom_left = Point(self._rect._bottom_left.x + self._rect._width/2, self._rect._bottom_left.y + self._rect._height/2)
        ne_top_right = Point(self._rect._top_right.x, self._rect._top_right.y)
        self._north_east = QuadTree(Rectangle(ne_bottom_left, ne_top_right))
        
        nw_bottom_left = Point(self._rect._bottom_left.x, self._rect._bottom_left.y + self._rect._height/2)
        nw_top_right = Point(self._rect._top_right.x - self._rect._width/2, self._rect._top_right.y)
        self._north_west = QuadTree(Rectangle(nw_bottom_left, nw_top_right))
        
        sw_bottom_left = Point(self._rect._bottom_left.x, self._rect._bottom_left.y)
        sw_top_right = Point(self._rect._top_right.x - self._rect._width/2, self._rect._top_right.y - self._rect._height/2)
        self._south_west = QuadTree(Rectangle(sw_bottom_left, sw_top_right))
        
        se_bottom_left = Point(self._rect._bottom_left.x + self._rect._width/2, self._rect._bottom_left.y)
        se_top_right = Point(self._rect._top_right.x, self._rect._top_right.y - self._rect._height/2)
        self._south_east = QuadTree(Rectangle(se_bottom_left, se_top_right))

        self.is_divided = True

    def add(self, point):
        if not self._rect.contains(point):
            return
        if len(self._members) < self._capacity:
            self._members.append(point)
        else:
            if not self.is_divided:
                self.subdivide()
            self._north_east.add(point)
            self._north_west.add(point)
            self._south_east.add(point)
            self._south_west.add(point)


    def query(self, rect:Rectangle, found=[]):
        if not self._rect.is_intersect(rect):
            return found
        for p in self._members:
            if rect.contains(p):
                found.append(p)
        if self.is_divided:
            found = self._north_east.query(rect, found)
            found = self._north_west.query(rect, found)
            found = self._south_east.query(rect, found)
            found = self._south_west.query(rect, found)
        return found


def draw_rectangle(axis, rect:Rectangle, color='k'):
    axis.plot([rect._bottom_left.x, rect._top_right.x],
              [rect._bottom_left.y, rect._bottom_left.y], color=color)
    axis.plot([rect._top_right.x, rect._top_right.x],
              [rect._bottom_left.y, rect._top_right.y], color=color)
    axis.plot([rect._top_right.x, rect._bottom_left.x],
              [rect._top_right.y, rect._top_right.y], color=color)
    axis.plot([rect._bottom_left.x, rect._bottom_left.x],
              [rect._top_right.y, rect._bottom_left.y], color=color)
    return axis

def draw_points(axis, point_list, color='b'):
    for point in point_list:
        axis.scatter(point.x, point.y, marker='*', c=color)
    return axis

def quad_tree_plotter(ax, qtree, color='k'):
    
    ax = draw_rectangle(ax, qtree._rect)
    ax = draw_points(ax, qtree._members)
    # print("_members")
    # print(qtree._members)
    draw_more = qtree.is_divided
    if draw_more:
        ax = quad_tree_plotter(ax, qtree._north_east, 'r')
        ax = quad_tree_plotter(ax, qtree._north_west, 'g')
        ax = quad_tree_plotter(ax, qtree._south_west, 'b')
        ax = quad_tree_plotter(ax, qtree._south_east, 'm')
    return ax


def test():
    import numpy as np
    np.random.seed(123)
    num_test_samples = 100
    bottom_left = Point(0, 0)
    top_right = Point(200, 200)
    big_rectangle = Rectangle(bottom_left, top_right)
    qtree = QuadTree(big_rectangle)
    points = [Point(np.random.uniform(bottom_left.x, top_right.x),
              np.random.uniform(bottom_left.y, top_right.y)) for _ in range(num_test_samples)]
    for point in points:
        # point.show()
        qtree.add(point)

    test_bottom_left = Point(50, 50)
    test_top_right = Point(120, 120)
    test_rectangle = Rectangle(test_bottom_left, test_top_right)

    test_found_points = qtree.query(test_rectangle)

    import matplotlib.pyplot as plt
    fig =  plt.figure()
    ax0 = fig.add_subplot(111)
    ax0 = quad_tree_plotter(ax0, qtree)
    ax0 = draw_rectangle(ax0, test_rectangle, 'g')
    draw_points(ax0, test_found_points, 'r')
    plt.show()


if __name__ == '__main__':
    test()

