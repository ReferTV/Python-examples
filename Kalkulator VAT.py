print("Wprowadź liczbę do której ma zostać dodany podatek")
x = input()
x = int(x)
print("A teraz wprowadź podatek VAT obowiązujący w twoim kraju")
podatek = input()
y = float(podatek)
y = y*0.01
wynik=x+x*y
print(wynik)

