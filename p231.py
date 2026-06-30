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
    muster = r"^[A-Za-zÄÖÜäöüß]+$"  # erlaubt nur Buchstaben

    while True:
        name = input(f"Name für Spieler*in {nummer}: ")

        if re.match(muster, name):
            return name

        print("❌ Ungüldcvxcvxcvdddddtiger Name. Bitte nur Buchstaben verwenden.\n")


def main():
    print("🎲 Willkommen zum Würfelspiel!\n")

    anzahl = frage_anzahl_spieler()
    spieler_namen = []

    for i in range(1, anzahl + 1):
        name = frage_spielername(i)
        spieler_namen.append(name)

    print("\n✅ Spieler*innen erfolgreich registriert:")
    for name in spieler_namen:
        print(" -", name)


if __name__ == "__main__":
    main()
