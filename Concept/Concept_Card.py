import flet as ft

def main(page: ft.Page):

    class Solitare:
        def __init__(self):
            self.start_top = 0
            self.start_left = 0
    solitare = Solitare()
    
    def drag(e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.delta_y)
        e.control.left = max(0, e.control.left + e.delta_x)
        e.control.update()
    def drop(e: ft.DragEndEvent):
        for slot in slots:
            if(abs(e.control.top-slot.top) < 40 and abs(e.control.left - slot.left) < 40):
                place(e.control,slot)
                e.control.update()
                return
        bounce_back(solitare, e.control)
        e.control.update()
    def place(card,slot):
        card.top = slot.top
        card.left = slot.left
        page.update()
    def bounce_back(game, card):
        card.top =  game.start_top
        card.left = game.start_left
        page.update()
    def move_on_top(card, controls):
        """Moves draggable card to the top of the stack"""
        controls.remove(card)
        controls.append(card)
        page.update()

    def start_drag(e: ft.DragStartEvent):
        move_on_top(e.control, controls)
        solitare.start_top = e.control.top
        solitare.start_left = e.control.left        
         
    slot0 = ft.Container(
        width = 70, height = 100, left = 0, top = 0, border = ft.border.all(1)
        )
    slot1 = ft.Container(
        width = 70, height = 100, left = 200, top = 0, border = ft.border.all(1)
        )
    slot2 = ft.Container(
        width = 70, height = 100, left = 300, top = 0, border = ft.border.all(1)
        )
    slots = [slot0,slot1,slot2]
    card1 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=4,
        on_pan_start=start_drag,
        on_pan_update=drag,
        on_pan_end=drop,
        left = 0,
        top = 0,
        content = ft.Container(bgcolor=ft.colors.GREEN, width = 70, height = 100)
    )
    card2 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=4,
        on_pan_start=start_drag,
        on_pan_update=drag,
        on_pan_end=drop,
        left = 100,
        top = 0,
        content = ft.Container(bgcolor=ft.colors.YELLOW, width = 70, height = 100)
    )
    controls = [slot0, slot1, slot2, card1, card2]
    page.add(ft.Stack(controls = controls, width=1000, height=100))
    place(card1, slot0)
    place(card2, slot1)


ft.app(main)
