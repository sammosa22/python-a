import json
import os
import random
import re

SAVE_FILE = "spielstand.json"


def frage_anzahl_spieler():
    while True:
        eingabe = input("Wie viele Spieler*innen nehmen teil? (1–99): ")
        if eingabe.isdigit():
            anzahl = int(eingabe)
            if 1 <= anzahl <= 99:
                return anzahl
        print("❌ Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 99 eingeben.\n")


def frage_spielername(nummer):
    muster = r"^[A-Za-zÄÖÜäöüß]+$"
    while True:
        name = input(f"Name für Spieler*in {nummer}: ")
        if re.match(muster, name):
            return name
        print("❌ Ungültiger Name. Bitte nur Buchstaben verwenden.\n")


def frage_rundenlimit():
    while True:
        eingabe = input("Wie viele Runden sollen gespielt werden? (1–50): ")
        if eingabe.isdigit():
            runden = int(eingabe)
            if 1 <= runden <= 50:
                return runden
        print("❌ Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 50 eingeben.\n")


def wuerfeln():
    return random.randint(1, 6)


def bubble_sort_rangliste(rangliste):
    n = len(rangliste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if rangliste[j]["punkte"] < rangliste[j + 1]["punkte"]:
                rangliste[j], rangliste[j + 1] = rangliste[j + 1], rangliste[j]
    return rangliste


def zeige_rangliste(rangliste, runde):
    print(f"\n📊 Rangliste nach Runde {runde}:")
    sortiert = bubble_sort_rangliste(rangliste.copy())
    for platz, eintrag in enumerate(sortiert, start=1):
        print(f" {platz}. {eintrag['name']} – {eintrag['punkte']} Punkte")


def speichern(runde, aktueller_index, rangliste, rundenlimit):
    daten = {
        "runde": runde,
        "aktueller_index": aktueller_index,
        "rangliste": rangliste,
        "rundenlimit": rundenlimit,
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(daten, f, indent=4, ensure_ascii=False)
    print("💾 Spielstand gespeichert!")


def auto_speichern(runde, rangliste, rundenlimit):
    daten = {
        "runde": runde,
        "aktueller_index": 0,  # neue Runde beginnt immer bei Spieler 0
        "rangliste": rangliste,
        "rundenlimit": rundenlimit,
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(daten, f, indent=4, ensure_ascii=False)
    print("💾 (Auto‑Save) Spielstand nach abgeschlossener Runde gespeichert.")


def laden():
    if not os.path.exists(SAVE_FILE):
        return None

    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    print("🎲 Willkommen zum Würfelspiel!\n")

    # Prüfen, ob gespeicherter Spielstand existiert
    gespeicherter_stand = laden()
    if gespeicherter_stand:
        print("📂 Gespeicherter Spielstand gefunden!")
        auswahl = input("Möchtest du das Spiel fortsetzen? (j/n): ").lower()
        if auswahl == "j":
            runde = gespeicherter_stand["runde"]
            aktueller_index = gespeicherter_stand["aktueller_index"]
            rangliste = gespeicherter_stand["rangliste"]
            rundenlimit = gespeicherter_stand["rundenlimit"]
            print("🔄 Spiel wird fortgesetzt...\n")
        else:
            gespeicherter_stand = None

    if not gespeicherter_stand:
        # Neues Spiel starten
        anzahl = frage_anzahl_spieler()
        spieler = [frage_spielername(i) for i in range(1, anzahl + 1)]
        rangliste = [{"name": name, "punkte": 0} for name in spieler]
        rundenlimit = frage_rundenlimit()
        runde = 1
        aktueller_index = 0

    # Spielschleife
    while runde <= rundenlimit:
        print(f"\n===== 🌀 Runde {runde} von {rundenlimit} =====")

        # Rangliste anzeigen (ab Runde 2)
        if runde > 1 and aktueller_index == 0:
            zeige_rangliste(rangliste, runde - 1)

        # Spieler*innen durchgehen
        while aktueller_index < len(rangliste):
            eintrag = rangliste[aktueller_index]
            name = eintrag["name"]

            print(f"\n👉 {name} ist an der Reihe.")
            aktion = input("ENTER = würfeln | 's' = speichern: ")

            if aktion.lower() == "s":
                speichern(runde, aktueller_index, rangliste, rundenlimit)
                continue

            wurf = wuerfeln()
            eintrag["punkte"] += wurf
            print(
                f"🎲 {name} hat eine {wurf} gewürfelt! (Gesamt: {eintrag['punkte']} Punkte)"
            )

            aktueller_index += 1

        # Runde abgeschlossen → Auto‑Save
        auto_speichern(runde, rangliste, rundenlimit)

        # Nächste Runde
        runde += 1
        aktueller_index = 0

    print("\n🏁 Spiel beendet!")
    zeige_rangliste(rangliste, rundenlimit)


if __name__ == "__main__":
    main()
