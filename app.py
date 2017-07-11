from flask import Flask, render_template, session

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/register')
def showSignup():
    return render_template('signup.html')

@app.route('/login')
def showSignin():
    return render_template('signin.html')

@app.route('/addWish')
def showAddWish():
    return render_template('addWish.html')

@app.route('/home')
def userHome():
   return render_template('userHome.html')
    
if __name__ == "__main__":
    app.run(debug=True)
