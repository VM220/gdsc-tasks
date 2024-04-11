import flet as ft #importing the module

from solitaire import Solitaire

def main(page: ft.Page):
    solitaire=Solitaire()
    page.add(Solitaire)

ft.app(target=main)