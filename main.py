import flet as ft #importing the module

class Solitaire:
    def __init__(self):
        self.start_top=0
        self.start_left=0

def main(page: ft.Page):
    def place(card,slot):
        """place card to the slot"""
        card.top=slot.top
        card.left=slot.left

    def bounce_back(game,card):
        """return to original slot"""
        card.top=game.start_top
        card.left=game.start_left

    def move_on_top(card,controls):
        """Move draggable card to the top"""
        controls.remove(card)
        controls.append(card)
        page.update()   

    def start_drag(e: ft.DragStartEvent):
        move_on_top(e.control,controls)
        solitaire.start_top=e.control.top
        solitaire.start_left=e.control.left
        
    def drag(e: ft.DragUpdateEvent):
        e.control.top=max(0,e.control.top + e.delta_y)
        e.control.left=max(0,e.control.left + e.delta_x)
        e.control.update()
    
    def drop(e: ft.DragEndEvent):
        for slot in slots:
          if( abs(e.control.top - slot.top)< 20 and  abs(e.control.left - slot.left)< 20 ):
            place(e.control,slot)
            e.control.update()
            return
        bounce_back(solitaire,e.control)
        e.control.update()

    slot0=ft.Container(width=70,height=100,left=0,top=0,border=ft.border.all(1))
    slot1=ft.Container(width=70,height=100,left=200,top=0,border=ft.border.all(1))
    slot2=ft.Container(width=70,height=100,left=300,top=0,border=ft.border.all(1))
    slots=[slot0,slot1,slot2]

    card1=ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_start=start_drag,
        on_pan_update=drag,
        on_pan_end=drop,
        top=0,
        left=0,
        content=ft.Container(bgcolor=ft.colors.GREEN,width=70,height=100),
    )

    card2=ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_start=start_drag,
        on_pan_update=drag,
        on_pan_end=drop,
        top=0,
        left=100,
        content=ft.Container(bgcolor=ft.colors.YELLOW,width=70,height=100),
    )
    controls=[slot0,slot1,slot2,card1,card2]
    place(card1,slot0)
    place(card2,slot1)
    solitaire=Solitaire()
   
    page.add(ft.Stack(controls=controls,width=1000,height=500))
    
   
ft.app(target=main)