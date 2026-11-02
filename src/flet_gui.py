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


    family_name = ft.TextField(label="Familienname")#, hint_text=login[0])
    middle_name = ft.TextField(label="Zweitname (Optional)")
    first_name = ft.TextField(label="Vorname")#, hint_text=login[1])
    ez_password = ft.TextField(label="Passwort (123)")
    start_time = ft.TextField(label="Startzeit (00:00)")
    end_time = ft.TextField(label="Endzeit (00:00)")

    time_entries_column = ft.Column(
        expand=True,
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
        controls=[],
    )

    def login(_):
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
            "Bitte gib ein Passwort ein" if not login_data[2] else None
        )

        if any((family_name.error, first_name.error, ez_password.error)):
            page.update()
            return

        def safe_filename_part(value):
            return re.sub(r"[^\w-]", "_", value, flags=re.UNICODE).strip("_")

        filename = (
            "_".join(safe_filename_part(part) for part in login_data[:2]) + ".json"
        )
        json_path = Path("Json") / filename

        try:
            with open(json_path, "r", encoding="utf-8") as f:
                raw_json_data = json.load(f)
        except (OSError, json.JSONDecodeError) as error:
            ez_password.error = f"Nutzerdatei konnte nicht geladen werden: {error}"
            page.update()
            return

        formatted_json_data = [
            ft.Text(
                f"ID: {eintrag.get('id', eintrag_id)}  \n"
                f"Datum: {eintrag.get('date', '')}  \n"
                f"Start: {eintrag.get('start_time', '')}  \n"
                f"Ende: {eintrag.get('end_time', '')}  \n"
                f"Arbeitszeit: {eintrag.get('houers_worked', 0)} Std. \n"
                f"{eintrag.get('minutes_worked', 0)} Min.\n",
                size=16,
            )
            for eintrag_id, eintrag in raw_json_data.items()
        ]
        time_entries_column.controls = formatted_json_data

        family_name.disabled = True
        middle_name.disabled = True
        first_name.disabled = True
        family_name.update()
        middle_name.update()
        first_name.update()
        
        login_frame.visible = False
        Content_Parent_Frame.visible = True
        page.update()

        '''
        returns = (login_data[0], login_data[1])
        return returns
        '''

    def submit(_):
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
                                    content="   Anmelden   ",
                                    on_click=login, 
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
                                        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                                        controls=[
                                            ft.Column(
                                                expand=True,
                                                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                                                controls=[
                                                    ft.Button(
                                                        expand=True,
                                                        content="Neuer Eintrag",
                                                        on_click=lambda e: show_frame(EntryCreationFrame),
                                                        
                                                    ),
                                                    ft.Button(
                                                        expand=True,
                                                        content="Übersicht",
                                                        on_click=lambda e: show_frame(TimeEntriesDisplayFrame)                                                   ),
                                                ]
                                            )
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
    
    EntryCreationFrame = ft.Container(
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


    TimeEntriesDisplayFrame = ft.Container(
        expand=True,
        padding=20,
        bgcolor=ft.Colors.GREEN_50,
        visible=False,
        content=time_entries_column,
    )


    frame_list = [ EntryCreationFrame, TimeEntriesDisplayFrame]
    right_frames.controls = frame_list

    def show_frame(frame_to_show):
        for frame in frame_list:
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
    ft.run(lambda page: main(page, on_submit))

if __name__ == "__main__":
    def standalone_submit(values: SubmittedValues) -> None:
        print("Formularwerte:", values)

    start_gui(standalone_submit)