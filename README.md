# Obligatorisk laboration

Ni ska skriva ett objekt-orienterat program i Python som räknar ut procentandelen avklarade obligatoriska högskolepoäng. Ett exempel på utskrift när programmet körs kan se ut så här:

```
Alla obligatoriska kurser:
DM1581 Introduktion till medieteknik 6.0 ECTS
SF1625 Envariabelanalys 7.5 ECTS
DM1579 Medieproduktion 6.0 ECTS
DM1578 Programintegrerande kurs i medieteknik 7.0 ECTS
SF1624 Algebra och geometri 7.5 ECTS
DD1318 Programmeringsteknik och tekniska beräkningar 9.0 ECTS
SF1626 Flervariabelanalys 7.5 ECTS
DD1320 Tillämpad datalogi 6.0 ECTS
DH1622 Människa-datorinteraktion. inledande kurs 7.5 ECTS
DM1135 Multimediasystem och signaler 7.5 ECTS
DM1588 Sensorprogrammering för medieteknik 6.0 ECTS
DM1590 Maskininlärning för medieteknik 7.5 ECTS
DT1175 Ljud 7.5 ECTS
SF1919 Sannolikhetsteori och statistik 6.0 ECTS
SK1140 Fotografi för medieteknik 4.0 ECTS
DH2642 Interaktionsprogrammering och dynamiska webben 7.5 ECTS
DM128X Examensarbete inom medieteknik. grundnivå 15.0 ECTS
DM1595 Programutveckling för interaktiva medier 7.5 ECTS
DM2573 Hållbarhet och medieteknik 7.5 ECTS
ME1039 Industriell Ekonomi och Entreprenörskap inom Media och IKT 7.5 ECTS
Total obligatorisk poängsumma:  147.5 ECTS
Exmpelstudent:
Katarina
Andel avklarade:   5.1%
Alla studenter:
Olle  Andel avklarade:  0.0%
Frida Andel avklarade:  9.2%
Sofie Andel avklarade: 55.6%
Linus Andel avklarade: 75.9%
```

Exempelstudenten Katarina är ovan hårdkodad i programmet av testskäl. Ni behöver inte ha med den i ert program.

Givet är filen [```ObligatoriskaMediakurser.csv```], med tre fält: kurskod; kursnamn och poäng:

```
DM1581;Introduktion till medieteknik;6.0
SF1625;Envariabelanalys;7.5
DM1579;Medieproduktion;6.0
...
```

Och filen [```Studieresultat.csv```]

```
Olle;
Frida;DM1581;SF1625
Sofie;DM1581;SF1625;DM1579;DT1175;SF1919;SK1140;DH2642;DM128X;DM1595;DM2573;ME1039
Linus;DM1581;SF1625;SF1626;DD1320;DH1622;DM1135;DM1590;DT1175;SF1919;SK1140;DH2642;DM128X;DM1
595;DM2573;ME1039;DD1380;DD2352
```

Filen innehåller två fält: namn och en semikolon-separerad lista med alla avklarade kurser (alltså inte endast de obligatoriska) för den personen. 

För denna uppgift räknar vi med att namn är unika.

Krav på lösningen:
- Klasser för att modellera kurs, student, mediastudent.
- Samtliga klasser ska skrivas i separata filer och innehålla testkod som testar all funktionalitet i klasserna. Du får själv välja hur du vill göra testerna. Några förslag är assert, unittest och doctest.
- Denna testkod ska INTE köras när ni sen importerar dessa moduler/klasser till programmet som löser uppgiften.
- Ingen kodupprepning.
- Ingen dataduplicering.
- All klass-extern access till attribut sker via metodanrop.
- All data från filerna ska läsas in till programmet och lagras i lämpliga strukturer som är klassbaserade INNAN beräkningar utförs.
- Inga metodanrop med bieffekter (dvs att variabler som inte är parametrar ändras). Beskrivande variabelnamn på alla variabler.