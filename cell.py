from graphics import Line, Point

class Cell:
    has_left_wall = True
    has_right_wall = True
    has_top_wall = True
    has_bottom_wall = True
    
    def __init__(self,point_1,point_2,win) -> None:
        self._win = win
        self._point_topleft = point_1
        self._point_bottomright = point_2
        self._point_topright = Point(self._point_bottomright.x,self._point_topleft.y)
        self._point_bottomleft = Point(self._point_topleft.x,self._point_bottomright.y)
        self.center = (self._point_topleft + self._point_bottomright) // 2
    
    def draw(self):
        if (self.has_left_wall):
            left_line = Line(self._point_topleft,self._point_bottomleft)
            self._win.draw_line(left_line,"black")
        if (self.has_bottom_wall):
            bottom_line = Line(self._point_bottomleft,self._point_bottomright)
            self._win.draw_line(bottom_line,"black")
        if (self.has_right_wall):
            right_line = Line(self._point_topright,self._point_bottomright)
            self._win.draw_line(right_line,"black")
        if (self.has_top_wall):
            top_line = Line(self._point_topleft,self._point_topright)
            self._win.draw_line(top_line,"black")
            
    def draw_move(self, to_cell, undo=False):
        if undo:
            line_color = "grey"
        else:
            line_color = "red"
        between_cell_line=Line(self.center,to_cell.center)
        self._win.draw_line(between_cell_line,line_color)