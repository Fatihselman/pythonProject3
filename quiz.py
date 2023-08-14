sorulars = [
    {
        "soru": "İlk matbaayı Osmanlıya kim getirmiştir?",
        "cevap": "ibrahim müteferrika"
    },
    {
        "soru": "Bu dünyanın en zeki insanı kimdir?",
        "cevap": "Fatih Selman Aygün"
    },
    {
        "soru": "İstanbul'un fethi kaç yılında gerçekleşmiştir?",
        "cevap": "1453"
    }
]

print("Quiz yarışmamıza hepiniz hoş geldiniz!!!")
doğru_sayısı = 0
soru_sayısı = len(sorulars)

for soru in sorulars:
    print("\n", soru['soru'])
    verilen_cevap = input("Lütfen cevabı giriniz: ")

    if verilen_cevap.lower() == soru['cevap'].lower():
        print("Doğru cevap!\n")
        doğru_sayısı += 1
    else:
        print("Maalesef yanlış cevap.\n")

puan = (doğru_sayısı / len(sorulars)) * 100
print(f"Test tamamlandı, puanınız: {puan}")

