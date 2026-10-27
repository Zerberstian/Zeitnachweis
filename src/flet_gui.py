import flet as ft


def main(page: ft.Page):
    page.title = "Flet Input and Selections Demo"
    page.window.maximized = True

    # Die vier "Frames" für die rechte Seite
    frame1 = ft.Container(
        expand=True,
        padding=20,
        bgcolor=ft.Colors.BLUE_50,
        content=ft.Column(
                    expand=True,
                    spacing=10,
                    controls=[
                        ft.TextField(label="Name"),
                    ],
            ),
       
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
