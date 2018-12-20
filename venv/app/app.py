from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '4e496f51234e81ea776d73a11a43ecc8 '

posts =[
    {
        'author': 'corey',
        'title' : 'Blog post 1',
        'content' : 'First post',
        'date_posted':'April 20, 2018'
    },

    {
        'author': 'John',
        'title' : 'Blog post 2',
        'content' : 'Second post',
        'date_posted':'october 10, 2018'
    }
]


@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', posts =posts)

    
@app.route('/about')
def about():
    return render_template('about.html', posts =posts, title='About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ =="__main__":
    app.run(debug=True)