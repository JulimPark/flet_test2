import flet as ft


def main(page: ft.Page):
    aa = ft.Text('안녕하세요')
    page.add(aa)
    pass

ft.app(target=main)