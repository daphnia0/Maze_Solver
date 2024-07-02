from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __add__(self, o):
        return Point(self.x + o.x, self.y + o.y)
    
    def __floordiv__(self, o):
        return Point(self.x // o, self.y // o)
        

class Line:
    def __init__(self,point_1,point_2) -> None:
        self.point_1 = point_1
        self.point_2 = point_2
        
    def draw(self,canvas,fill_color):
        canvas.create_line(self.point_1.x,self.point_1.y,self.point_2.x,self.point_2.y,fill=fill_color, width=2)
        
class Cell:
    has_left_wall = True
    has_right_wall = True
    has_top_wall = True
    has_bottom_wall = True
    
    def __init__(self,point_1,point_2,win) -> None:
        self._win = win
        self._point_topleft = point_1
        self._point_bottomright = point_2
        self.center = (self._point_topleft + self._point_bottomright) // 2
    
    def draw(self):
        if (self.has_left_wall):
            left_line = Line(self._point_topleft,Point(self._point_topleft.x,self._point_bottomright.y))
            self._win.draw_line(left_line,"black")
        if (self.has_bottom_wall):
            bottom_line = Line(Point(self._point_topleft.x,self._point_bottomright.y),self._point_bottomright)
            self._win.draw_line(bottom_line,"black")
        if (self.has_right_wall):
            right_line = Line(Point(self._point_bottomright.x,self._point_topleft.y),self._point_bottomright)
            self._win.draw_line(right_line,"black")
        if (self.has_top_wall):
            top_line = Line(self._point_topleft,Point(self._point_bottomright.x,self._point_topleft.y))
            self._win.draw_line(top_line,"black")
            
    def draw_move(self, to_cell, undo=False):
        if undo:
            line_color = "grey"
        else:
            line_color = "red"
        between_cell_line=Line(self.center,to_cell.center)
        self._win.draw_line(between_cell_line,line_color)

class Window:
    def __init__(self,width,height):
        self._rootWidget = Tk()
        self._rootWidget.title("Maze Solver")
        self._rootWidget.protocol("WM_DELETE_WINDOW",self.close)
        
        self._canvasWidget = Canvas(self._rootWidget, width=width,height=height)
        self._canvasWidget.pack()
        self._running = False
        
    def draw_line(self,line,fill_color):
        line.draw(self._canvasWidget,fill_color)
        
    def redraw(self):
        self._rootWidget.update_idletasks()
        self._rootWidget.update()
        
    def wait_for_close(self):
        self._running = True
        while(self._running):
            self.redraw()

    def close(self):
        self._running = False
        
        
def main():
    win = Window(800,600)
    cell1 = Cell(Point(100,100),Point(200,200),win)
    cell1.has_bottom_wall = False
    cell1.has_right_wall = False
    cell1.draw()
    cell2 = Cell(Point(100,200),Point(200,300),win)
    cell2.has_top_wall = False
    cell2.draw()
    cell1.draw_move(cell2)
    win.wait_for_close()
    
if __name__ == "__main__":
    main()