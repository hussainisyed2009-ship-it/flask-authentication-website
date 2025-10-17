from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=False)

@auth.route('/logout')
def logout():
    return "<p>Logout<p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        FirstName = request.form.get('FirstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email is invalid, make sure to use full school email', category='error')
        elif len(FirstName) < 2:
            flash('First name is invalid, first name should be longer than 2 charecters', category='error')
        elif password1 != password2:
            flash('Passwords do not match, please try again', category='error')
        elif len(password1) < 5:
            flash('Password is too short, it should be over 5 charecters long', category='error')
        else:
            flash('Account created!', category='success')

    return render_template("sign_up.html")