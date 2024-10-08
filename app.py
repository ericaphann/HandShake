from flask import Flask, render_template

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/your_portfolio')
def your_portfolio():
    return render_template('your_portfolio.html')

@app.route('/create_profile')
def create_profile():
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)
