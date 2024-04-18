# Generate Ecommerce Fashion Data

## Description

use to create type, products in Ecommerce fashion for personal project
Download data from [Fashion product from Kaggle](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset/code)

## Usage

Step 1: Create type.json from styles.csv, run

    py get_type_json.py

Step 2: Create products.json from styles.csv, run

    py get_products_json.py

Step 3: Create .env with .env template, add data to firestore database

    node --env-file=.env add_firestore_db.js




