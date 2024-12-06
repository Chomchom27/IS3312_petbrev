from flask import Flask, request, redirect, url_for, session, render_template
from dao.productdao import ProductDAO
from dao.userdao import UserDAO

app = Flask(__name__)
app.secret_key = 'notagreatsecretkey'

@app.route('/')
def home():
    proddao = ProductDAO()
    products = proddao.getAllProducts()
    return render_template('index.html', products=products)

@app.route('/index')
def index():
    proddao = ProductDAO()
    products = proddao.getAllProducts()
    return render_template('index.html', products=products)

@app.route('/admin')
def admin():
    return render_template('adminhome.html')

@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
def product(product_id):
    proddao = ProductDAO()
    product = proddao.getProduct(product_id=product_id)

    if request.method == 'POST':
        if 'username' not in session:
            return redirect(url_for('login'))

        # Add to cart logic
        if 'cart' not in session:
            session['cart'] = []

        session['cart'].append({'id': product_id, 'name': product.name, 'price': product.price, 'type': product.spider_type, 'sex' : product.sex, 'image:': product.imageUrl, 'quantity': int(request.form['quantity'])})
        session.modified = True

    return render_template('product.html', product=product, cart_count=len(session.get('cart', [])))

@app.route('/basket')
def basket():
    if 'cart' not in session:
        session['cart'] = []
    return render_template('basket.html', cart=session['cart'], cart_count=len(session.get('cart', [])))

@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    """
    Removes an item from the cart by product_id.
    """
    if 'cart' in session:
        session['cart'] = [item for item in session['cart'] if item['id'] != product_id]
        session.modified = True
    return redirect(url_for('basket'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        userdao = UserDAO()
        user = userdao.getuserbyusername(username=username)
        if user is None:
            return redirect(url_for('index'))

        if user.password != password:
            return redirect(url_for('index'))
        elif user.user_type == 'administrator':
            session['username'] = user.username
            return redirect(url_for('admin'))
        elif user.user_type == 'customer':
            session['username'] = user.username
            return redirect(url_for('index'))
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    if 'cart' in session:
        session.pop('cart')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
