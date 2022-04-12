from calculator import Calculator

class UiStart:

    def __init__(self):
        self.commands = {
            "1": "Tee uusi arvio selkärangattoman aikuistumisesta",
            "2": "Lopeta"
        }

    def start(self):

        while True:

            for command, explanation in self.commands.items():
                print(command, explanation)

            command = input("Anna komennon numero: ")

            if command not in self.commands:
                print("Virheellinen komento")
            if command == "2":
                print("Suljetaan sovellus")
                break
            if command == "1":
                UiStart.calculation(self)


    def calculation(self):
        while True:
            amount_of_moults = input("Anna jäljelläolevien nahanluontien määrä: ")
            try:
                amount = int(amount_of_moults)
            except ValueError:
                print("Virhe: Määrän tulee olla positiivinen kokonaisluku")
                continue

            if amount < 1:
                print("Virhe: Määrä ei voi olla pienempi kuin 1")
                continue

            break

        while True:
            frequency_of_moults = input("Anna arvioitu nahanluontien taajuus päivinä: ")
            try:
                frequency = int(frequency_of_moults)
            except ValueError:
                print("Virhe: Taajuuden tulee olla positiivinen kokonaisluku")
                continue

            if int(frequency_of_moults) < 0:
                print("Virhe: Taajuus ei voi olla negatiivinen")
                continue

            break

        while True:
            change = input("Muuta aikaa ennen viimeistä nahanluontia? (y/n) ")
            if change.lower() == "y" or change.lower() == "n":
                break
            print("Virhe: Merkki ei ole vaihtoehdoissa")

        if change.lower() == "y":
            while True:
                last_moult = input("Kesto päivinä: ")
                try:
                    last = int(last_moult)
                except ValueError:
                    print("Virhe: Keston tulee olla annettu positiivisena kokonaislukuna")
                    continue

                if int(last_moult) < 0:
                    print("Virhe: Kesto ei voi olla negatiivinen")
                    continue

                break

        elif change.lower() == "n":
            last_moult = 0


        result = Calculator.calculate(amount, frequency, last)

        print(result)
