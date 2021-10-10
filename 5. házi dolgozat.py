print("Japán naptár")
a = int(input("Adjon meg egy évszámot: "))
if 1984 > a or a > 2043:
    print("Ez az év nem a ciklus része")
elif a % 10 == 1 or 2:
    print("Ez az év zöld")
elif a % 10 == 3 or 4:
    print("Ez az év piros")
elif a % 10 == 5 or 6:
    print("Ez az év sárga")
elif a % 10 == 7 or 8:
    print("Ez az év fehér")
elif a % 10 == 9 or 0:
    print("Ez az év fekete")
