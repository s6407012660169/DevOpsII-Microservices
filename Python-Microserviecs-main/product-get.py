from flask import Flask, request, jsonify
import data_product

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def products():
    products = data_product.get_products()
    return jsonify(products)

@app.route('/product/<id>', methods=['GET'])
def product(id):
    product = data_product.get_product(id)
    return jsonify(product)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True) #127.0.0.1