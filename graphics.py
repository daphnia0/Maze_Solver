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
    def __init__(self,point_1,point_2):
        self.point_1 = point_1
        self.point_2 = point_2
        
    def draw(self,canvas,fill_color):
        canvas.create_line(self.point_1.x,self.point_1.y,self.point_2.x,self.point_2.y,fill=fill_color, width=2)
        
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
        
        
