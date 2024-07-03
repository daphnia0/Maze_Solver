from graphics import Window,Point
from cell import Cell


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