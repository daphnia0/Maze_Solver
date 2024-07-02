from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:
    def __init__(self,point1,point2) -> None:
        self.point1 = point1
        self.point2 = point2
        
    def draw(self,canvas,fill_color):
        canvas.create_line(self.point1.x,self.point1.y,self.point2.x,self.point2.y,fill=fill_color, width=2)
        

class Window():
    def __init__(self,width,height):
        self.rootWidget = Tk()
        self.rootWidget.title("Maze Solver")
        self.rootWidget.protocol("WM_DELETE_WINDOW",self.close)
        
        self.canvasWidget = Canvas(self.rootWidget, width=width,height=height)
        self.canvasWidget.pack()
        self.running = False
        
    def draw_line(self,line,fill_color):
        line.draw(self.canvasWidget,fill_color)
        
    def redraw(self):
        self.rootWidget.update_idletasks()
        self.rootWidget.update()
        
    def wait_for_close(self):
        self.running = True
        while(self.running):
            self.redraw()

    def close(self):
        self.running = False
        
        
def main():
    win = Window(800,600)
    line1 = Line(Point(10,10),Point(20,20))
    win.draw_line(line1,"blue")
    line2 = Line(Point(30,10),Point(40,20))
    win.draw_line(line2,"black")
    line3 = Line(Point(200,100),Point(400,500))
    win.draw_line(line3,"green")
    line4 = Line(Point(300,300),Point(123,421))
    win.draw_line(line4,"red")
    line5 = Line(Point(333,444),Point(232,111))
    win.draw_line(line5,"orange")
    
    win.wait_for_close()
    
if __name__ == "__main__":
    main()