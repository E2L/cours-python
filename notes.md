Ce fichier contient diverses notes utiles à la préparation des futurs cours.

# Sujets à évoquer

## next chapter

* Let's create *explicit* hidden interfaces!

## bits

* base class / derived class -> more vocabulary
* attributes on functions (you never know)
* `__call__`, functors
* scopes, closures, global, nonlocal
* private
* no overlaod in python
   * several `__init__` ? Nope, alternative constructors
   * https://code-maven.com/slides/python-programming/class-methods-alternative-constructor
* properties on classes
* stable sorts
* dict: setdefault
* listes: pop prend un argument
* slices takes a step too [::-1] -> reverse
* with: contextmanager, ContextDecorator
* short circuit in if: `if a is not None and a.b == 42`

## big stuff

* exceptions: try, catch, finally
* files: "wa", accès séquentiel (chunk = file.read(chunk_size))
* style: trailing white space, editor configuration,
* [formatage de strings](fragments/format.md)
* liste par compréhension et filtres
* `help()`
* packages, libraries tierces
* requests, HTTP protocol (headers, methodes, urls, anchors, links ...)

* décorateurs

* regular expressions

* Données binaires, encodage (binaire, ASCII, hexadécimal, unicode ...)

* virtualenv, pip, et bibliothèques tierces

* IDEs: don't use them ... yet (or ever)
    * linters,
    * déboguage
    * demo: pyflakes - black

* tests: pytest, TDD


# Idées d'ateliers

Parser du RSS et télécharger les émissions:

  * Source: https://github.com/dmerejkowsky/pypodget/
  * Concepts:
     * `setup.py`
     * scripts, entry points

* Remplacer Matlab par Python + numpy + matplotlib
* Effets audio
* Jeux vidéos (pygame)
* IOT : micro-controller, Rasberry Pi
* Blender/GIMP
* Stéganographie: cacher un texte dans une image

* Patcher des binaires Windows pour le fun?
