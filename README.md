# Food & Nutrition Knowledge Graph - KEN4256 Assignment 1 (Team 12)

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
