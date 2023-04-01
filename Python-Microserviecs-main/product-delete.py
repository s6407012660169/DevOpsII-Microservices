from flask import Flask, request, jsonify
import data_product

app = Flask(__name__)

@app.route('/product/<id>', methods = ['DELETE'])
def delete_product(id):
    product = data_product.get_product(id)
    if not product:
        return jsonify({'error': 'Product does not exist.'}), 404
    else:
        try:
            data_product.delete_product(id)
            return jsonify({"message": "Product deleted successfully"}) ,200
        except Exception as e:
            return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug = True)
