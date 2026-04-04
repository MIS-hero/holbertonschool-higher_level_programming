from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# --- Helper functions ---
def read_json(file_path='products.json'):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

def read_csv(file_path='products.csv'):
    products = []
    try:
        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return products

def read_sqlite(db_path='products.db'):
    products = []
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # access columns by name
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
    except Exception as e:
        print(f"Error reading SQLite: {e}")
    return products

# --- Flask Route ---
@app.route('/products')
def products():
    source = request.args.get('source', '').lower()   # json, csv, sql
    prod_id = request.args.get('id', type=int)
    error = None
    products_list = []

    # Select data source
    if source == 'json':
        products_list = read_json()
    elif source == 'csv':
        products_list = read_csv()
    elif source == 'sql':
        products_list = read_sqlite()
    else:
        error = "Wrong source"

    # Filter by ID if provided
    if prod_id is not None and not error:
        products_list = [p for p in products_list if p['id'] == prod_id]
        if not products_list:
            error = "Product not found"

    return render_template('product_display.html', products=products_list, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)