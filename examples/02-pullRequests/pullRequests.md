# Pull Requests

Op GitHub kan je PR's openen, zover was je al. Nu gaan we bekijken wat de nuttige commando's zijn voor het oplossen van een merge conflict.\
Als voorbeeldbestand heb ik het script bijgevoegd dat verantwoordelijk is voor het berekenen van een tablet area voor tekentablets gebaseerd op de monitor's beeldverhouding. Hier zitten een aantal prints in, wat het makkelijk maakt om niet al te grote veranderingen te maken aan de echte functionaliteit.

Om je ook te laten zien hoe dit veroorzaakt wordt, laat ik de changes door jou zelf maken.\
Start eerst en vooral met het maken van een nieuwe branch:

```
git checkout -b eerste-branch
```

Op deze branch maak je een change aan een van de prints. Dit kan willekeurig. Deze change add, commit en push je naar je repository op de bijbehorende branch.

Daarna maak je een nieuwe branch vanaf `main`. Dus **NIET** vanaf `eerste-branch`.

Maak nu een change aan **dezelfde lijn** die je net in `eerste-branch` hebt veranderd. _Maar_, niet exact dezelfde change.\
Push deze change nu naar je tweede branch.

Hierna ga je naar GitHub, en open **2 Pull Requests** van je nieuwe branches naar `main`. De eerste merge je gewoon. Hierna ga je terug naar de tweede PR en zie je een merge conflict opduiken. Waarom? Wat doen we in een project ter preventie hiervan?

Los de merge conflict op in je IDE, maar commit nog niets. We gaan nog een paar commando's leren hierbij.

Stel er gaat iets mis tijdens het oplossen van conflicten, dan kun je altijd dit commando uitvoeren:

```
git merge --abort
```

Dit revert alles tot vóór de merge. Het reset dus alles tot het laatste wat je huidige branch kent van al zijn commits.\
Als alles goed gaat, maak je geen commit in de CLI. Je zet je merge verder. Dit dus met:

```
git merge --continue
```

Hierna verschijnt Vim of nano (afhankelijk van je git instellingen) en kun je de merge vervolledigen. Bij Vim verwacht ik nog een aantal vragen te krijgen, dus wees gerust in ze te stellen, ook al hebben ze niets met de git commando's te maken!

Hierna kun je gerust `git push` uitvoeren.
