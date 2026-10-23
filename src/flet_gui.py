import flet as ft


def main(page: ft.Page):

    # Erstellt das Formularfenster und legt seine Größe fest.
    page.title = "Flet Input and Selections Demo"
    page.window.width = 360
    page.window.height = 320

    name = ft.TextField(label="Name")
    agree = ft.Checkbox(label="I agree to the terms")

    # Der Erfahrungsstand kann in elf Stufen von 0 bis 10 gewählt werden.
    level = ft.Slider(
        label="Experience level",
        min=0,
        max=10,
        divisions=10,
        value=5,
    )
    color = ft.Dropdown(
        label="Favorite color",
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )

    # Die Radiobuttons bilden eine Gruppe, aus der eine Option gewählt wird.
    framework = ft.RadioGroup(
        content=ft.Column(
            [
                ft.Radio(value="Flet", label="Flet"),
                ft.Radio(value="Tkinter", label="Tkinter"),
                ft.Radio(value="PyQt6", label="PyQt6"),
                ft.Radio(value="PySide6", label="PySide6"),
            ]
        )
    )
    notifications = ft.Switch(label="Enable notifications", value=True)

    # Fügt alle Formularfelder in der gewünschten Reihenfolge zur Seite hinzu.
    page.add(
        ft.Text("Fill in the form and adjust the options:"),
        name,
        agree,
        level,
        color,
        framework,
        notifications,
    )

ft.run(main)