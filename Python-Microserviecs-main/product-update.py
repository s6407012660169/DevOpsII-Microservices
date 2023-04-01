from flask import Flask, request, jsonify
import datetime
import data_product

app = Flask(__name__)


@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    product = data_product.get_product(id)

    if product:
        data_product.update_product(id, name, category, price, instock)
        return jsonify({'message': 'Updated successfully'}), 200
    else:
        return jsonify({'message': 'Product not found'}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug = True)

