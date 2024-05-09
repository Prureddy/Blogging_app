from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    fav_pizza = ['Pepparoni','chese n corn', 'Pepper','Non veg Pizza']
    stuff = "<p>This is <strong>Bold</strong> text<p>"
    return render_template("index.html" ,stuff = stuff, fav_pizza = fav_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name1 = name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500     

if __name__ == "__main__":
    app.run(debug=True)