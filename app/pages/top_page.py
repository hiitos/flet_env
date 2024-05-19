import flet as ft

class Top(ft.View):
    def __init__(self):
        data = "Top data"
        controls = [
            ft.AppBar(title=ft.Text("Flet App Top"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.TextField(value=data, on_change=self.changed),
            ft.ElevatedButton("Go to Chat", on_click=self.clicked)
        ]
        super().__init__("/", controls=controls)
        self.data = data
        
    def clicked(self, e):
        e.page.go("/chat")
    
    def changed(self, e):
        self.data = e.control.value
        self.update()
