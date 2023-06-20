from tkinter import Button
import random
import settings
class Celdas:
    all=[]
    def  __init__(self,x,y,is_mine=False):
        self.is_mine=is_mine
        self.celda_btn_obj=None 
        self.x=x
        self.y=y
        Celdas.all.append(self)
    def crear_btn_obj(self,location):
        btn=Button(
            location,
            width=12,
            height=4
        )    
        btn.bind('<Button-1>',self.izq_click_actions)#izquierdo
        btn.bind('<Button-3>',self.der_click_actions)#derecho
        self.celda_btn_obj=btn

    def izq_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()  
    def surrounded_cells(self)          
    def show_cell(self):
        surrounded_cells=[
            self.get_cells_por_axis(self.x-1,self.y-1),
            self.get_cells_por_axis(self.x-1,self.y),
            self.get_cells_por_axis(self.x-1,self.y+1),
            self.get_cells_por_axis(self.x,self.y-1),
            self.get_cells_por_axis(self.x+1,self.y-1),
            self.get_cells_por_axis(self.x+1,self.y),
            self.get_cells_por_axis(self.x+1,self.y+1),
            self.get_cells_por_axis(self.x,self.y+1)
        ]
        Celda=[celdas for celdas in Celda if celdas is not None]
        print(Celda)
    def surrounded_cells_mines_length(self):
        counter = 0
        for celdas in self.surrounded_cells:
            if celdas.is_mine:
                counter += 1

        return counter

    def get_cells_por_axis(self,x,y):
        for cell in Celdas.all:
            if Celdas.x == x and Celdas.y == y:
                return Celdas
    def show_mine(self):
        self.celda_btn_obj.configure(bg="red")        
    def der_click_actions(self, event):
        print(event)
        print("soy dercho")
    @staticmethod
    def randomize_minas():
        elegir_celdas=random.sample(
            Celdas.all, settings.MINES
        )
        for elegir_celda in elegir_celdas:
            elegir_celda.is_mine=True
    def __repr__(self):
        return f"Celda({self.x},{self.y})"