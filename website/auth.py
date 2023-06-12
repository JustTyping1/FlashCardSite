from flask import Blueprint, render_template, request

auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return "<p>logout</p>"

@auth.route("sign-up", methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            pass
        elif len(firstName) < 2:
            pass
        elif password1 != password2:
            pass
        elif len(password1) < 8:
            pass
        else:
            #database
            pass
    return render_template("sign-up.html")