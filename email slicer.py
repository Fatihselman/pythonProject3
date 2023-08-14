import time

print("Hoş geldin email bölücüye")

time.sleep(2)

x = input("Lütfen email adresini girer misin hemen: ")
x.split("@")
(username, domain)=(x.split("@"))
(domain,adress) = domain.split(".")

print(f"Username:{username} ")
print(f"Domain:{domain} ")
print(f"Adress:{adress} ")