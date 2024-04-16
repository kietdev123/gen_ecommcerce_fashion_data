# Generate Ecommerce Fashion Data

## Description

use to create type, products in Ecommerce fashion for personal project

## Usage

Step 1: Download data from [Fashion product from Kaggle](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset/code)

Step 2: Create data foulder with images - foulder and styles.csv

Step 3: Create type.json from styles.csv, run

    py get_type_json.py

Step 4: Create products.json from styles.csv, run

    py get_products_json.py

Step 5: Create .env with .env template, get product_images.json when upload images to cloudinary, run

    node --env-file=.env upload_images.js




