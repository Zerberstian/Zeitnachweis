from src.User_Input import is_valid_time

from collections.abc import Callable
from pathlib import Path
import flet as ft
import json
import re



def main(page: ft.Page):
    page.title = "Routes Example"

    print("Initial route:", page.route)

    # async macht den Handler asynchron; await wartet auf den Routenwechsel,
    # ohne dabei den UI-Ereignisablauf waehrenddessen zu blockieren.
    async def open_mail_settings(e):
        await page.push_route("/bums")

    async def open_settings(e):
        await page.push_route("/dings")

    async def entry_dings(e):
        await page.push_route("/dings/entry_dings")

    async def anzeige_dings(e):
        await page.push_route("/dings/anzeige_dings")

    async def to_root(e):
        await page.push_route("/")
    
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
        
    time_entries_column = ft.Column(
        expand=True,
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
        controls=[],
    )

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
        
    # Baut den sichtbaren View-Stack passend zur aktuellen URL (page.route) neu auf.
    def route_change():
        #print("Route change:", page.route)
        page.views.clear()
        # Die Startseite bleibt immer die unterste View im Navigations-Stack.
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.SafeArea(
                        content=ft.Column(
                            controls=[
                                ft.AppBar(title=ft.Text("Flet app")),
                                ft.Container(
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
                                                                on_click=open_settings, 
                                                            ),
                                                            ft.Button(
                                                                content="Nutzer anlegen",
                                                                on_click=open_mail_settings,
                                                            ),
                                                        ]
                                                    )

                                                ]   
                                        )
                                    
                                    )
                            ]
                        )
                    )
                ],
            )
        )
        
        right_frames = ft.Row(
            expand=7,
            vertical_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[],
        )
        # Unterseiten behalten /dings als vorherige View im Navigations-Stack.
        if page.route == "/dings" or page.route.startswith("/dings/"):
            page.views.append(
                ft.View(
                    route="/dings",
                    controls=[
                        ft.SafeArea(
                            content=ft.Column(
                                controls=[
                                    ft.Button(
                                        content="Ausloggen",
                                        on_click=to_root,
                                    ),
                                    ft.Column(
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
                                                                            on_click=entry_dings,
                                                                            
                                                                        ),
                                                                        ft.Button(
                                                                            expand=True,
                                                                            content="Übersicht",
                                                                            on_click=anzeige_dings,
                                                                        ),
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
                                ]
                            )
                        )
                    ],
                )
            )

        if page.route == "/dings/entry_dings":
            page.views.append(
                ft.View(
                    route="/dings/entry_dings",
                    controls=[
                        ft.SafeArea(
                            content=ft.Column(
                                controls=[
                                    ft.AppBar(
                                        title=ft.Text("Registrierungs Bums"),
                                        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                                    ),
                                    ft.Column(
                                        expand=True,
                                        spacing=10,
                                        controls=[
                                            entry_family_name,
                                            entry_middle_name,
                                            entry_first_name,
                                            start_time,
                                            end_time,
                                            ft.Button(content="Einreichen", on_click=lambda: print("knecht")),
                                        ],
                                    ),
                                    ft.Column(
                                        expand=True,
                                        spacing=10,
                                        controls=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                )
            )

        if page.route == "/dings/anzeige_dings":
            page.views.append(
                ft.View(
                    route="/dings/anzeige_dings",
                    controls=[
                        ft.SafeArea(
                            content=ft.Column(
                                controls=[
                                    ft.AppBar(
                                        title=ft.Text("Übersicht"),
                                        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                                    ),
                                    time_entries_column,
                                ],
                            ),
                        ),
                    ],
                )
            )
        '''
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
                            ft.Button(content="Einreichen", on_click=print("knecht")),
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
        '''

        TimeEntriesDisplayFrame = ft.Container(
            expand=True,
            padding=20,
            bgcolor=ft.Colors.GREEN_50,
            visible=False,
            content=time_entries_column,
        )


        frame_list = [TimeEntriesDisplayFrame]
        right_frames.controls = frame_list
        # Die Mail-Seite wird nur fuer genau diese tiefere Route hinzugefuegt.
        if page.route == "/bums":
            page.views.append(
                ft.View(
                    route="/bums",
                    controls=[
                        ft.SafeArea(
                            content=ft.Column(
                                controls=[
                                    ft.AppBar(
                                        title=ft.Text("Registrierungs Bums"),
                                        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                                    ),
                                    #ft.Text("Mail settings!"),
                                ]
                            )
                        )
                    ],
                )
            )
        # Uebernimmt die neu zusammengestellten Views in die Anzeige.
        page.update()

    # Wird aufgerufen, wenn der Nutzer eine View per Zurueck-Navigation schliesst.
    async def view_pop(e):
        if e.view is not None:
            #print("View pop:", e.view)
            #page.views.remove(e.view)
            # Nach dem Entfernen zeigt die oberste uebrige View die Zielroute.
            top_view = page.views[0]
            #await page.push_route(top_view.route)
            await page.pop_views_until("/dings", result="Done!")

    # Flet ruft diese Handler bei Routenwechsel bzw. Zurueck-Navigation auf.
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Erstellt beim Start direkt die Views fuer die aktuelle Route.
    route_change()


if __name__ == "__main__":
    ft.run(main)