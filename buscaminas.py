from tkinter import *
import utils 
import settings
from celdas import celdas



root=Tk() 
root.configure(bg="black")
root.title("Buscaminas")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')


top_frame= Frame (root,
                 bg="black",
                 width=settings.WIDTH,
                 height=utils.height_prct(25))


top_frame.place(x=0,y=0)

left_frame=Frame(root,
                 bg="black"
                 ,width=utils.width_prct(25),
                 height=utils.height_prct(75)
                 )
left_frame.place(x=0,y=utils.height_prct(25))

center_frame=Frame(
    root,
    bg="black",
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(x=utils.width_prct(25),y=utils.height_prct(25))
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c=celdas(x,y)
        c.crear_btn_obj(center_frame)
        c.celda_btn_obj.grid(
            column=x,
            row=y
        )

celdas.randomize_minas()
for c in celdas.all:
    print(c.is_mine)    

root.mainloop()
