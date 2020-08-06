# tee ratkaisu tänne
def kaikki_vaarinpain(lista:list):
    i = -1
    a = 0
    uusi = []
    while a < len(lista):
        sana = lista[i] 
        sana = sana[::-1]
        uusi.append(sana)
        a += 1
        i -= 1
    return uusi

lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
lista2 = kaikki_vaarinpain(lista)
print(lista2)
