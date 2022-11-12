palavra_secreta = "CHOCOLATE"
palpite = str(input("INFORME SEU PALPITE")).upper()
acertou = bool(palpite == palavra_secreta)
print("ACERTOU? ",acertou)