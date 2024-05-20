import flet as ft
from pages.top_page import Top
from pages.chat_page import ChatView


def main(page: ft.Page):
    page.title = "test app"

    def route_change(e):
        route = ft.TemplateRoute(e.route)

        if route.match("/"):
            page.views.clear()
            page.views.append(Top())
        elif route.match("/chat"):
            page.views.clear()
            chat_view = ChatView(page)
            page.views.append(chat_view)
            chat_view.show_dialog(page)

        page.update()

    def view_pop(e):
        page.views.pop()
        page.go("/")

    # ルート変更時のロジック設定
    page.on_route_change = route_change
    # 戻る時のロジック設定
    page.on_view_pop = view_pop
    page.views.clear()
    # 初期表示
    page.go("/")


if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER, port=8080)