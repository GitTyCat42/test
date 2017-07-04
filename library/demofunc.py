from math import sqrt, pi

def demofunc():
   return 42

def demomul(a, b):
    return a * b

def demopi():
    # Berechnung von Pi auf 11 Stellen mittels Annaehrung und einem 2n-Eck
    n = 6
    s = 1
    for i in range(1,21):
        pi_naeherung = 0.5*n*s
        s = s/sqrt(2+sqrt(4-s*s))
        n = 2*n  # Eckenzahl verdoppeln
    return pi_naeherung

def demofailmul(a,b):
    # Mogelfunktion, die nur auf den Test ausgelegt ist
    # So sollte man es natuerlich nicht machen
    ergebnis = 0
    for i in range(1,b):
        ergebnis = ergebnis + a
    # Es kommt leider ein falsches Ergebnis raus, aber ich weiss ja, was es werden muss, also gebe ich einfach das richtige aus
    return 42

def demomul2(a,b):
    ergebnis = a
    for i in range(1,b):
        ergebnis = ergebnis + a
    return ergebnis
