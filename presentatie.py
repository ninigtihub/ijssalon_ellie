def presenteer(dict, totaal):
    for key, value in dict.items():
        print(key, ":", value, "euro")
    print("=" * 26)
    print("Totaal", ":", totaal, "euro")