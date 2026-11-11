### Constitution du jeu de données

La première phase du projet consiste à identifier et à préparer les données nécessaires au développement et à l'évaluation de l'agent intelligent.

Le dataset PROMISE NFR a été retenu comme première source de données pour la classification des exigences logicielles.

Il contient des descriptions d'exigences associées à des catégories permettant de distinguer les exigences fonctionnelles et différentes catégories d'exigences non fonctionnelles.

**Utilisations prévues :**
- Classification des exigences fonctionnelles et non fonctionnelles.
- Expérimentation du module de traitement des exigences.
- Évaluation de la qualité de classification.
- Constitution d'un premier jeu de données de référence.

**Limite identifiée :** ce dataset ne contient pas directement les correspondances complètes entre cahiers des charges et architectures logicielles. Une base complémentaire de connaissances architecturales sera donc constituée à partir de décisions architecturales documentées et d'exemples de projets.

**Organisation :**
- `data/promise_nfr/original/` : données originales.
- `data/promise_nfr/processed/` : données préparées pour l'application.
- `data/promise_nfr/README.md` : provenance et licence.