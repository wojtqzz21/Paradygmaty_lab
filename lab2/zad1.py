text = '''Przeczytaj krótki tekst i odpowiedz na kilka pytań, które sprawdzą, czy wszystko zrozumiałeś. 
Możesz wybrać fragmenty artykułów, biogramy pisarzy lub którąś z naszych dowcipnych historyjek.
Uwaga, wybrany tekst możesz rozwiązywać tylko raz dziennie.'''

liczba_slow = list(filter(lambda x: x == " " or x == "." or x == "," or x == "!" or x == "?", text))
print(f'Liczba słów: {len(liczba_slow)}')

liczba_zdan = list(filter(lambda x: x == "." or x == "!" or x == "?", text))
print(f'Liczba zdań: {len(liczba_zdan)}')

liczba_akapitow = list(filter(lambda x: x == "\n", text))
print(f'Liczba akapitów: {len(liczba_akapitow)}')

slowa_1 = text.split(" ")
slowa = set(slowa_1)
slowa = list(slowa)
stop = ["i", "na", "które", "czy", "lub", "z"]
for i in slowa:
    if i in stop:
        slowa_1.remove(i)
print(slowa)
slownik = {i : slowa_1.count(i) for i in slowa}

print(slownik)
posortowany_slownik = sorted(slownik.items(), key=lambda x: x[1], reverse=True)
print(posortowany_slownik)

rev = [i[::-1] for i in slowa if i[0] == "a" or i [0] == "A"]
print(rev)





