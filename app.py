
from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# =================================
# ALL COURSES / PROGRAMMES
# =================================

COURSES = [
    ("Class 9th", "Mathematics and Science"),
    ("Class 10th", "Mathematics and Science"),
    ("Class 11th", "Mathematics, Physics, Chemistry, Biology"),
    ("Class 12th", "Mathematics, Physics, Chemistry, Biology"),
    ("JEE Preparation", "Engineering Entrance Preparation"),
    ("NEET Preparation", "Medical Entrance Preparation"),
    ("Foundation Course", "Build Strong Academic Concepts"),
    ("CUET Preparation", "Common University Entrance Preparation"),
    ("SSC CGL", "Staff Selection Commission - Combined Graduate Level"),
    ("SSC CHSL", "Staff Selection Commission - Combined Higher Secondary Level"),
    ("UPSC CSAT", "Civil Services Aptitude Test Preparation"),
    ("Other Courses", "Contact Us for More Details")
]


# =================================
# HOME PAGE HTML
# =================================

HOME_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Elite Maths Academy 2070</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

<style>
* {
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    margin: 0;
    background: #eef2f7;
    color: #222;
}

header {
    background: #173b70;
    color: white;
    padding: 30px 15px;
    text-align: center;
}

header h1 {
    margin: 0;
    font-size: 30px;
}

header p {
    font-size: 17px;
}

nav {
    background: white;
    padding: 18px;
    text-align: center;
    box-shadow: 0 2px 6px #ddd;
}

nav a {
    color: #173b70;
    text-decoration: none;
    margin: 10px;
    font-weight: bold;
}

.hero {
    background: white;
    text-align: center;
    padding: 65px 20px;
}

.hero h2 {
    color: #173b70;
    font-size: 32px;
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
    margin-top: 15px;
    font-weight: bold;
}

.btn:hover {
    background: #24569b;
}

.section {
    padding: 45px 20px;
    text-align: center;
}

.section h2 {
    color: #173b70;
    margin-bottom: 30px;
}

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
    max-width: 1100px;
    margin: auto;
}

.card {
    background: white;
    padding: 30px 15px;
    border-radius: 12px;
    box-shadow: 0 3px 12px #ccc;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}

.card h3 {
    color: #173b70;
}

.card p {
    line-height: 1.5;
}

.about {
    background: white;
}

footer {
    background: #173b70;
    color: white;
    text-align: center;
    padding: 25px;
}

@media(max-width:600px) {
    header h1 {
        font-size: 23px;
    }

    .hero h2 {
        font-size: 25px;
    }

    nav a {
        display: inline-block;
        margin: 8px;
    }
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

    <p>Quality Education for Students</p>

    <a class="btn" href="/enquiry">
        STUDENT ENQUIRY
    </a>

</div>

<div class="section about" id="about">

    <h2>About Our Academy</h2>

    <p>
        Welcome to Elite Maths Academy 2070.
        We focus on quality education
        and student success.
    </p>

</div>

<div class="section" id="courses">

    <h2>OUR COURSES</h2>

    <div class="cards">

        {% for course, description in courses %}

        <div class="card">
            <h3>{{ course }}</h3>
            <p>{{ description }}</p>
        </div>

        {% endfor %}

    </div>

    <a class="btn" href="/enquiry">
        Enquire About Courses
    </a>

</div>

<div class="section about" id="contact">

    <h2>CONTACT US</h2>

    <p>
        For Admission Enquiries,
        Please Contact Our Academy.
    </p>

    <a class="btn" href="/enquiry">
        Enquire Now
    </a>

</div>

<footer>

    <h3>ELITE MATHS ACADEMY 2070</h3>

    <p>Learn Today, Lead Tomorrow</p>

    <p>© 2026 Elite Maths Academy 2070</p>

    <p>All Rights Reserved</p>

</footer>

</body>
</html>
"""


# =================================
# STUDENT ENQUIRY FORM
# =================================

FORM_HTML = """
<!DOCTYPE html>
<html>
<head>

<title>Student Enquiry - Elite Maths Academy</title>

<meta name="viewport"
content="width=device-width, initial-scale=1">

<style>

body {
    font-family: Arial, sans-serif;
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
    text-decoration: none;
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

<h3 style="text-align:center">
STUDENT ENQUIRY FORM
</h3>

{% if submitted %}

    <h2 class="success">Thank You!</h2>

    <p class="success">
    Your enquiry form has been submitted.
    </p>

    <a class="home" href="/">
        Back to Home Page
    </a>

{% else %}

<form method="POST">

    <label>Student Name</label>
    <input type="text" name="student" required>

    <label>Father's Name</label>
    <input type="text" name="father" required>

    <label>Mobile Number</label>
    <input type="tel" name="mobile"
    pattern="[0-9]{10}" maxlength="10" required>

    <label>Programme / Class</label>

    <select name="class_name" required>
        <option value="">Select Programme</option>

        {% for course, description in courses %}
        <option value="{{ course }}">{{ course }}</option>
        {% endfor %}

    </select>

    <label>Subject</label>

    <select name="subject" required>
        <option value="">Select Subject</option>
        <option>Mathematics</option>
        <option>Physics</option>
        <option>Chemistry</option>
        <option>Biology</option>
        <option>Reasoning</option>
        <option>General Studies</option>
        <option>All Subjects</option>
        <option>Other</option>
    </select>

    <label>School / College Name</label>
    <input type="text" name="school">

    <label>City</label>
    <input type="text" name="city" required>

    <button type="submit">
        SUBMIT ENQUIRY
    </button>

</form>

<a class="home" href="/">
    Back to Home Page
</a>

{% endif %}

</div>

</body>
</html>
"""


# =================================
# HOME PAGE ROUTE
# =================================

@app.route("/")
def home():

    return render_template_string(
        HOME_HTML,
        courses=COURSES
    )


# =================================
# ENQUIRY PAGE ROUTE
# =================================

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

        print("NEW STUDENT ENQUIRY")
        print("Student:", student)
        print("Father:", father)
        print("Mobile:", mobile)
        print("Programme:", class_name)
        print("Subject:", subject)
        print("School:", school)
        print("City:", city)

        submitted = True

    return render_template_string(
        FORM_HTML,
        submitted=submitted,
        courses=COURSES
    )


# =================================
# RUN APPLICATION
# =================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
