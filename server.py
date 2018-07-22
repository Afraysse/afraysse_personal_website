from flask import Flask, render_template, flash, redirect, request, jsonify, url_for, session
from flask_debugtoolbar import DebugToolbarExtension

# from model import connect_to_db

app = Flask(__name__)
app.secret_key = "CBA"

@app.route('/')
def hello_world():

    # current_sesh = session.get('user_id', None)
    return render_template('homepage.html')

@app.route('/projects')
def projects():

    # eventually this will query for all projects and return + display
    return render_template('projects.html')

@app.route('/me')
def me():

    return render_template('me.html')

@app.route('/blog')
def blog():

    # eventually this will query for all blog posts and display
    return render_template('blog.html')


# @app.route('/login', methods=['POST'])
# def login():
#
#     email = request.form.get('email')
#     password = request.form.get('password')
#
#     user = User.query.filter_by(email=email).first()
#     print user
#
#     if not user:
#         flash("User not found. Please register.")
#         return redirect('/')
#
#     if user.password != password:
#         flash("Incorrect password! Please try again.")
#         return redirect('/login')
#
#     session["user_id"] = user.user_id
#
#     return redirect('/homepage')
#
# @app.register('/register', methods=['POST'])
# def register():
#
#     username = request.form.get('username')
#     email = request.form.get('email')
#     firstName = request.form.get('firstName')
#     lastName = request.form.get('lastName')
#     age = request.form.get('age')
#     location = request.form.get('location')
#     password = request.form.get('password')
#
#     new_user = User(username=username, email=email, firstName=firstName, lastName,
#                 age=age, location=location, password=password)
#
#     db.session.add(new_user)
#     db.session.commit()
#
#     flash("Welcome {}!".format(username))
#     return redirect('/')
#
# @app.route('/homepage', methods=['GET'])
# def homepage():
#
#     current_session = session.get('user_id', None)
#     return render_template('homepage.html')
#
# @app.route('/logout')
# def logout():
#
#     del session["user_id"]
#     flash("You have now logged out!")
#     return redirect('/')

############################################

if __name__ == "__main__":
    app.debug = True
    # connect_to_db(app)
    DebugToolbarExtension(app)
    app.run()
