#Stringhe

# x = "ciao"
# y = 'a tutti'
# print(x)

# #Stringhe multiriga 
# z = """
# a
# a
# a
# a
# """
# print(z)


#le [] con i numeri(indici) al suo interno selezionano il carattere richiesto
x = "ciao"
print(x[0])

#con len dall'inglese lenght vado a prendere la lunghezza dei caratteri contneuti in y

y = "buon natale"
print(len(y))


#ciclo for, mi stampa ogni carattere della stringa da me inserita(in questo caso computer)
for carattere in "computer":
    print(carattere)


#[:3] in questo caso avendo i ":" prende i primi 3 caratteri della stringa
#[3:] in questo caso non seleziona i primi 3 caratteri della stringa 
#[2:7] in questo caso seleziona i caratteri che stanno tra 2 e 7
#[-5] in questo caso essendoci il "-" inizia a prendere gli ultimi caratteri della stringa
#[-5:] in questo caso prende il range di caratteri in questo caso sarebbe "ianni"
#.upper mi consente di modificare i caratteri in maiuscolo
#.lower mi consente di modificare i caratteri in minuscolo
#.strip mi consente di togliere lo spazio in eccesso davanti e alla fine della stringa
#.replace mi consente di rimpiazzare un carattere della stringa con un altro
#.split mi consente di suddividere la stringa in più elementi o stringhe

# a = " ciao sono Gianni "

# print(a[:3])
# print(a[3:])
# print(a[2:7])
# print(a[-5:])
# print(a.upper())
# print(a.upper())
# print(a.strip())
# print(a.replace("o", "k"))
# print(a.split())

# FORMAT

x = 31
y = 70
z = 1.70
test = "Ciao sono Gianni e sono nato il {}, peso {}, e sono altezzo {}"

print(test.format(x,y,z))