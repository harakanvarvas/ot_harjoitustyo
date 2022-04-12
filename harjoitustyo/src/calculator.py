

class Calculator:

    def calculate(amount, frequency, last):

        if int(last) == 0:
            result = int(amount) * int(frequency)
        elif int(amount) == 0:
            result = 0
        elif int(frequency) == 0:
            result = 0
        elif int(amount) < 0:
            return False
        elif int(frequency) < 0:
            return = False
        elif int(last) < 0:
            return False
        elif int(amount) == 1:
            return f"Aikuistuminen tapahtuu arviolta {int(last)} päivän kuluttua"


        else:
            result = (int(amount) - 1) * int(frequency) + int(last)

        if result > 7:
            result = result // 7
            return f"Aikuistuminen tapahtuu arviolta {result} viikon kuluttua"

        elif result <= 7:
            return f"Aikuistuminen tapahtuu arviolta {result} päivän kuluttua"

        else:
            return result
