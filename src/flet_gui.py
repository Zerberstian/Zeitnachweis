from User_Input import is_valid_time

from collections.abc import Callable
from pathlib import Path
import flet as ft
import json
import re


# Callback order: family name, middle name, first name, start time, end time.
SubmittedValues = tuple[str, str, str, str, str]


def main(page: ft.Page, on_submit: Callable[[SubmittedValues], None]):
    page.title = "Flet Input and Selections Demo"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.maximized = True


    family_name = ft.TextField(label="Familienname")
    middle_name = ft.TextField(label="Zweitname (Optional)")
    first_name = ft.TextField(label="Vorname")
    ez_password = ft.TextField(label="Passwort (123)")
    start_time = ft.TextField(label="Startzeit (00:00)")
    end_time = ft.TextField(label="Endzeit (00:00)")

    def login():
        login_data = (
            (family_name.value or "").strip(),
            (first_name.value or "").strip(),
            (ez_password.value or "").strip(),
        )
        family_name.error = (
            "Bitte gib einen Familiennamen ein." if not login_data[0] else None
        )
        first_name.error = (
            "Bitte gib einen Vornamen ein." if not login_data[1] else None
        )
        ez_password.error = (
            "Bitte gib ein Passwort ein"
        )

        login_frame.visible = False
        Content_Parent_Frame.visible = True
        page.update()
        
        '''

        # dass hier bei Content Frame 2 oder so

        def safe_filename_part(value):
            return re.sub(r"[^\w-]", "_", str(value), flags=re.UNICODE).strip("_")

        filename_parts = [login_data[0]]
        filename_parts.append(login_data[1])
        filename = "_".join(safe_filename_part(part) for part in filename_parts) + ".json"
        json_path = Path("Json") / filename

        
        with open(json_path, 'r') as f:
            d = json.load(f)

        print(d)
        '''
        
    def submit(_):
        # strip inputs from gotten Values
        input_values = (
            (family_name.value or "").strip(),
            (middle_name.value or "").strip(),
            (first_name.value or "").strip(),
            (start_time.value or "").strip(),
            (end_time.value or "").strip(),
        )

        family_name.error = (
            "Bitte gib einen Familiennamen ein." if not input_values[0] else None
        )
        first_name.error = (
            "Bitte gib einen Vornamen ein." if not input_values[2] else None
        )
        start_time.error = (
            "Bitte gib eine Startzeit ein."
            if not input_values[3]
            else (
                "Gib eine Uhrzeit im Format HH:MM ein."
                if not is_valid_time(input_values[3])
                else None
            )
        )
        end_time.error = (
            "Bitte gib eine Endzeit ein."
            if not input_values[4]
            else (
                "Gib eine Uhrzeit im Format HH:MM ein."
                if not is_valid_time(input_values[4])
                else None
            )
        )

        if any((family_name.error, first_name.error, start_time.error, end_time.error)):
            page.update()
            return

        page.update()
        try:
            # The callback handles calculation and saving; its validation errors return to the form.
            on_submit(input_values)
        except ValueError as error:
            end_time.error = str(error)
            page.update()

    login_frame = ft.Container(
        expand=100,
        content=ft.Column(
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10, 
                    controls= [
                        family_name,
                        first_name,
                        ez_password,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Button(
                                #expand=True,
                                content="Anmelden",
                                on_click=lambda e: login(), 
                                ),
                                ft.Button(
                                    content="Nutzer anlegen",
                                ),
                            ]
                        )

                        
                    ]   
        )
        
    )

    right_frames = ft.Row(
        expand=7,
        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        controls=[],
    )

    Content_Parent_Frame = ft.Container(
        expand=True,
        visible=False,
        content=ft.Column(
                    expand=True,
                    spacing=10, 
                    controls= ft.Row(
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
                                                        on_click=lambda e: show_frame(Content_Frame_1),
                                                        
                                                    ),
                                                    ft.Button(
                                                        expand=True,
                                                        content="Button 2",
                                                        on_click=lambda e: show_frame(Content_Frame_2)                                            ),
                                                    ft.Button(
                                                        expand=True,
                                                        content="Button 3",
                                                        on_click=lambda e: show_frame(Content_Frame_3),
                                                    ),
                                                    ft.Button(
                                                        expand=True,
                                                        content="Button 4",
                                                        on_click=lambda e: show_frame(Content_Frame_4), 
                                                    ),
                                                ]
                                            )
                                        ],
                                    ),
                                    ft.Row(
                                        expand=True
                                    ),
                                    ft.Row(
                                        expand=True,
                                        controls=[
                                            ft.Button(
                                                expand=False,
                                                content="Settings",
                                                on_click=lambda e: show_frame(Content_Frame_4), 
                                            ),
                                        ],
                                    ),
                                ],
                            ),

                            # Rechter Bereich mit allen Frames
                            right_frames,
                        ],
                    ),
                ),
            )



    # Die vier "Frames" für die rechte Seite
    Content_Frame_1 = ft.Container(
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
                        middle_name,
                        first_name,
                        start_time,
                        end_time,
                        ft.Button(content="Einreichen", on_click=submit),
                    ],
                ),
                ft.Column(
                    expand=True,
                    spacing=10,
                    controls=[],
                ),
            ],
        ),
    )

    Content_Frame_2 = ft.Container(
        expand=True,
        padding=20,
        bgcolor=ft.Colors.GREEN_50,
        content=ft.Text("Inhalt von Frame 2"),
        visible=False,
    )

    Content_Frame_3 = ft.Container(
        expand=True,
        padding=20,
        bgcolor=ft.Colors.AMBER_50,
        content=ft.Text("Inhalt von Frame 3"),
        visible=False,
    )

    Content_Frame_4 = ft.Container(
        expand=True,
        padding=20,
        bgcolor=ft.Colors.PURPLE_50,
        content=ft.Text("Inhalt von Frame 4"),
        visible=False,
    )

    frames = [ Content_Frame_1, Content_Frame_2, Content_Frame_3, Content_Frame_4]
    right_frames.controls = frames

    def show_frame(frame_to_show):
        for frame in frames:
            frame.visible = frame is frame_to_show
        page.update()

    page.add(
        ft.SafeArea(# <= hier dann die Container in eine Row packen zum swappen der inhalte
            expand=True,
            content=ft.Row(
                expand=True,
                vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                spacing=20,
                controls=[
                    login_frame,
                    Content_Parent_Frame,
                ]
            )
        )
    )            
def start_gui(on_submit: Callable[[SubmittedValues], None]) -> None:
    # Flet supplies page; bind the application callback required by main().
    ft.run(lambda page: main(page, on_submit))

if __name__ == "__main__":
    def standalone_submit(values: SubmittedValues) -> None:
        print("Formularwerte:", values)

    start_gui(standalone_submit)