
# My name is Jagadeesh Kumar . S
# You may contact me through my mobile number which is +917397285837
# 👀 I’m interested in getting a good job at this moment.
# 🌱 I’m a Full Stack Developer.
# 📫 You may send mail tom my email address which is jagadeesh_2k17@proton.me
# 💬 You may ask me about HTML, JavaScript, React JS, CSS and so on.
# 🧔‍♂️ My age is 27
# 🧔‍♂️ My gender is male
# 🤩 I’m looking to collaborate on Full Stack Development Projects
# 👨‍🏭 Master Of Computer Applications Graduate and Full Stack Developer
# 💻 You may look at my Portfolio on https://portfolios.selvam-instruments.com
# My resume or CV or curriculum vitae is on drive.google.com/file/d/1ks63xad9cDv9Zzio4gz00Pow6qwolE4Z/view?usp=sharing .
   

# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 

from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient
client = MongoClient(os.getenv("MY_KEY"))
db = client.Python

app = Flask(__name__)

## HTML
@app.route('/')
def homework():
    return render_template('index.html')


# My name is Jagadeesh Kumar . S
# You may contact me through my mobile number which is +917397285837
# 👀 I’m interested in getting a good job at this moment.
# 🌱 I’m a Full Stack Developer.
# 📫 You may send mail tom my email address which is jagadeesh_2k17@proton.me
# 💬 You may ask me about HTML, JavaScript, React JS, CSS and so on.
# 🧔‍♂️ My age is 27
# 🧔‍♂️ My gender is male
# 🤩 I’m looking to collaborate on Full Stack Development Projects
# 👨‍🏭 Master Of Computer Applications Graduate and Full Stack Developer
# 💻 You may look at my Portfolio on https://portfolios.selvam-instruments.com
# My resume or CV or curriculum vitae is on drive.google.com/file/d/1ks63xad9cDv9Zzio4gz00Pow6qwolE4Z/view?usp=sharing .
   
# POST API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }

    db.homework.insert_one(doc)

    return jsonify({'result': 'success'})


# Read API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.homework.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)

# My name is Jagadeesh Kumar . S
# You may contact me through my mobile number which is +917397285837
# 👀 I’m interested in getting a good job at this moment.
# 🌱 I’m a Full Stack Developer.
# 📫 You may send mail tom my email address which is jagadeesh_2k17@proton.me
# 💬 You may ask me about HTML, JavaScript, React JS, CSS and so on.
# 🧔‍♂️ My age is 27
# 🧔‍♂️ My gender is male
# 🤩 I’m looking to collaborate on Full Stack Development Projects
# 👨‍🏭 Master Of Computer Applications Graduate and Full Stack Developer
# 💻 You may look at my Portfolio on https://portfolios.selvam-instruments.com
# My resume or CV or curriculum vitae is on drive.google.com/file/d/1ks63xad9cDv9Zzio4gz00Pow6qwolE4Z/view?usp=sharing .
   