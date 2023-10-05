from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017")
db = client.store
collection = db.products

# CREATE operation for a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    # Ensure the provided JSON data matches the expected format
    if 'id' in data and 'title' in data and 'price' in data and 'description' in data and 'category' in data and 'image' in data and 'rating' in data:
        insert_result = collection.insert_one(data)
        return jsonify({"message": "Product created successfully", "id": str(insert_result.inserted_id)}), 201
    else:
        return jsonify({"message": "Invalid product data format"}), 400

# Read operation to get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = list(collection.find())
    for product in products:
        product['_id'] = str(product['_id'])
    return jsonify(products), 200

# Read operation to get a specific product by ID
@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = collection.find_one({'_id': ObjectId(product_id)})
    if product:
        product['_id'] = str(product['_id'])
        return jsonify(product), 200
    else:
        return jsonify({"message": "Product not found"}), 404

# Update operation to modify a product by ID
@app.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    updated_product = collection.update_one(
        {'_id': ObjectId(product_id)},
        {'$set': data}
    )
    if updated_product.modified_count > 0:
        return jsonify({"message": "Product updated successfully"}), 200
    else:
        return jsonify({"message": "Product not found"}), 404

# Delete operation to remove a product by ID
@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    deleted_product = collection.delete_one({'_id': ObjectId(product_id)})

    if deleted_product.deleted_count > 0:
        return jsonify({"message": "Product deleted successfully"}), 200
    else:
        return jsonify({"message": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
