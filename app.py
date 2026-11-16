
from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

HOME_HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Elite Maths Academy 2070</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
    font-family: Arial;
    margin: 0;
    background: #eef2f7;
    color: #222;
}
header {
    background: #173b70;
    color: white;
    padding: 25px 15px;
    text-align: center;
}
nav {
    background: white;
    padding: 15px;
    text-align: center;
}
nav a {
    color: #173b70;
    text-decoration: none;
    margin: 10px;
    font-weight: bold;
}
.hero {
    text-align: center;
    padding: 65px 15px;
    background: white;
}
.hero h2 {
    color: #173b70;
    font-size: 30px;
}
.hero p {
    font-size: 18px;
    line-height: 1.6;
}
.btn {
    display: inline-block;
    background: #173b70;
    color: white;
    padding: 15px 28px;
    text-decoration: none;
    border-radius: 7px;
    margin-top: 20px;
}
.section {
    text-align: center;
    padding: 35px 15px;
}
.cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 15px;
}
.card {
    background: white;
    padding: 22px;
    border-radius: 10px;
    width: 220px;
    box-shadow: 0 2px 8px #ccc;
}
footer {
    background: #173b70;
    color: white;
    text-align: center;
    padding: 20px;
}
</style>
</head>

<body>

<header>
<h1>ELITE MATHS ACADEMY 2070</h1>
<p>Learn Today, Lead Tomorrow</p>
</header>

<nav>
<a href="/">Home</a>
<a href="#about">About</a>
<a href="#courses">Courses</a>
<a href="#contact">Contact</a>
</nav>

<div class="hero">
<h2>Welcome to Elite Maths Academy</h2>
<p>
Build Your Knowledge, Improve Your Skills
and Achieve Your Goals.
</p>
<p>Quality Education for Classes 9th to 12th</p>

<a class="btn" href="/enquiry">
STUDENT ENQUIRY
</a>
</div>

<div class="section" id="about">
<h2>About Our Academy</h2>
<p>
Welcome to Elite Maths Academy 2070.
We focus on quality education and student success.
</p>
</div>

<div class="section" id="courses">
<h2>Our Courses</h2>

<div class="cards">
<div class="card">
<h3>Class 9th</h3>
<p>Mathematics and Science</p>
</div>

<div class="card">
<h3>Class 10th</h3>
<p>Mathematics and Science</p>
</div>

<div class="card">
<h3>Class 11th</h3>
<p>Mathematics, Physics, Chemistry</p>
</div>

<div class="card">
<h3>Class 12th</h3>
<p>Mathematics, Physics, Chemistry</p>
</div>
</div>
</div>

<div class="section" id="contact">
<h2>Contact Us</h2>
<p>For admission enquiries, please fill out our form.</p>
<a class="btn" href="/enquiry">Enquire Now</a>
</div>

<footer>
<p>© 2026 Elite Maths Academy 2070</p>
<p>All Rights Reserved</p>
</footer>

</body>
</html>
"""

FORM_HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Student Enquiry - Elite Maths Academy</title>
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
    cursor: pointer;
}
.home {
    display: block;
    text-align: center;
    margin-top: 20px;
    color: #173b70;
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
<a class="home" href="/">Back to Home Page</a>

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

<a class="home" href="/">Back to Home Page</a>

{% endif %}
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HOME_HTML)


@app.route("/enquiry", methods=["GET", "POST"])
def enquiry():

    submitted = False

    if request.method == "POST":
        student = request.form.get("student")
        father = request.form.get("father")
        mobile = request.form.get("mobile")
        class_name = request.form.get("class_name")
        subject = request.form.get("subject")
        school = request.form.get("school")
        city = request.form.get("city")

        print("New enquiry received:",
              student, father, mobile,
              class_name, subject, school, city)

        submitted = True

    return render_template_string(
        FORM_HTML,
        submitted=submitted
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
