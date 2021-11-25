def test(wybor):
     for wybor in range(wybor):
          print("Wpisz pierwszą liczbę")
          x = int(input())
          print("Wpisz drugą liczbę")
          y = int(input())

          z = x+y

          print("Wynik to ", z)


wybor = int(input("\033[1;37;40mIle razy chcesz wykonać działanie?\n"))

test(wybor)

print("\033Gotowe, czy chcesz jeszcze powtórzyć działania?")
print("\033Wpisz liczbę działań do potwórzenia lub 'n' aby anulować")

tn = input()

if tn == "n":
     print("Okej, zakoćzyłem pracę")

else:
	test(wybor)