from flask import Flask, render_template, request, redirect
import urllib.parse

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/apply', methods=['POST'])
def apply():
    name = request.form['name']
    number = request.form['number']
    
    message = f"New User:\nName: {name}\nNumber: {number}"
    
    encoded_message = urllib.parse.quote(message)
    
    return redirect(f"https://wa.me/918081852658?text={encoded_message}")
app.run(debug=True)