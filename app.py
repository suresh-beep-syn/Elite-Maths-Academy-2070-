
from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Elite Maths Academy 2070</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        body {
            font-family: Arial;
            background: #eef2f7;
            padding: 20px;
        }

        .container {
            max-width: 550px;
            margin: auto;
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 3px 15px #ccc;
        }

        h1 {
            text-align: center;
            color: #173b70;
        }

        label {
            font-weight: bold;
        }

        input, select {
            width: 100%;
            padding: 12px;
            margin: 8px 0 18px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 6px;
        }

        button {
            width: 100%;
            padding: 14px;
            background: #173b70;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 16px;
        }

        .success {
            color: green;
            text-align: center;
        }
    </style>
</head>

<body>
<div class="container">

<h1>ELITE MATHS ACADEMY 2070</h1>
<h3 style="text-align:center">STUDENT ENQUIRY FORM</h3>

{% if submitted %}

    <h2 class="success">Thank You!</h2>
    <p class="success">Your enquiry form has been submitted.</p>

{% else %}

<form method="POST">

    <label>Student Name</label>
    <input type="text" name="student" required>

    <label>Father's Name</label>
    <input type="text" name="father" required>

    <label>Mobile Number</label>
    <input type="tel" name="mobile"
           pattern="[0-9]{10}" maxlength="10" required>

    <label>Class</label>
    <select name="class_name" required>
        <option value="">Select Class</option>
        <option>9th</option>
        <option>10th</option>
        <option>11th</option>
        <option>12th</option>
    </select>

    <label>Subject</label>
    <select name="subject" required>
        <option value="">Select Subject</option>
        <option>Mathematics</option>
        <option>Physics</option>
        <option>Chemistry</option>
        <option>Biology</option>
    </select>

    <label>School Name</label>
    <input type="text" name="school">

    <label>City</label>
    <input type="text" name="city" required>

    <button type="submit">SUBMIT ENQUIRY</button>

</form>

{% endif %}

</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    submitted = False

    if request.method == "POST":
        student = request.form.get("student")
        father = request.form.get("father")
        mobile = request.form.get("mobile")
        class_name = request.form.get("class_name")
        subject = request.form.get("subject")
        school = request.form.get("school")
        city = request.form.get("city")

        print("New enquiry received:", student, father,
              mobile, class_name, subject, school, city)

        submitted = True

    return render_template_string(
        HTML,
        submitted=submitted
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
