from flask import render_template, request, redirect
from users_app import app
from users_app.models.user import User

@app.route('/')
def root():
    return redirect("/users")

@app.route("/users")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    return render_template("users.html", users=users)

@app.route('/show_user/<int:id>')
def show_user(id):
    data = {
        "id" : id
    }
    return render_template("show_user.html", user = User.get_one(data))

@app.route('/create_user')
def create_user():
    return render_template('create.html')

@app.route('/do_it', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')

@app.route('/edit_user/<int:id>')
def edit_user(id):
    data = {
        'id' : id
    }
    return render_template('edit_user.html', user=User.get_one(data))

@app.route('/user/update', methods=['POST'])
def user_update():
    data = {
        'fname': request.form['first_name'],
        'lname': request.form['last_name'],
        'email': request.form['email'],
        'id': request.form['id']
    }
    return redirect('/users')

@app.route('/delete_user/<int:id>')
def destroy(id):
    data = {
        'id':id
    }
    User.destroy(data)
    return redirect('/users')