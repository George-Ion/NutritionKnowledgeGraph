"""
Script to prepare files for GitHub upload:
1. Creates a README.md describing the project
2. Exports first 1000 entries from each data file
3. Prints git commands to commit and push
"""

import pandas as pd
import os

BASE_PATH = r"c:\Users\georg\Desktop\Master\Period 4\Building and mining knowledge graphs\Assignment 1"

# ============== 1. CREATE README.md ==============
readme_content = """# Food & Nutrition Knowledge Graph - KEN4256 Assignment 1 (Team 12)

## Project Overview
This project builds a **Knowledge Graph** for food, nutrition, recipes, and restaurants using RDF and Linked Data principles. The KG integrates structured data (CSV files), unstructured data (reviews with NLP), and external knowledge from Wikidata.

## What Was Done

### 1. Structured Knowledge Graph
- **Recipes**: Extracted recipe data including name, ingredients, cook time, images, keywords, and categories
- **Nutrition**: Linked nutritional information (calories, protein, sugar, fiber) to recipes
- **Restaurants**: Modeled restaurant data with location, ratings, price range, and cuisine types
- **Schema**: Used [schema.org](https://schema.org) vocabulary with custom namespaces

### 2. Unstructured Knowledge Graph
- Processed **user reviews** using NLP (spaCy)
- Performed **sentiment analysis** using VADER to classify reviews as positive/negative/neutral
- Extracted **ingredient mentions** from review text using phrase matching
- Linked reviews to their corresponding recipes

### 3. Wikidata Integration
- Linked **ingredients** to Wikidata entities using `owl:sameAs`
- Queried Wikidata SPARQL endpoint for **cuisine-country relationships**
- Enriched KG with **dish-cuisine** associations from Wikidata

### 4. SPARQL Queries
Implemented 8 competency questions:
- 4.1: Recipes containing mango
- 4.2: Quick and healthy pies
- 4.3: Chinese restaurants in New Delhi with delivery
- 4.4: Average cost of Asian restaurants in Davenport
- 4.5: Easy desserts under 300 calories (post-2000)
- 4.6: Top beverages by sentiment
- 4.7: High-protein recipes with cuisine info
- 4.8: Top healthy recipes by Nutrition Density Score (NDS)

## Technologies Used
- **Python** (pandas, rdflib, spaCy, VADER)
- **RDF/Turtle** for knowledge representation
- **SPARQL** for querying
- **Wikidata API** for entity linking

## Files
| File | Description |
|------|-------------|
| `Assignment1.ipynb` | Main Jupyter notebook with all code |
| `KEN4256-structured-KG-12.ttl` | Structured KG (recipes, nutrition, restaurants) |
| `KEN4256-unstructured-KG-12.ttl` | Unstructured KG (reviews with sentiment) |
| `KEN4256-integrated-KG-12.ttl` | Merged integrated KG |
| `SPARQL_Results.txt` | Query results for all competency questions |
| `data/` | Sample data files (first 1000 entries) |

## Data Sample
The `data/` folder contains the first 1000 entries from:
- `Nutrition_sample.csv` - Nutritional information
- `Recipes_sample.csv` - Recipe data
- `Restaurants_sample.csv` - Restaurant data
- `Reviews_sample.txt` - User reviews

## How to Run
1. Update `BASE_PATH` in the notebook to your local path
2. Run all cells in `Assignment1.ipynb`
3. Output files will be generated in the same directory

## Authors
Team 12 - KEN4256 Building and Mining Knowledge Graphs
"""

readme_path = os.path.join(BASE_PATH, "README.md")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)
print(f"[OK] Created: {readme_path}")

# ============== 2. EXPORT FIRST 1000 DATA ENTRIES ==============
data_path = os.path.join(BASE_PATH, "data")

# Nutrition - first 1000 rows
try:
    nutrition_df = pd.read_csv(os.path.join(data_path, "Nutrition.csv"), sep=";", encoding="latin1")
    nutrition_sample = nutrition_df.head(1000)
    sample_path = os.path.join(data_path, "Nutrition_sample.csv")
    nutrition_sample.to_csv(sample_path, sep=";", index=False, encoding="utf-8")
    print(f"[OK] Exported {len(nutrition_sample)} nutrition entries to: {sample_path}")
except Exception as e:
    print(f"[ERROR] Nutrition: {e}")

# Recipes - first 1000 rows  
try:
    recipes_df = pd.read_csv(
        os.path.join(data_path, "Recipes.csv"),
        sep=";", encoding="latin1", engine='python',
        quotechar='"', doublequote=True, on_bad_lines='skip'
    )
    recipes_sample = recipes_df.head(1000)
    sample_path = os.path.join(data_path, "Recipes_sample.csv")
    recipes_sample.to_csv(sample_path, sep=";", index=False, encoding="utf-8")
    print(f"[OK] Exported {len(recipes_sample)} recipe entries to: {sample_path}")
except Exception as e:
    print(f"[ERROR] Recipes: {e}")

# Restaurants - first 1000 rows
try:
    restaurants_df = pd.read_csv(os.path.join(data_path, "Restaurants.csv"), sep=";", encoding="latin1")
    restaurants_sample = restaurants_df.head(1000)
    sample_path = os.path.join(data_path, "Restaurants_sample.csv")
    restaurants_sample.to_csv(sample_path, sep=";", index=False, encoding="utf-8")
    print(f"[OK] Exported {len(restaurants_sample)} restaurant entries to: {sample_path}")
except Exception as e:
    print(f"[ERROR] Restaurants: {e}")

# Reviews - first 1000 lines
try:
    reviews_path = os.path.join(data_path, "Reviews.txt")
    sample_path = os.path.join(data_path, "Reviews_sample.txt")
    with open(reviews_path, "r", encoding="utf-8", errors="replace") as f_in:
        lines = []
        for i, line in enumerate(f_in):
            if i >= 1000:
                break
            lines.append(line)
    with open(sample_path, "w", encoding="utf-8") as f_out:
        f_out.writelines(lines)
    print(f"[OK] Exported {len(lines)} review entries to: {sample_path}")
except Exception as e:
    print(f"[ERROR] Reviews: {e}")

# ============== 3. CREATE .gitignore ==============
gitignore_content = """# Ignore large original data files (keep samples)
data/Nutrition.csv
data/Recipes.csv
data/Restaurants.csv
data/Reviews.txt

# Python
__pycache__/
*.py[cod]
.ipynb_checkpoints/

# VS Code
.vscode/

# Environment
.env
venv/
"""

gitignore_path = os.path.join(BASE_PATH, ".gitignore")
with open(gitignore_path, "w", encoding="utf-8") as f:
    f.write(gitignore_content)
print(f"[OK] Created: {gitignore_path}")

# ============== 4. PRINT GIT COMMANDS ==============
print("\n" + "="*60)
print("FILES READY! Now run these git commands:")
print("="*60)
print(f"""
cd "{BASE_PATH}"
git add .
git commit -m "Add KG assignment: notebook, TTL files, sample data, and README"
git push origin main
""")
print("="*60)
