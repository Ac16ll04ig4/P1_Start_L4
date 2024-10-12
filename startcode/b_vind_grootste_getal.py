mijn_lijst = [1,2,3,4,5,6,7,8,9,10]
def vind_grootste_getal(mijn_lijst):
    grootste_getal = 1
    for item in mijn_lijst:
        if item > grootste_getal:
            grootste_getal = item
    print(grootste_getal)
# Schrijf een functie vind_grootste_getal die de grootste waarde uit een lijst teruggeeft.
# Gebruik een for-loop om de grootste waarde te vinden.
vind_grootste_getal(mijn_lijst)