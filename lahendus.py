nimi = input("Sisestage nimi: ")
lubatud_kiirus = int(input("Sisestage lubatud kiirus: "))
tegelik_kiirus = int(input("Sisestage tegelik kiirus: "))

kiiruse_uletus = tegelik_kiirus - lubatud_kiirus
trahv = min(300, kiiruse_uletus * 5)

print(nimi + ", kiiruse ületamise eest on teie trahv " + str(trahv) + " eurot")
