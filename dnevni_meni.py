dnevni_meni = {}
x = "yes"
while x == "yes":
    jed = str(input("Vnesite ime jedi:"))
    cena = float(input("Vnesite ceno jedi(v EUR):"))
    dnevni_meni[jed] = cena
    x = str(input("Ali želite v dnevni meni dodati še kakšno jed? (yes/no):"))
    
tekst = open("menu.txt", "w")
y = 1
while y < len(dnevni_meni) + 1:
    for jed, cena in dnevni_meni.items():
        tekst.write("Jed "+ str(y)+ ".: "+ str(jed)+ ","+ " CENA:"+ str(cena)+ "EUR" + "\n")
        y += 1
tekst.close()
    
