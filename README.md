# BotOfStuudium
Discord bot, mis võtab infot Stuudiumi API kaudu

# Kuidas kasutada?

1. Paigaldada vajalikud teegid programmi tööks:
    - requests
    - html.parser
    - schedule
    - discord
    - sqlite3
    - pandas
2. Konfigureerida ./src/.env fail:
    - Sisestada väärused

3. Jooksutada ./src/main.py


Argo Kamenik, Sass Kristofer Kase, Siim Seppo
Discord bot, mis saadaks sulle notificationi, kui Studiumisse tuleb uus hinne/suhtluses avatakse uus teema
Rollid: 
Argo - Stuudiumi API kaudu info saamine
P3 prototüüp: ./src/parseHTML.py
Programm võtab Stuudiumi hinnetelehe (meil näiteks pandud grades.html) ning tükeldab selle sõnastikuks, kus igal ainel on hinnetest list.
Koostatud sõnastik prinditakse kasutajale.



Siim - Info filtreerimine ja struktuuri lihtsustamine
Prototüübi tööle saamine: Kõik failid kaustast SQLite, mis asub src kaustas ning Hindedtabelistjne.py fail tuleb alla laadida ja siis saab sisestada tabelSQL faili väärtusi ja sealt edasi on võimalik need salvestada database-i. Selle tabeli saab printida välja Pythoni failiga, seda jooksutades, peale SQL faili salvestamist.

Sass - Discord boti ehitamine - On olemas töötav bot, mis ühendub discordi serveriga ja millega saab suhelda slash commandide teel, hetkel on olemas commandid /sayhi, mis paneb boti sind "tervitama" ja /grades, mis viskab ette nii öelda templatei hilisemast funktsionaalsusest. Boti failid asuvad src kaustas ja need on TTWARD.py ja peidetud .env fail, kus on guildi id ja boti key. Selleks et boti teistesse serveritesse panna on hetkel vaja teha väga palju tööd, nii et lihtsam on demonstratsiooni paluda ;)




Drive - https://drive.google.com/drive/folders/1cZ3bADJTOmOyGmkzyNO1s12NqqPMK_D4?usp=sharing
Trello - https://trello.com/invite/b/9jEKvNzn/f4161eb71675c5c55bf3125747134c1c/thistotallywontresultinasecuritybreach
