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


def main():
    print("🎲 Willkommen zum Würfelspiel!\n")

    # Spieler*innen erfassen
    anzahl = frage_anzahl_spieler()
    spieler = [frage_spielername(i) for i in range(1, anzahl + 1)]

    # Rundenlimit erfassen
    rundenlimit = frage_rundenlimit()

    print("\n🎮 Das Spiel beginnt!\n")

    # Spielschleife
    for runde in range(1, rundenlimit + 1):
        print(f"\n===== 🌀 Runde {runde} von {rundenlimit} =====")

        for name in spieler:
            print(f"\n👉 {name} ist an der Reihe.")
            input("Drücke ENTER zum Würfeln... ")

            wurf = wuerfeln()
            print(f"🎲 {name} hat eine {wurf} gewürfelt!")

    print("\n🏁 Spiel beendet! Danke fürs Mitspielen.")


if __name__ == "__main__":
    main()
