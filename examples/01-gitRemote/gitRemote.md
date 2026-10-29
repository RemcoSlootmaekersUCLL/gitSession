# Git Remote

`git remote` is een command waarmee je je remote kan bekijken, aanpassen,...

We kijken naar 3 opties:

```
git remote -v (--verbose)
git remote add [options]
git remote remove [options]
```

`git remote -v` laat je huidige remote zien.\
Nu is dat voor de huidige repository dus:

```
$ git remote -v
origin  https://github.com/RemcoSlootmaekersUCLL/gitSession.git (fetch)
origin  https://github.com/RemcoSlootmaekersUCLL/gitSession.git (push)
```

Nu gaan we de remote veranderen naar je eigen repository. Je maakt dus een nieuwe repository aan op [GitHub](https://github.com/new) en laat hem volledig leeg. Je kan hierna al een beetje zien welke commando's je gaat moeten uitvoeren, maar laten we het stap voor stap doen.

Ten eerste haal je de oude remote weg, zodat je je eigen remote in de plaats kan zetten.

```
git remote remove origin
```

<sub>Je kan na elke stap nakijken met `git remote -v`</sub>

Hierna voegen we je nieuwe GitHub repository toe als origin. Probeer deze zelf eens uit te vinden.

<details>
<summary>Open dit als je het niet vind of wilt bevestigen</summary>

`git remote add origin <git-url>`

</details>

Daarna push je naar je eigen repository.
