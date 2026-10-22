# Git Lesson

Zeer nodig voor SASM, dus leer met Git Bash werken i.p.v. de knoppen in VSCode / IntelliJ

## Basics

```
git add [files]
git commit [options]
git push [options]
```

In het geval iets misgaat:

```
git restore
git restore --staged
```

<sub>Belangrijk verschil ^^</sub>

## Projecten

In projecten, wanneer je met een groep werkt en merge conflicts hebt in een PR:

```
git merge [branch]
```

Als er iets misgaat tijdens het mergen:

```
git merge --abort
```

Indien compleet:

```
git merge --continue
```

Van branch switchen kan op 2 manieren..
Kan één van jullie mij vertellen wat het verschil is tussen deze 2 commando's?

```
git switch
git checkout
```
