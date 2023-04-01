from flask import Flask, request, jsonify
import data_product

app = Flask(__name__)

@app.route('/product', methods=['POST'])
def add_product():
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    res = data_product.add_product(name, category, price, instock)
    return jsonify({'message': 'Created successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True) #127.0.0.1