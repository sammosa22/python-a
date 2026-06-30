import random
import re


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
    # Sortiert absteigend nach Punkten (größte Punkte zuerst)
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


def main():
    print("🎲 Willkommen zum Würfelspiel!\n")

    # Spieler*innen erfassen
    anzahl = frage_anzahl_spieler()
    spieler = [frage_spielername(i) for i in range(1, anzahl + 1)]

    # Punkte initialisieren
    rangliste = [{"name": name, "punkte": 0} for name in spieler]

    # Rundenlimit erfassen
    rundenlimit = frage_rundenlimit()

    print("\n🎮 Das Spiel beginnt!\n")

    # Spielschleife
    for runde in range(1, rundenlimit + 1):
        print(f"\n===== 🌀 Runde {runde} von {rundenlimit} =====")

        # Vor Beginn der Runde Rangliste anzeigen (außer Runde 1)
        if runde > 1:
            zeige_rangliste(rangliste, runde - 1)

        for eintrag in rangliste:
            name = eintrag["name"]
            print(f"\n👉 {name} ist an der Reihe.")
            input("Drücke ENTER zum Würfeln... ")

            wurf = wuerfeln()
            eintrag["punkte"] += wurf

            print(
                f"🎲 {name} hat eine {wurf} gewürfelt! (Gesamt: {eintrag['punkte']} Punkte)"
            )

    # Finale Rangliste
    print("\n🏁 Spiel beendet!")
    zeige_rangliste(rangliste, rundenlimit)


if __name__ == "__main__":
    main()
