import arff
import csv
import io
from pathlib import Path

# Déterminer le dossier principal du projet
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Chemins des fichiers
INPUT_FILE = (
    PROJECT_ROOT / "data" / "promise_nfr" / "original" / "nfr.arff"
)

OUTPUT_FILE = (
    PROJECT_ROOT / "data" / "promise_nfr" / "processed" / "requirements.csv"
)

# Vérifier que le fichier original existe
if not INPUT_FILE.exists():
    raise FileNotFoundError(f"Dataset introuvable : {INPUT_FILE}")

# Lire le fichier ARFF sans modifier l'original
content = INPUT_FILE.read_text(encoding="cp1252")
lines = content.splitlines()

# Nettoyer uniquement les commentaires ajoutés
# à la fin des déclarations d'attributs
cleaned_lines = []
in_data = False

for line in lines:
    if line.strip().upper() == "@DATA":
        in_data = True

    if (
        not in_data
        and line.lstrip().upper().startswith("@ATTRIBUTE")
        and "%" in line
    ):
        line = line.split("%", 1)[0].rstrip()

    cleaned_lines.append(line)

# Charger le contenu ARFF nettoyé
dataset = arff.load(io.StringIO("\n".join(cleaned_lines)))

# Récupérer les noms des colonnes
columns = [attribute[0] for attribute in dataset["attributes"]]

# Créer le dossier de sortie si nécessaire
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

# Convertir les données en CSV
with OUTPUT_FILE.open(
    "w",
    newline="",
    encoding="utf-8-sig"
) as file:

    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    for row in dataset["data"]:
        writer.writerow(dict(zip(columns, row)))

# Afficher le résultat
print("\nConversion terminée avec succès !")
print("Fichier créé :", OUTPUT_FILE)
print("Nombre de colonnes :", len(columns))
print("Nombre de lignes :", len(dataset["data"]))
print("Colonnes :", columns)
