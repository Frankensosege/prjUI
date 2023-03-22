from flask import Blueprint, render_template, request, redirect, url_for
from FlaskTest.models import Users
from FlaskTest import db
import datetime

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        usr_id = request.form['id']
        pw = request.form['pw']

        # query the database for the user with the given username and password
        user = Users.query.filter_by(id=usr_id, passwd=pw).first()
        name = user.user_name

        if user is not None:
            # redirect the user to the home page
            return redirect(url_for('main.home'), name=name)
        else:
            # display an error message
            error = 'Invalid credentials. Please try again.'

    # render the login page
    return render_template('login.html', error=error)

@bp.route('/register.html', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        usr_id = request.form['regi_id']
        pw = request.form['regi_pw']

        answer = Users(id=usr_id, passwd=pw, create_date=datetime.now(), lastupdate_date=datetime.now())
        Users.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('main.home', question_id=question_id))

@bp.route('/home.html/<name>', methods=['GET', 'POST'])
def home(name):
    print('sdddddddddddddddddddddddddddddddddddddddddddddd')
    error = None
    return render_template('home.html', name=name)
