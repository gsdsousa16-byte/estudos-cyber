#Mini scanner de portas
alvo = "192.168.1.1"
portas = [80, 443, 22, 3306, 8080, 21, 23, 8443]

print("Iniciando scan no alvo:", alvo)
print("-" * 35)

for porta in portas:
    if porta == 21:
        print("Porta", porta, "-FTP detectado! Risco alto")
    elif porta == 22:
        print("Porta", porta, "-SSH detectado!")
    elif porta == 3306:
        print("Porta", porta, "-Banco de dados exposto!")
    elif porta == 23:
        print("Porta", porta, "-Telnet detectado! Risco alto")
    else:
        print("Porta", porta, "-sem risco imediato")

print("-" * 35)
print("Scan finalizado!")