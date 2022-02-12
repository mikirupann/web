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


if __name__ == '__main__':
    port = 5000
    app.run(port=port, debug=True)
