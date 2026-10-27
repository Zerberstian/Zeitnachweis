import flet as ft



def main(page: ft.Page):
    page.title = "Flet Input and Selections Demo"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.maximized = True


    family_name = ft.TextField(label="Familienname")
    first_name = ft.TextField(label="Vorname")
    start_time = ft.TextField(label="Startzeit (00:00)")
    end_time = ft.TextField(label="Endzeit (00:00)")

    def submit(_):

        input_values = [
            (family_name.value or "").strip(),
            (first_name.value or "").strip(),
            (start_time.value or "").strip(),
            (end_time.value or "").strip(),
        ]
        print(input_values)

    # Die vier "Frames" für die rechte Seite
    frame1 = ft.Container(
        expand=True,
        padding=20,
        bgcolor=ft.Colors.BLUE_50,
        content=ft.Row(
                    expand=True,
                    spacing=10, 
                    controls=[
                            ft.Column(
                                expand=True,
                                spacing=10,
                                controls=[
                                    family_name,
                                    first_name,
                                    start_time,
                                    end_time,
                                ],
                            ),
                            ft.Column(
                                expand=True,
                                spacing=10,
                                controls=[
                                    ft.Button(content="Einreichen", on_click=submit)
                                    ]
                            ),
        
                    ],
                )
    )

    frame2 = ft.Container(
        expand=True,
        padding=20,
        bgcolor=ft.Colors.GREEN_50,
        content=ft.Text("Inhalt von Frame 2"),
        visible=False,
    )

    frame3 = ft.Container(
        expand=True,
        padding=20,
        bgcolor=ft.Colors.AMBER_50,
        content=ft.Text("Inhalt von Frame 3"),
        visible=False,
    )

    frame4 = ft.Container(
        expand=True,
        padding=20,
        bgcolor=ft.Colors.PURPLE_50,
        content=ft.Text("Inhalt von Frame 4"),
        visible=False,
    )

    frames = [frame1, frame2, frame3, frame4]

    def show_frame(frame_to_show):
        for frame in frames:
            frame.visible = frame is frame_to_show
        page.update()

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Row(
                expand=True,
                vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                spacing=20,
                controls=[
                    # Linke Column mit den Navigations-Buttons
                    ft.Column(
                        expand=1,
                        spacing=10,
                        controls=[
                            ft.Row(
                                expand=True,
                                vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                                controls=[
                                    ft.Column(
                                        expand=True,
                                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                                        controls=[
                                            ft.Button(
                                                expand=True,
                                                content="Button 1",
                                                on_click=lambda e: show_frame(frame1),
                                                
                                            ),
                                            ft.Button(
                                                expand=True,
                                                content="Button 2",
                                                on_click=lambda e: show_frame(frame2)                                            ),
                                            ft.Button(
                                                expand=True,
                                                content="Button 3",
                                                on_click=lambda e: show_frame(frame3),
                                            ),
                                            ft.Button(
                                                expand=True,
                                                content="Button 4",
                                                on_click=lambda e: show_frame(frame4), 
                                            ),
                                        ]
                                    )
                                ],
                            ),
                            ft.Row(
                                expand=True
                            ),
                            ft.Row(
                                expand=True
                            ),
                        ],
                    ),

                    # Rechter Bereich mit allen Frames
                    ft.Row(
                        expand=7,
                        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                        controls=frames,
                    ),
                ],
            ),
        ),
    )


ft.run(main)
