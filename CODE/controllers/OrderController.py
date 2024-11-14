from flask import jsonify, request
from models.OrderModel import Order
from models.MenuModel import Menu
from config import db

def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])

def get_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    return jsonify(order.to_dict())

def add_order():
    new_order_data = request.get_json()
    new_order = Order(
        menu_id=new_order_data['menu_id'],
        quantity=new_order_data['quantity']
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order added successfully!", 'order': new_order.to_dict()})

def update_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    updated_data = request.get_json()
    order.menu_id = updated_data.get('menu_id', order.menu_id)
    order.quantity = updated_data.get('quantity', order.quantity)
    db.session.commit()
    return jsonify({'message': 'Order updated successfully!', 'order': order.to_dict()})

def delete_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order deleted successfully!"})