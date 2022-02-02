#Print de tafel van een op te geven getal met input()  Bijv. 1 x 4 = 4 ; 2 x 4 = 8 etc t/m 10 x 4 = 40

print("Geef een nummer")
nummer = int(input())

print("------")
for i in range(1,11):
    print(i * nummer)