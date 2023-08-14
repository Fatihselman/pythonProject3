ekle = []

print("Listeye istediğiniz kadar değer ekleyebilir, sonra bulmanız gereken sayıyı seçmelisin.")
print("Toplama işaretine tıklamadığınız sürece eklemeye devam edebilirsiniz.")
while True:
    x = input("Eklenecek sayıyı gir ('+' ile bitir): ")

    if x == "+":
        break

    ekle.append(int(x))
    print(sorted(ekle))

hedef = int(input("Listedeki hedef sayıyı girin: "))

baslangic = 0
bitis = len(ekle) - 1

while baslangic <= bitis:
    orta = (baslangic + bitis) // 2
    orta_deger = ekle[orta]

    if orta_deger == hedef:
        print(f"Hedef sayı {orta+1}. pozisyonda bulundu.")
        break
    elif orta_deger < hedef:
        baslangic = orta + 1
    else:
        bitis = orta - 1
else:
    print("Hedef sayı listede bulunamadı.")



