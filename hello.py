from flask import Flask, render_template

#create a flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')
#def index():
#   return "<h1>Hello DUNIA!</h1>"

def index():
    firstname = "Marya"
    bold = "This is <strong>bold</strong> text"
    striptag = "This is <strong>bold</strong> text with striptags"
    
    fav_pizza =["Pepperoni", "Cheese", "Mashroom", 30]
    
    return render_template("index.html",
        first_name = firstname,
        stuff = bold,
        stuffs = striptag,
        favorite_pizza = fav_pizza)


@app.route('/users')
def users():
    return "<h1>Hello USER</h1>"

@app.route('/user/<nama>')
def user(nama):
    return render_template("user.html", username=nama)

@app.route('/umur/<umur>')
def umur(umur):
    return "<h1>Your Age is {} years old</h1>".format(umur)


#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500

app.run(debug=True)