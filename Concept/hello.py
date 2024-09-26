import flet as ft

def main(greeting_page: ft.Page):
    greeting_page.add(ft.Text(value="Hello, World"))
    """Hi"""
ft.app(main)