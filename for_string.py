#Kirjutage programm, mis käib läbi iga tähe sõnes ja prindib selle välja.

text = "hello"

""" for letter in text:
    print(i) """

#Prindi sõna tagurpidi (viimasest tähemärgist esimese juurde, iga täht sõnast kuvatakse eraldi reale tagurpdi järjekorras).

lenght = len(text)
print(lenght)

for letter in range(len(text) -1, -1, -1):
    print(text[letter])
