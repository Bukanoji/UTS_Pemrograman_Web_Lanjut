from flask import Blueprint
from controllers.CategoryController import get_categories, get_category, add_category, update_category, delete_category

category_bp = Blueprint('Category_bp', __name__)

category_bp.route('/api/categories', methods=['GET'])(get_categories)

category_bp.route('/api/categories/<int:id>', methods=['GET'])(get_category)

category_bp.route('/api/categories', methods=['POST'])(add_category)

category_bp.route('/api/categories/<int:id>', methods=['PUT'])(update_category)

category_bp.route('/api/categories/<int:id>', methods=['DELETE'])(delete_category)