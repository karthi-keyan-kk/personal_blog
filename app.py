from flask import Flask, render_template, request, session, redirect, url_for
from queris import Query as query
from datetime import date

app = Flask(__name__)
app.secret_key = "YOUR_KEY"

data = query.auth()

today = date.today().strftime("%d-%m-%Y")

@app.route('/')
def home():
    d = query.all_data()
    return render_template("home.html", data = d)

@app.route('/brief/<int:id>')
def brief(id):
    d = query.data(int(id))
    return render_template("brief.html", data = d)

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route('/admin', methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        user_name = request.form.get("mail")
        pwd = request.form.get("pwd")
        if data[0] == user_name and data[1] == pwd:
            session["user_name"] = data[0]
            return redirect(url_for('adminpage'))
        else:
            return render_template("admin.html", error = "Invalid Username or Password")
    else:
        return redirect(url_for('admin'))

@app.route('/adminpage')
def adminpage():
    d = query.all_data()
    if "user_name" in session:
        # session.pop("user_name", None)
        return render_template("adminpage.html", data = d)
    
@app.route("/adminpage", methods=["GET", "POST"])
def admin_insert():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        query.insert_data(title, content, today)
        return redirect(url_for("adminpage"))
    
@app.route("/update_blog/<int:id>")
def update_blog(id):
    d = query.data(int(id))
    return render_template("update.html", data = d)

@app.route("/update_blog/<int:id>", methods=["GET", "POST"])
def updating(id):
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        query.update_blog(id=int(id), title=str(title), content=str(content), date=str(today))
        return redirect(url_for("adminpage"))
    
@app.route("/delete/<int:id>")
def delete(id):
    a = query.count_user(int(id))
    if a > 0:
        query.delete_blog(int(id))
        return redirect(url_for('adminpage'))

@app.route("/logout")
def logout():
    session.pop("user_name", None)
    return redirect(url_for("admin"))


if __name__ == "__main__":
    app.run(debug=True)
