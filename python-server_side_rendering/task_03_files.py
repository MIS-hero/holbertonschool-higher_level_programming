from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Helper functions
def read_json(file_path='products.json'):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data
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

# Route for product display
@app.route('/products')
def products():
    source = request.args.get('source', '').lower()   # json or csv
    prod_id = request.args.get('id', type=int)
    error = None
    products_list = []

    # Select source
    if source == 'json':
        products_list = read_json()
    elif source == 'csv':
        products_list = read_csv()
    else:
        error = "Wrong source"

    # Filter by ID if given
    if prod_id is not None and not error:
        products_list = [p for p in products_list if p['id'] == prod_id]
        if not products_list:
            error = "Product not found"

    return render_template('product_display.html', products=products_list, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)