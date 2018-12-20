from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ =="__main__":
    app.run(debug=True)