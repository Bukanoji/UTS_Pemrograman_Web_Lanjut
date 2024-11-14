from flask import Blueprint
from controllers.MenuController import get_menus, get_menu, add_menu, update_menu, delete_menu

menu_bp = Blueprint('Menu_bp', __name__)

menu_bp.route('/api/menus', methods=['GET'])(get_menus)

menu_bp.route('/api/menus/<int:menu_id>', methods=['GET'])(get_menu)

menu_bp.route('/api/menus', methods=['POST'])(add_menu)

menu_bp.route('/api/menus/<int:menu_id>', methods=['PUT'])(update_menu)

menu_bp.route('/api/menus/<int:menu_id>', methods=['DELETE'])(delete_menu)