# Documentation du dataset PROMISE NFR

## 1. Présentation

Le dataset PROMISE NFR est un ensemble d'exigences logicielles annotées par catégories.

Il est utilisé dans notre projet AI Software Architect Agent pour étudier et expérimenter la classification automatique des exigences non fonctionnelles.

## 2. Organisation des fichiers

```text
promise_nfr/
├── original/
│   └── nfr.arff
├── processed/
│   ├── requirements.csv
│   ├── distribution_classes.csv
│   └── distribution_projets.csv
└── README.md
```

## 3. Description des colonnes

| Colonne | Description |
|---|---|
| ProjectID | Identifiant du projet |
| RequirementText | Texte de l'exigence logicielle |
| class | Catégorie attribuée à l'exigence |

## 4. Prétraitement réalisé

Les opérations réalisées sont :

1. Téléchargement du fichier original au format ARFF.
2. Conversion du fichier ARFF en CSV.
3. Conservation du fichier original.
4. Exploration des données avec Pandas.
5. Analyse des catégories et des valeurs manquantes.
6. Analyse de la répartition des exigences par projet.

## 5. Utilisation dans notre projet

Ce dataset servira de première source de données pour développer et évaluer un module de classification des exigences logicielles.

Ce module pourra notamment identifier les catégories d'exigences non fonctionnelles à partir de leur description textuelle.

Le dataset ne fournit pas directement une correspondance complète entre les exigences et les architectures logicielles. Une base complémentaire de décisions architecturales devra donc être constituée.

## 6. Source

Dépôt GitHub :

https://github.com/AleksandarMitrevski/se-requirements-classification

Fichier original :

0-datasets/tera-PROMISE NFR/nfr.arff

## 7. Licence

La licence indiquée pour cette ressource est CC BY-SA 3.0. Il faut conserver l'attribution à la source et respecter les conditions de partage applicables.

## 8. Limites

- Le dataset porte sur la classification des exigences.
- Il ne couvre pas directement toutes les décisions de conception architecturale.
- Les résultats obtenus devront être évalués avant toute utilisation dans le moteur de recommandation.