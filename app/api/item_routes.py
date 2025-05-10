from flask import Blueprint, jsonify
from app.models import Item

item_routes = Blueprint('items', __name__)

# Get all items
@item_routes.route('/')
def get_all_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items]), 200

# Get items by Index
@item_routes.route('/<string:index>', methods=['GET'])
def get_item_by_index(index):
    item = Item.query.filter_by(index=index).first()
    if item:
        return jsonify(item.to_dict())
    return jsonify({"error": "Item not found"}), 404

# Get items by inventory_id
@item_routes.route('/inventories/<int:inventory_id>')
def get_items_by_inventory_id(inventory_id):
    items = Item.query.filter_by(inventory_id=inventory_id).all()
    if not items:
        return jsonify({"error": "No items found for this inventory"}), 404
    return jsonify([item.to_dict() for item in items]), 200