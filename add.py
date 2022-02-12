from flask import Flask, render_template

import db

app = Flask(__name__)


# /indexにGETでアクセスが来たらindex.htmlを返す
@app.route("/")
def index():
    customers = db.get_all_customers()
    return render_template("index.html")


@app.route("/sdgs/<sdgs_id>", methods=["GET"])
def show(sdgs_id):
    customers = db.get_info(sdgs_id)
    # print(customers)
    return render_template("01.html", customers=customers, sdgs_id=sdgs_id)


@app.route("/02")
def show02():
    customers = db.get_all_customers()
    return render_template("02.html")


@app.route("/03")
def show03():
    customers = db.get_all_customers()
    return render_template("03.html")


@app.route("/04")
def show04():
    customers = db.get_all_customers()
    return render_template("04.html")


@app.route("/05")
def show05():
    customers = db.get_all_customers()
    return render_template("05.html")


@app.route("/06")
def show06():
    customers = db.get_all_customers()
    return render_template("06.html")


@app.route("/07")
def show07():
    customers = db.get_all_customers()
    return render_template("07.html")


@app.route("/08")
def show08():
    customers = db.get_all_customers()
    return render_template("08.html")


@app.route("/09")
def show09():
    customers = db.get_all_customers()
    return render_template("09.html")


@app.route("/10")
def show10():
    customers = db.get_all_customers()
    return render_template("10.html")


@app.route("/11")
def show11():
    customers = db.get_all_customers()
    return render_template("11.html")


@app.route("/12")
def show12():
    customers = db.get_all_customers()
    return render_template("12.html")


@app.route("/13")
def show13():
    customers = db.get_all_customers()
    return render_template("13.html")


@app.route("/14")
def show14():
    customers = db.get_all_customers()
    return render_template("14.html")


@app.route("/15")
def show15():
    customers = db.get_all_customers()
    return render_template("15.html")


@app.route("/16")
def show16():
    customers = db.get_all_customers()
    return render_template("16.html")


@app.route("/17")
def show17():
    customers = db.get_all_customers()
    return render_template("17.html")


if __name__ == '__main__':
    port = 5000
    app.run(port=port, debug=True)
