from flask import jsonify, request
from models.MenuModel import Menu
from models.CategoryModel import Category
from config import db

def get_menus():
    menus = Menu.query.all()
    return jsonify([menu.to_dict() for menu in menus])

def get_menu(menu_id):
    menu = Menu.query.get(menu_id)
    if not menu:
        return jsonify({'error': 'Menu not found'}), 404
    return jsonify(menu.to_dict())

def add_menu():
    new_menu_data = request.get_json()
    new_menu = Menu(
        name=new_menu_data['name'],
        price=new_menu_data['price'],
        category_id=new_menu_data['category_id']
    )
    db.session.add(new_menu)
    db.session.commit()
    return jsonify({"message": "Menu added successfully!", 'menu': new_menu.to_dict()})

def update_menu(menu_id):
    menu = Menu.query.get(menu_id)
    if not menu:
        return jsonify({'error': 'Menu not found'}), 404
    updated_data = request.get_json()
    menu.name = updated_data.get('name', menu.name)
    menu.price = updated_data.get('price', menu.price)
    menu.category_id = updated_data.get('category_id', menu.category_id)
    db.session.commit()
    return jsonify({'message': 'Menu updated successfully!', 'menu': menu.to_dict()})

def delete_menu(menu_id):
    menu = Menu.query.get(menu_id)
    if not menu:
        return jsonify({'error': 'Menu not found'}), 404
    db.session.delete(menu)
    db.session.commit()
    return jsonify({"message": "Menu deleted successfully!"})