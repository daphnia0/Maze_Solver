from cell import Cell
from graphics import Point
import time

class maze:
    def __init__(self, point_1, num_rows, num_cols, cell_size, win):
        self.point_1 = point_1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self.win = win
    
    def _create_cells(self):
        self.cell_list = []
        for i in range(self.num_rows):
            row_list = []
            for j in range(self.num_cols):
                current_point_x = self.point_1.x+(self.cell_size*j)
                current_point_y = self.point_1.y+(self.cell_size*i)
                current_point_upperleft = Point(current_point_x,current_point_y)
                current_point_lowerRight = Point(current_point_x+self.cell_size,current_point_y+self.cell_size)
                current_cell=Cell(current_point_upperleft,current_point_lowerRight,self.win)
                row_list.append(current_cell)
            self.cell_list.append(row_list)
        self._draw_cells()
        self._animate()
    
    def _draw_cells(self):
        for row in self.cell_list:
            for cell in row:
                cell.draw()
                
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)