import random

print("Lütfen yazmak istediğiniz kadar seçenek yazdıktan sonra ayrılmak için 1'e basın.")

isimlistesi = []

while True:
    x = input("Lütfen bir isim giriniz: ")

    if x == "1":
        break

    isimlistesi.append(x)
    print(isimlistesi)

if isimlistesi:
    random_index = random.randint(0, len(isimlistesi) - 1)
    secilen_isim = isimlistesi[random_index]
    print(f"Rastgele seçilen isim: {secilen_isim}")
else:
    print("Listeye bir şey eklemediniz.")
