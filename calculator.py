def topla():
    x = int(input("Bir sayı giriniz: "))
    y = int(input("Bir sayı daha giriniz: "))
    return x + y

def çıkar():
    x = int(input("Bir sayı giriniz: "))
    y = int(input("Bir sayı daha giriniz: "))
    return x - y

def çarp():
    x = int(input("Bir sayı giriniz: "))
    y = int(input("Bir sayı daha giriniz: "))
    return x * y

def böl():
    x = int(input("Bir sayı giriniz: "))
    y = int(input("Bir sayı daha giriniz: "))
    return x / y

def kareal():
    x = int(input("Bir sayı giriniz: "))
    y = int(input("Bir sayı daha giriniz: "))
    return x ** y

print("1=topla")
print("2=çıkar")
print("3=çarp")
print("4=böl")
print("5=kareal")

seçim = int(input("Lütfen bir seçim yapınız: "))

if seçim == 1:
    print(topla())
elif seçim == 2:
    print(çıkar())
elif seçim == 3:
    print(çarp())
elif seçim == 4:
    print(böl())
elif seçim == 5:
    print(kareal())
else:
    print("Geçersiz seçim! Lütfen 1 ile 5 arasında bir seçim yapın.")
