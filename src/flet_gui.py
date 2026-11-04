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


    def build_rows(items: dict[str, dict[str, object]]) -> list[ft.DataRow]:
        return [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(entry.get("date", entry_id)))),
                    ft.DataCell(ft.Text(str(entry.get("start_time", "")))),
                    ft.DataCell(ft.Text(str(entry.get("end_time", "")))),
                    ft.DataCell(ft.Text(str(entry.get("houers_worked", "")))),
                    ft.DataCell(ft.Text(str(entry.get("minutes_worked", "")))),
                    ft.DataCell(ft.Text(str(entry.get("over_time", "")))),
                ]
            )
            for entry_id, entry in items.items()
        ]
        

    table = ft.DataTable(
        expand=True,
        width=900,
        bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
        border=ft.Border.all(1, ft.Colors.OUTLINE_VARIANT),
        border_radius=10, 
        divider_thickness=1,
        columns=[
            ft.DataColumn(
                label=ft.Text("Datum")
            ),
            ft.DataColumn(
                label=ft.Text("Start")
            ),
            ft.DataColumn(label=ft.Text("Ende")),
            ft.DataColumn(label=ft.Text("Stunden")),
            ft.DataColumn(label=ft.Text("Minuten")),
            ft.DataColumn(label=ft.Text("Überstunden")),
        ],
        rows=[],
    )

    login_family_name = ft.TextField(label="Familienname")
    login_first_name = ft.TextField(label="Vorname")
    login_password = ft.TextField(label="Passwort (123)")

    account_family_name = ft.TextField(label="Familienname")
    account_middle_name = ft.TextField(label="Zweitname (Optional)")
    account_first_name = ft.TextField(label="Vorname")
    account_password = ft.TextField(label="Passwort (123)")

    entry_family_name = ft.TextField(label="Familienname")
    entry_middle_name = ft.TextField(label="Zweitname (Optional)")
    entry_first_name = ft.TextField(label="Vorname")
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
            (login_family_name.value or "").strip(),
            (login_first_name.value or "").strip(),
            (login_password.value or "").strip(),
        )
        login_family_name.error = (
            "Bitte gib einen Familiennamen ein." if not login_data[0] else None
        )
        login_first_name.error = (
            "Bitte gib einen Vornamen ein." if not login_data[1] else None
        )
        login_password.error = (
            "Bitte gib ein Passwort ein" if not login_data[2] else None
        )

        if any((login_family_name.error, login_first_name.error, login_password.error)):
            login_frame.update()
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
            login_family_name.error = "Nachname nicht gefunden"
            login_first_name.error = "Vorname nicht gefunden"
            login_password.error = "Datei nicht vorhanden"
            print(f"Error-code: {error}")
            page.update()
            return
        
        table.rows = build_rows(raw_json_data)
        time_entries_column.controls = [table]
        time_entries_column.update()

        entry_family_name.value = login_data[0]
        entry_first_name.value = login_data[1]
        entry_family_name.disabled = True
        entry_middle_name.disabled = True
        entry_first_name.disabled = True

        login_frame.visible = False
        Content_Parent_Frame.visible = True
        page.update()

        

        
        returns = (json_path)
        return returns
        

    def submit(_):
        input_values = (
            (entry_family_name.value or "").strip(),
            (entry_middle_name.value or "").strip(),
            (entry_first_name.value or "").strip(),
            (start_time.value or "").strip(),
            (end_time.value or "").strip(),
        )

        entry_family_name.error = (
            "Bitte gib einen Familiennamen ein." if not input_values[0] else None
        )
        entry_first_name.error = (
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

        if any((entry_family_name.error, entry_first_name.error, start_time.error, end_time.error)):
            page.update()
            return

        page.update()
        try:
            # The callback handles calculation and saving; its validation errors return to the form.
            on_submit(input_values)
        except ValueError as error:
            end_time.error = str(error)
            page.update()

    def back_to_login(_):
        creation_frame.visible = False
        login_frame.visible = True
        account_family_name.error = None
        account_first_name.error = None
        account_password.error = None
        login_family_name.error = None
        login_first_name.error = None
        login_password.error = None

        page.update()

    def to_cration_frame(_):
        login_frame.visible = False
        creation_frame.visible = True
        account_family_name.error = None
        account_first_name.error = None
        account_password.error = None
        login_family_name.error = None
        login_first_name.error = None
        login_password.error = None
        page.update()

    def create_acc(_):
        new_acc = (
            (account_family_name.value or "").strip(),
            (account_middle_name.value or "").strip(),
            (account_first_name.value or "").strip(),
            (account_password.value or "").strip(),
        )
        account_family_name.error = (
            "Bitte gib einen Familiennamen ein." if not new_acc[0] else None
        )
        account_first_name.error = (
            "Bitte gib einen Vornamen ein." if not new_acc[2] else None
        )
        account_password.error = (
            "Bitte gib ein Passwort ein" if not new_acc[3] else None
        )
        if any((account_family_name.error, account_first_name.error, account_password.error)):
            creation_frame.update()
            page.update()
            return

        page.update()

        def create_json_file(path):
            with path.open("x", encoding="utf-8") as file:
                json.dump({}, file, indent=4, ensure_ascii=False)

        def safe_filename_part(value):
            return re.sub(r"[^\w-]", "_", value, flags=re.UNICODE).strip("_")

        filename = "_".join(
            safe_filename_part(part) for part in (new_acc[0], new_acc[2])
        ) + ".json"
        json_path = Path("Json") / filename

        try:
            json_path.parent.mkdir(parents=True, exist_ok=True)
            create_json_file(json_path)


        except FileExistsError:
            account_family_name.error = "Ein Nutzer mit diesem Namen existiert bereits."
            creation_frame.update()
            page.update()
            return
        except OSError:
            account_family_name.error = "Die Nutzerdatei konnte nicht erstellt werden."
            creation_frame.update()
            page.update()
            return
        
        account_family_name.value = ""
        account_middle_name.value = ""
        account_first_name.value = ""
        account_password.value = ""
        page.update()

    login_frame = ft.Container(
        expand=100,
        content=ft.Column(
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10, 
                    controls= [
                        ft.Text("Anmeldung", size=24),
                        login_family_name,
                        login_first_name,
                        login_password,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Button(
                                    content="   Anmelden   ",
                                    on_click=login, 
                                ),
                                ft.Button(
                                    content="Nutzer anlegen",
                                    on_click=to_cration_frame,
                                ),
                            ]
                        )
        
                    ]   
        )
        
    )


    creation_frame = ft.Container(   
        expand=100,
        visible=False,
        content=ft.Column(
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10, 
                    controls=[
                        ft.Text("Nutzererstellung", size=24),
                        account_family_name,
                        account_middle_name,
                        account_first_name,
                        account_password,
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Button(
                                    content="   Zurück   ",
                                    on_click=back_to_login, 
                                ),
                                ft.Button(
                                    content="   anlegen   ",
                                    on_click=create_acc
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
                        entry_family_name,
                        entry_middle_name,
                        entry_first_name,
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
                    creation_frame,
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