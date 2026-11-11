
from pathlib import Path
import pandas as pd

# 1. Déterminer le dossier principal du projet
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# 2. Définir le chemin du dataset
DATASET_FILE = (
    PROJECT_ROOT
    / "data"
    / "promise_nfr"
    / "processed"
    / "requirements.csv"
)

# 3. Vérifier que le fichier existe
if not DATASET_FILE.exists():
    raise FileNotFoundError(
        f"Dataset introuvable : {DATASET_FILE}"
    )

# 4. Charger le dataset
df = pd.read_csv(DATASET_FILE, encoding="utf-8-sig")

print("\n========== 1. APERÇU DES DONNÉES ==========")
print(df.head(10))

print("\n========== 2. DIMENSIONS ==========")
print("Nombre de lignes :", df.shape[0])
print("Nombre de colonnes :", df.shape[1])

print("\n========== 3. INFORMATIONS GÉNÉRALES ==========")
df.info()

print("\n========== 4. VALEURS MANQUANTES ==========")
print(df.isnull().sum())

print("\n========== 5. RÉPARTITION DES CLASSES ==========")
class_counts = df["class"].value_counts(dropna=False)
print(class_counts)

print("\n========== 6. NOMBRE DE PROJETS ==========")
print("Nombre de projets :", df["ProjectID"].nunique())

print("\n========== 7. RÉPARTITION PAR PROJET ==========")
print(df["ProjectID"].value_counts().sort_index())

print("\n========== 8. DOUBLONS ==========")
print("Nombre de lignes dupliquées :", df.duplicated().sum())

print("\n========== 9. EXEMPLES D'EXIGENCES ==========")
for _, row in df.head(5).iterrows():
    print("\nProjet :", row["ProjectID"])
    print("Exigence :", row["RequirementText"])
    print("Classe :", row["class"])

# 10. Sauvegarder les statistiques
OUTPUT_DIR = DATASET_FILE.parent

class_counts.rename_axis("class").reset_index(
    name="nombre"
).to_csv(
    OUTPUT_DIR / "distribution_classes.csv",
    index=False,
    encoding="utf-8-sig"
)

df["ProjectID"].value_counts().sort_index().rename_axis(
    "ProjectID"
).reset_index(
    name="nombre_exigences"
).to_csv(
    OUTPUT_DIR / "distribution_projets.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\n========== TERMINÉ ==========")
print("Les statistiques ont été enregistrées dans :", OUTPUT_DIR)


print("\n========== 10. ANALYSE DES DOUBLONS ==========")

duplicates = df[df.duplicated(keep=False)]

if duplicates.empty:
    print("Aucun doublon trouvé.")
else:
    print("Lignes concernées :")
    print(duplicates.to_string(index=False))

    print("\nNombre de doublons exacts :",
          df.duplicated().sum())

    print("\nExigences identiques dans plusieurs projets :")
    repeated_texts = df[
        df.duplicated(
            subset=["RequirementText"],
            keep=False
        )
    ].sort_values("RequirementText")

    print(repeated_texts.to_string(index=False))
