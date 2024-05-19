import flet as ft

class Message():
    def __init__(self, user_name: str, text: str, message_type: str):
        self.user_name = user_name
        self.text = text
        self.message_type = message_type

class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment="start"
        self.controls=[
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(message.user_name)),
                color=ft.colors.WHITE,
                bgcolor=self.get_avatar_color(message.user_name),
            ),
            ft.Column(
                [
                    ft.Text(message.user_name, weight="bold"),
                    ft.Text(message.text, selectable=True),
                ],
                tight=True,
                spacing=5,
            ),
        ]

    def get_initials(self, user_name: str):
        return user_name[:1].capitalize()

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]

def join_chat_click(page, join_user_name, new_message):
    if not join_user_name.value:
        join_user_name.error_text = "Name cannot be blank!"
        join_user_name.update()
    else:
        page.session.set("user_name", join_user_name.value)
        page.dialog.open = False
        new_message.prefix = ft.Text(f"{join_user_name.value}: ")
        page.pubsub.send_all(Message(user_name=join_user_name.value, text=f"{join_user_name.value} has joined the chat.", message_type="login_message"))
        page.update()

def send_message_click(page, new_message):
    if new_message.value != "":
        print(f"receive send message: {new_message.value}")
        page.pubsub.send_all(Message(page.session.get("user_name"), new_message.value, message_type="chat_message"))
        new_message.value = ""
        new_message.focus()
        page.update()

def on_message(page, chat, message: Message):
    print(f"receive message on on_message: {message.text}")
    if message.message_type == "chat_message":
        mes = ChatMessage(message)
    elif message.message_type == "login_message":
        mes = ft.Text(message.text, italic=True, color=ft.colors.BLACK45, size=12)
    chat.controls.append(mes)
    chat.update()
    page.update()
