#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici
    nouveau_mot = ""
    for lettre in mot:
        nouveau_mot += chr(ord(lettre) - 32)

    return nouveau_mot

if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
