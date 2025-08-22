# Simple-Json-Parser

Simple-Json-Parser est un projet Python visant à créer un parseur JSON minimaliste, première étape vers la création d'une base de données maison.

## Objectif

L'objectif principal de ce projet est de comprendre et d'implémenter les bases du parsing JSON, afin de pouvoir ensuite développer une base de données personnalisée sans dépendre de bibliothèques externes.

## Fonctionnalités

- Découpage (lexing) d'une chaîne JSON en tokens (chaînes, nombres, booléens, null, symboles JSON)
- Gestion des espaces, guillemets, et syntaxe JSON de base
- Prise en charge des types :
	- Chaînes de caractères
	- Nombres (int, float)
	- Booléens (`true`, `false`)
	- Null (`null`)
	- Symboles JSON (`{`, `}`, `[`, `]`, `:`, `,`)

## Exemple d'utilisation

```python
from main import JsonParser

parser = JsonParser()
tokens = parser.lex('{"key": [1, 2, 3, true, null]}')
print(tokens)
# Résultat attendu : ['{', 'key', ':', '[', 1, ',', 2, ',', 3, ',', True, ',', True, ']', '}']
```

## Prochaines étapes

- Implémenter le parsing des objets (`parse_object`) et des tableaux (`parse_array`)
- Gérer les erreurs de syntaxe plus finement
- Développer la structure de base de données sur la base de ce parseur
- Optimisation : 
  - Supprimer les copies de chaines
  - Patterns répétitif => Pré-compilation de Regex
  - if/elif => Dictionnaires ?
  - Accès mémoire plus rapide => memoryview/bytes ?
  - Parser récursif
- test de performance

## Pourquoi ce projet ?

J'avais besoin d'un parseur JSON simple pour la suite de mon projet de base de données. Plutôt que d'utiliser une bibliothèque existante, j'ai choisi de tout coder moi-même pour mieux comprendre le fonctionnement interne du parsing et du stockage de données.

## Licence

MIT