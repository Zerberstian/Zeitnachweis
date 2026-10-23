## Überlegungsschema/Struktur

```
arbeitszeit-rechner/
├── src/
│   ├── main                 # Programmstart
│   ├── berechnung           # Arbeitszeit und Summen berechnen
│   ├── modelle              # Datenmodell für einen Arbeitstag
│   ├── eingabe              # Konsolen- oder GUI-Eingabe
│   ├── ausgabe              # Ergebnisse anzeigen
│   ├── speicherung          # Einträge speichern und laden
│   └── export               # Druck-/PDF-Ausgabe
├── tests/
│   ├── test_berechnung
│   └── test_speicherung
└── README

```


## für venv in Code Terminal 

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass 
```

## activate Venv

```
.\.venv\Scripts\Activate.ps1 
```
## pip install flet

```
python -m pip install flet      
```

## für run

```
.\.venv\Scripts\python.exe .\src\flet_gui.py  
```
