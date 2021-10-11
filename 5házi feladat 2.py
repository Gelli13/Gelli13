print("Japán naptár")
a = int(input("Adjon meg egy évszámot: "))
b= a % 10
if 1984 > a or a > 2043:
    print("Ez az év nem a ciklus része")
elif b == 4 or b == 5:
    print("Ez az év zöld")
elif b == 6 or b == 7:
    print("Ez az év piros")
elif b == 8 or b == 9:
    print("Ez az év sárga")
elif b == 1 or  b == 0:
    print("Ez az év fehér")
elif b == 2 or b == 3:
    print("Ez az év fekete")
