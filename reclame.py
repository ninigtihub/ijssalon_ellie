from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    aanbieding = prijs - korting * prijs
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {aanbieding} euro."
    return uitvoer

print(aanbieding_1("aardbei", 4, 0.1))


def inkomsten_totaal(btw, inkomsten):
    totaal = sum(inkomsten)
    bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    return uitvoer

print(inkomsten_totaal(0.09, inkomsten = [220, 430, 125, 160, 205, 90, 345]))


def laag_en_hoog(mijn_lijst):
    max1 = max(mijn_lijst)
    min1 = min(mijn_lijst)
    return max1, min1

print(laag_en_hoog(mijn_lijst = [220, 430, 125, 160, 205, 90, 345]))


def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    bedrag = totaal / 7
    uitvoer = f"De gemiddelde inkomsten deze week zijn {bedrag} euro."
    return uitvoer

print(gemiddelde(mijn_lijst = [220, 430, 125, 160, 205, 90, 345]))


def meervoudig(invoer_lijst):
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer

print(meervoudig(invoer_lijst = [10,5,3,2,1,2,9]))


def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer