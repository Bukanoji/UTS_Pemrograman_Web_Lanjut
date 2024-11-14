from config import app, db
from routes.Menu_bp import menu_bp
from routes.Category_bp import category_bp
from routes.Order_bp import order_bp

app.register_blueprint(menu_bp)
app.register_blueprint(category_bp)
app.register_blueprint(order_bp)

def handler(request):
    return app(request.environ, start_response)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)