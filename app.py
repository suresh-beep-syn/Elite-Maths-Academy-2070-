from flask import Flask, request, render_template_string
from datetime import datetime

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
    background: #edf2f7;
    padding: 20px;
}
.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 25px;
    border-radius: 12px;
}
h1 {
    text-align: center;
    color: #173b70;
}
input, select {
    width: 100%;
    padding: 12px;
    margin: 8px 0 15px;
    box-sizing: border-box;
}
button {
    background: #173b70;
    color: white;
    padding: 14px;
    border: 0;
    width: 100%;
    cursor: pointer;
}
</style>
</head>
<body>
<div class="container">
<h1>ELITE MATHS ACADEMY 2070</h1>
<h3>Student Enquiry Form</h3>

{% if submitted %}
<h2>Thank You!</h2>
<p>Your enquiry has been received.</p>
{% else %}
<form method="POST">
<label>Student Name</label>
<input name="student" required>

<label>Father's Name</label>
<input name="father" required>

<label>Mobile Number</label>
<input name="mobile" type="tel" pattern="[0-9]{10}" required>

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
<input name="school">

<label>City</label>
<input name="city" required>

<button type="submit">Submit Enquiry</button>
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

        print("NEW STUDENT ENQUIRY")
        print(student, father, mobile, class_name)
        print(subject, school, city)

        submitted = True

    return render_template_string(HTML, submitted=submitted)

if __name__ == "__main__":
    app.run()
