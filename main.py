from graphics import Window,Point
from cell import Cell


def main():
    win = Window(820,820)
    cell1 = Cell(Point(10,10),Point(110,110),win)
    cell1.draw()
    cell2 = Cell(Point(110,10),Point(210,110),win)
    cell2.draw()
    cell3 = Cell(Point(210,10),Point(310,110),win)
    cell3.draw()
    cell4 = Cell(Point(310,10),Point(410,110),win)
    cell4.draw()
    cell5 = Cell(Point(410,10),Point(510,110),win)
    cell5.draw()
    cell6 = Cell(Point(510,10),Point(610,110),win)
    cell6.draw()
    cell6 = Cell(Point(610,10),Point(710,110),win)
    cell6.draw()
    cell6 = Cell(Point(710,10),Point(810,110),win)
    cell6.draw()
    cell1.draw_move(cell2)
    cell2.draw_move(cell3)
    cell3.draw_move(cell4)
    cell4.draw_move(cell5)
    cell5.draw_move(cell6)
    win.wait_for_close()
    
if __name__ == "__main__":
    main()