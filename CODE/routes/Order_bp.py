from flask import Blueprint
from controllers.OrderController import get_orders, get_order, add_order, update_order, delete_order

order_bp = Blueprint('Order_bp', __name__)

order_bp.route('/api/orders', methods=['GET'])(get_orders)

order_bp.route('/api/orders/<int:order_id>', methods=['GET'])(get_order)

order_bp.route('/api/orders', methods=['POST'])(add_order)

order_bp.route('/api/orders/<int:order_id>', methods=['PUT'])(update_order)

order_bp.route('/api/orders/<int:order_id>', methods=['DELETE'])(delete_order)