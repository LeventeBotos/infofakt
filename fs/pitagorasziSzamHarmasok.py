# Fájl megnyitása írásra
with open("pitagoraszi_szamharmasok.txt", "w") as f:
    # Számok inicializálása
    szamok = [1, 2, 3]

    while True:
        # Ellenőrizzük, hogy pitagoraszi számhármas-e
        if (szamok[0]**2 + szamok[1]**2 == szamok[2]**2):
            # Eredmény kiírása fájlba
            f.write(f"{szamok[0]}, {szamok[1]}, {szamok[2]}\n")
            print(f"Igaz: {szamok[0]}, {szamok[1]}, {szamok[2]}")

        # A számok növelése
        szamok[2] += 1  # A harmadik számot növeljük folyamatosan
        if szamok[2] > 100:  # Ha elér egy adott határt, visszaállítjuk
            szamok[1] += 1
            szamok[2] = szamok[1] + 1  # A harmadik szám mindig nagyobb kell legyen a másodiknál
        if szamok[1] >= 100:  # Ha a második szám is elér egy határt, növeljük az elsőt
            szamok[0] += 1
            szamok[1] = szamok[0] + 1
            szamok[2] = szamok[1] + 1

        # Ciklus megszakítása egy kritérium alapján
        if szamok[0] > 100:
            break
