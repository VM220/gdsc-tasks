import flet as ft #importing the module

from solitaire import Solitaire

def main(page: ft.Page):
    solitaire=Solitaire()
    page.add(solitaire)

ft.app(target=main)