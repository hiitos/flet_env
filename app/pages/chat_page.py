import flet as ft
from components.chat import on_message, send_message_click, join_chat_click

class ChatView(ft.View):
    def __init__(self, page: ft.Page):
        self.page = page
        # Subscribe to pubsub messages
        self.page.pubsub.subscribe(lambda message: on_message(self.page, self.chat, message))

        self.join_user_name = ft.TextField(
            label="Enter your name to join the chat",
            autofocus=True,
            on_submit=lambda e: join_chat_click(e.page, self.join_user_name, self.new_message)
        )
        self.new_message = ft.TextField(
            hint_text="Write a message...",
            autofocus=True,
            shift_enter=True,
            min_lines=1,
            max_lines=5,
            filled=True,
            expand=True,
            on_submit=lambda e: send_message_click(e.page, self.new_message)
        )
        self.chat = ft.ListView(
            expand=True,
            spacing=10,
            auto_scroll=True,
        )
        self.dialog = ft.AlertDialog(
            open=True,
            modal=True,
            title=ft.Text("Welcome!"),
            content=ft.Column([self.join_user_name], width=300, height=70, tight=True),
            actions=[ft.ElevatedButton(text="Join chat", on_click=lambda e: join_chat_click(e.page, self.join_user_name, self.new_message))],
            actions_alignment="end",
        )

        controls = [
            ft.AppBar(
                title=ft.Text("Chat view"),
                bgcolor=ft.colors.SURFACE_VARIANT,
                leading=ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    on_click=lambda e: page.go("/"),
                )
            ),
            ft.Container(
                content=self.chat,
                border=ft.border.all(1, ft.colors.OUTLINE),
                border_radius=5,
                padding=10,
                expand=True,
            ),
            ft.Row(
                [
                    self.new_message,
                    ft.IconButton(
                        icon=ft.icons.SEND_ROUNDED,
                        tooltip="Send message",
                        on_click=lambda e: send_message_click(e.page, self.new_message),
                    ),
                ]
            )
        ]
        super().__init__("/chat", controls=controls)

    def show_dialog(self, page: ft.Page):
        page.dialog = self.dialog
        page.update()