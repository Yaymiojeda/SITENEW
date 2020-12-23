from flask import Flask, render_template

app = Flask(__name__)

#add pages here
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

@app.route('/community')
def community():
    return render_template('community.html')

if __name__ == '__main__':
    app.run(debug=True)