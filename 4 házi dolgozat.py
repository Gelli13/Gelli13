m2=float(input("Kérem adja meg a magasságát m-ben: "))
kg=float(input("Kérem adja meg a testsúlyát kg-ben: "))
tti = kg/m2**2
print("*"*30,"-"*5,"*"*30)
print("Az ön testömegindexe: ", round(tti, 2), "%")
TTImin=18.5*m2**2
TTImax=24.99*m2**2
print("Az ön magasságához az ideális testtömeg:", round(TTImin, 2),"és", round(TTImax, 2), "kg között van")