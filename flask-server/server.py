from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    
# How to build API on Flask and route it to React app?
# app.route('/api/data', methods=['GET'])
