print("Hello, world!")
number = 40 + 2
print(f"Il risultato della somma è {number}")
try:
    number1 = 40 / 0
    print(f"il risultato della divisione è {number1}")
except ZeroDivisionError:
    print("Errore: Non è possibile dividere un numero per zero.")
