---

[Sparta Coding Club] BE Week 2, TIL and Solution to Homework of BE week two
The Objectives of BE Week two were followings.
Manage mongoDB using pymongo
Create an API for Spartapedia and complete the project!

---

The things that were taught in BE week two were followings.
What is CRUD?
Create, Read, Update, and Delete (CRUD) are the four basic functions that models should be able to do, at most.
Create : ex) user can create a post
Read : ex) user can read the post
Update : ex) user can edit the post
Delete : ex) user can delete the post

What is an API?
API(Application Programming Interface)

APIs are mechanisms that enable two software components to communicate with each other using a set of definitions and protocols.

---

Solution to Homework of BE week two
Create a Flask project using shopping mall feature API.
Here, one-page shopping mall page does two things :
Make an order(POST): after clicking the 'order button', the information should be added in the list.
2) See the order list(GET): after page loading, the order list is updated.

app.py

# My name is Jagadeesh Kumar . S
# You may contact me through my mobile number which is +917397285837
# 👀 I'm interested in getting a good job at this moment.
# 🌱 I'm a Full Stack Developer.
# 📫 You may send mail tom my email address which is jagadeesh_2k17@proton.me
# 💬 You may ask me about HTML, JavaScript, React JS, CSS and so on.
# 🧔‍♂️ My age is 27
# 🧔‍♂️ My gender is male
# 🤩 I'm looking to collaborate on Full Stack Development Projects
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
# 👀 I'm interested in getting a good job at this moment.
# 🌱 I'm a Full Stack Developer.
# 📫 You may send mail tom my email address which is jagadeesh_2k17@proton.me
# 💬 You may ask me about HTML, JavaScript, React JS, CSS and so on.
# 🧔‍♂️ My age is 27
# 🧔‍♂️ My gender is male
# 🤩 I'm looking to collaborate on Full Stack Development Projects
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
# 👀 I'm interested in getting a good job at this moment.
# 🌱 I'm a Full Stack Developer.
# 📫 You may send mail tom my email address which is jagadeesh_2k17@proton.me
# 💬 You may ask me about HTML, JavaScript, React JS, CSS and so on.
# 🧔‍♂️ My age is 27
# 🧔‍♂️ My gender is male
# 🤩 I'm looking to collaborate on Full Stack Development Projects
# 👨‍🏭 Master Of Computer Applications Graduate and Full Stack Developer
# 💻 You may look at my Portfolio on https://portfolios.selvam-instruments.com
# My resume or CV or curriculum vitae is on drive.google.com/file/d/1ks63xad9cDv9Zzio4gz00Pow6qwolE4Z/view?usp=sharing .
templates/index.html
<!DOCTYPE html>

<!-- My name is Jagadeesh Kumar . S
You may contact me through my mobile number which is +917397285837
👀 I'm interested in getting a good job at this moment.
🌱 I'm a Full Stack Developer.
📫 You may send mail tom my email address which is jagadeesh_2k17@proton.me
💬 You may ask me about HTML, JavaScript, React JS, CSS and so on.
🧔‍♂️ My age is 27
🧔‍♂️ My gender is male
🤩 I'm looking to collaborate on Full Stack Development Projects
👨‍🏭 Master Of Computer Applications Graduate and Full Stack Developer
💻 You may look at my Portfolio on https://portfolios.selvam-instruments.com
My resume or CV or curriculum vitae is on drive.google.com/file/d/1ks63xad9cDv9Zzio4gz00Pow6qwolE4Z/view?usp=sharing .
    -->
<html lang="ko">

<head>
    <!-- Webpage Title -->
    <title>One-page shopping mall</title>

    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <!-- JS -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>

    <!-- Google Font -->
    <link href="https://fonts.googleapis.com/css?family=Stylish&display=swap" rel="stylesheet">

    <script type="text/javascript">

        function order() {
            let name = $("#order-name").val();
            let count = $("#order-count").val();
            let address = $("#order-address").val();
            let phone = $("#order-phone").val();

            if (name == "") {
                alert("Please fill out name")
                $("#order-name").focus()
                return
            } else if (count == "") {
                alert("Please fill out quantity")
                $("#order-count").focus()
                return
            } else if (address == "") {
                alert("Please fill out address")
                $("#order-address").focus()
                return
            } else if (phone == "") {
                alert("Please fill out phone number")
                $("#order-phone").focus()
                return
            } else {
                alert('Order completed!')
                // return
            }
            let doc = {
                'name_give': name,
                'count_give': count,
                'address_give': address,
                'phone_give': phone
            };
            console.log(doc)
            // Use POST API here
            $.ajax({
                type: 'POST',
                url: '/order',
                data: doc,
                success: function (response) {
                    console.log(response)
                }
            })
            $(document).ready(function () {
                $("#orders-box").html("");
                showOrders();
            });
        }

        $(document).ready(function () {
            $("#orders-box").html("");
            showOrders();
        });

        function showOrders() {
            // Use READ API here
            $.ajax({
                type: 'GET',
                url: '/order',
                data: {},
                success: function (response) {
                    let orders = response['orders']
                    console.log(response['orders']);
                    for (let i = 0; i < orders.length; i++) {
                        let order = orders[i];
                        let name = order['name'];
                        let count = order['count'];
                        let address = order['address'];
                        let phone = order['phone'];
                        makeOrderRow(name, count, address, phone);
                    }
                }

            })

        }

        function makeOrderRow(name, count, address, phone) {
            let tempHtml = `<tr>\
                                <td>${name}</td>
                                <td>${count}</td>
                                <td>${address}</td>
                                <td>${phone}</td>
                              </tr>`;

            $("#orders-box").append(tempHtml);
        }
    </script>

    <style type="text/css">
        * {
            font-family: "Stylish", sans-serif;
        }

        h1,
        h5 {
            display: inline;
        }

        .wrap {
            width: 500px;
            margin: auto;
        }

        .img {
            background-image: url("https://thecandlepackaging.com/wp-content/uploads/2022/08/white-candle-packaging.jpg");
            background-size: cover;
            background-position: center;
            width: 500px;
            height: 300px;
        }

        .info {
            margin-top: 20px;
            margin-bottom: 20px;
        }

        .order {
            text-align: center;
        }

        .orders {
            margin-top: 100px;
        }
    </style>
</head>

<body>
    <div class="wrap">
        <div class="img"></div>
        <div class="info">
            <h1>Sparta Candles</h1>
            <h5>Price: $3 each</h5>
            <p>These candles actually have special power!</p>
            <div class="input-group mb-3">
                <div class="input-group-prepend">
                    <span class="input-group-text">Your name</span>
                </div>
                <input type="text" class="form-control" id="order-name">
            </div>

            <!-- My name is Jagadeesh Kumar . S
You may contact me through my mobile number which is +917397285837
👀 I'm interested in getting a good job at this moment.
🌱 I'm a Full Stack Developer.
📫 You may send mail tom my email address which is jagadeesh_2k17@proton.me
💬 You may ask me about HTML, JavaScript, React JS, CSS and so on.
🧔‍♂️ My age is 27
🧔‍♂️ My gender is male
🤩 I'm looking to collaborate on Full Stack Development Projects
👨‍🏭 Master Of Computer Applications Graduate and Full Stack Developer
💻 You may look at my Portfolio on https://portfolios.selvam-instruments.com
My resume or CV or curriculum vitae is on drive.google.com/file/d/1ks63xad9cDv9Zzio4gz00Pow6qwolE4Z/view?usp=sharing . -->

            <div class="input-group mb-3">
                <div class="input-group-prepend">
                    <label class="input-group-text" for="order-count">Quantity</label>
                </div>
                <select class="custom-select" id="order-count">
                    <option selected value=""> -- Please select quantity --</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                </select>
            </div>
            <div class="input-group mb-3">
                <div class="input-group-prepend">
                    <span class="input-group-text">Address</span>
                </div>
                <input type="text" class="form-control" id="order-address">
            </div>
            <div class="input-group mb-3">
                <div class="input-group-prepend">
                    <span class="input-group-text">Phone number</span>
                </div>
                <input type="text" class="form-control" id="order-phone">
            </div>
            <div class="order">
                <button onclick="order()" type="button" class="btn btn-primary">Order</button>
            </div>
        </div>
        <div class="orders">
            <table class="table">
                <thead>
                    <tr>
                        <th scope="col">Name</th>
                        <th scope="col">Quantity</th>
                        <th scope="col">Address</th>
                        <th scope="col">Phone number</th>
                    </tr>
                </thead>
                <tbody id="orders-box">
                    <tr>
                        <td>Victoria</td>
                        <td>3</td>
                        <td>Seoul, Korea</td>
                        <td>010-1234-5678</td>
                    </tr>

                </tbody>
            </table>
        </div>
    </div>
</body>
<!-- 
My name is Jagadeesh Kumar . S
You may contact me through my mobile number which is +917397285837
👀 I'm interested in getting a good job at this moment.
🌱 I'm a Full Stack Developer.
📫 You may send mail tom my email address which is jagadeesh_2k17@proton.me
💬 You may ask me about HTML, JavaScript, React JS, CSS and so on.
🧔‍♂️ My age is 27
🧔‍♂️ My gender is male
🤩 I'm looking to collaborate on Full Stack Development Projects
👨‍🏭 Master Of Computer Applications Graduate and Full Stack Developer
💻 You may look at my Portfolio on https://portfolios.selvam-instruments.com
My resume or CV or curriculum vitae is on drive.google.com/file/d/1ks63xad9cDv9Zzio4gz00Pow6qwolE4Z/view?usp=sharing .
    -->

</html>

---

Screenshots of results

---

Github
Github link is on https://github.com/Jagadeesh-Kumar-With-Initial-As-S/Week-2-BE-HW.

---

Deploy
The solution to homework of BE Week two is deployed on https://week-2-be-hw.vercel.app/.

---

Conclusion
This week I learned to code in Python using Flask framework and so on.
I completed the Homework of BE week two.
I hope that Solution to Homework of BE week two will help the viewers.
