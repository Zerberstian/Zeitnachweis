import flet as ft


def main(page: ft.Page):
    def button_clicked(e: ft.Event[ft.Button]):
        print("Leck Eier Fridrich März")

    # Erstellt das Formularfenster und legt seine Größe fest.
    page.title = "Flet Input and Selections Demo"
    page.window.maximized = True
    #page.window.width = 360
    #page.window.height = 320

    page.add(
    ft.SafeArea(
        expand=True,
        content=ft.Row(
            expand=True,
            spacing=20,
            controls=[
                ft.Column(
                    expand=1,
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Row(
                            spacing=10,
                            controls=[
                                ft.Button(
                                    content="Button 1",
                                    on_click=button_clicked,
                                ),

                            ],
                        ),
                        ft.Row(
                            spacing=10,
                            controls=[
                                ft.Button(
                                    content="Button 2",
                                    on_click=button_clicked,
                                ),

                            ],
                        ),
                        ft.Row(
                            spacing=10,
                            controls=[
                                ft.Button(
                                    content="Button 3",
                                    on_click=button_clicked,
                                ),

                            ],
                        ),
                        ft.Row(
                            spacing=10,
                            controls=[
                                ft.Button(
                                    content="Button 4",
                                    on_click=button_clicked,
                                ),

                            ],
                        ),
                    ],
                ),  # Komma zwischen den beiden Columns
                ft.Column(
                    expand=1,
                    alignment=ft.MainAxisAlignment.CENTER,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Text("Zweite Column"),
                        ft.Text("Weitere Inhalte hier"),
                    ],
                ),
            ],
        ),
    ),
    )
    
'''
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

    
        name,
        agree,
        level,
        color,
        framework,
        notifications,
    '''
    
    # Fügt alle Formularfelder in der gewünschten Reihenfolge zur Seite hinzu.
 
ft.run(main)