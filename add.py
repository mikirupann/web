from flask import Flask, render_template

import db

app = Flask(__name__)


# /indexにGETでアクセスが来たらindex.htmlを返す
@app.route("/")
def index():
    customers = db.get_all_customers()
    return render_template("index.html")

< !DOCTYPE
html >
< html
lang = "ja" >

< head >
< link
rel = "stylesheet"
href = "static/css/style.css" >
< meta
charset = "UTF-8" >
< title > SDGsを学ぶアプリ < / title >
< / head >
< body >
< header >
< a >
< img
src = "http://line.blogimg.jp/takeda_souun/imgs/d/3/d3b74bec.jpg"
alt = "平泉町ロゴ"
height = "80"
width = "130" >
< / a >
< h1
style = "text-align:center" > SDGsを学ぼう < / h1 >
< / header >
< form
action = ""
method = "post" >
< div
style = "width: 600px; margin: auto;" >
< select


class ="pull" size="1" >

< option
value = "" > 選択してください < / option >
< option
value = "選択肢1" > 1.
貧困をなくそう < / option >
< option
value = "選択肢2" > 2.
飢餓をゼロに < / option >
< option
value = "選択肢3" > 3.
すべての人に健康と福祉を < / option >
< option
value = "選択肢4" > 4.
質の高い教育をみんなに < / option >
< option
value = "選択肢5" > 5.
ジェンダー平等を実現しよう < / option >
< option
value = "選択肢6" > 6.
安全な水とトイレを世界中に < / option >
< option
value = "選択肢7" > 7.
エネルギーをみんなにそしてクリーンに < / option >
< option
value = "選択肢8" > 8.
働きがいも経済成長も < / option >
< option
value = "選択肢9" > 9.
産業と技術革新の基盤をつくろう < / option >
< option
value = "選択肢10" > 10.
人や国の不平等をなくそう < / option >
< option
value = "選択肢11" > 11.
住み続けられるまちづくりを < / option >
< option
value = "選択肢12" > 12.
つくる責任つかう責任 < / option >
< option
value = "選択肢13" > 13.
気候変動に具体的な対策を < / option >
< option
value = "選択肢14" > 14.
海の豊かさを守ろう < / option >
< option
value = "選択肢15" > 15.
陸の豊かさを守ろう < / option >
< option
value = "選択肢16" > 16.
平和と公正をすべての人に < / option >
< option
value = "選択肢17" > 17.
パートナーシップで目標を達成しよう < / option >
< / select >
< input
type = "submit"
value = "検索" >
< / div >
< / form >
< div


class ="hyou1" >

< a
href = "sdgs/1" > < img
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs1-1536x1024.png"
alt = "貧困をなくそう"
height = "200"
width = "300" > < / a >
< a
href = "sdgs/2" > < img
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs2-1536x1024.png"
alt = "飢餓をゼロに"
height = "200"
width = "300" > < / a >
< a
href = "sdgs/3" > < img
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs3-1536x1024.png"
alt = "すべての人に健康と福祉を"
height = "200"
width = "300" > < / a >
< a
href = "sdgs/4" > < img
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs4-1536x1024.png"
alt = "質の高い教育をみんなに"
height = "200"
width = "300" > < / a >
< a
href = "sdgs/5" > < img
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs5-1536x1024.png"
alt = "ジェンダー平等を実現しよう"
height = "200"
width = "300" > < / a >
< a
href = "sdgs/6" > < img
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs6-1536x1024.png"
alt = "安全な水とトイレを世界中に"
height = "200"
width = "300" > < / a >
< a
href = "sdgs/7" > < img
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs7-1536x1024.png"
alt = "エネルギーをみんなに"
height = "200"
width = "300" > < / a >
< a
href = "sdgs/8" > < img
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs8-1536x1024.png"
alt = "働きがいも経済成長も"
height = "200"
width = "300" > < / a >
< a
href = "sdgs/9" > < img
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs9-1536x1024.png"
alt = "産業と技術革新の基盤をつくろう"
height = "200"
width = "300" > < / a >
< a
href = "sdgs/10" > < img
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs10-1536x1024.png"
alt = "人や国の不平等をなくそう"
height = "200"
width = "300" > < / a >
< a
href = "sdgs/11" > < img
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs11-1536x1024.png"
alt = "住み続けられるまちづくりを"
height = "200"
width = "300" > < / a >
< a
href = "sdgs/12" > < img
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs12-1536x1024.png"
alt = "つくる責任つかう責任"
height = "200"
width = "300" > < / a >
< a
href = "sdgs/13" > < img
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs13-1536x1024.png"
alt = "気候変動に具体的な対策を"
height = "200"
width = "300" > < / a >
< a
href = "sdgs/14" > < img
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs14-1536x1024.png"
alt = "海の豊かさを守ろう"
height = "200"
width = "300" > < / a >
< a
href = "sdgs/15" > < img
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs15-1536x1024.png"
alt = "陸の豊かさを守ろう"
height = "200"
width = "300" > < / a >
< a
href = "sdgs/16" > < img
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs16-1536x1024.png"
alt = "平和と公正をすべての人に"
height = "200"
width = "300" > < / a >
< a
href = "sdgs/17" > < img
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs17-1536x1024.png"
alt = "パートナーシップで目標を達成しよう"
height = "200"
width = "300" > < / a >
< !-- & lt;! & ndash; < input
type = "image"
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs1-1536x1024.png"
alt = "貧困をなくそう" & ndash; & gt;
& lt;! & ndash;
title = "貧困をなくそう"
height = "200"
width = "300" > & ndash; & gt;
& lt;! & ndash; < input
type = "image"
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs2-1536x1024.png"
alt = "飢餓をゼロに"
title = "飢餓をゼロに"
height = "200"
width = "300" > & ndash; & gt;
& lt;! & ndash; < input
type = "image"
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs3-1536x1024.png"
alt = "すべての人に健康と福祉を"
title = "すべての人に健康と福祉を"
height = "200"
width = "300" > & ndash; & gt;
& lt;! & ndash; < input
type = "image"
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs4-1536x1024.png"
alt = "質の高い教育をみんなに"
title = "質の高い教育をみんなに"
height = "200"
width = "300" > & ndash; & gt;
& lt;! & ndash; < input
type = "image"
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs5-1536x1024.png"
alt = "ジェンダー平等を実現しよう"
title = "ジェンダー平等を実現しよう"
height = "200"
width = "300" > & ndash; & gt;
& lt;! & ndash; < input
type = "image"
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs6-1536x1024.png"
alt = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs6-1536x1024.png"
title = "安全な水とトイレを世界中に"
height = "200"
width = "300" >
< / div >
< div


class ="hyou1" >

< input
type = "image"
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs7-1536x1024.png"
alt = "エネルギーをみんなに"
title = "エネルギーをみんなに"
height = "200"
width = "300" >
< / div >
< div


class ="hyou1" >

< input
type = "image"
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs8-1536x1024.png"
alt = "働きがいも経済成長も"
title = "働きがいも経済成長も"
height = "200"
width = "300" >
< / div >
< div


class ="hyou1" >

< input
type = "image"
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs9-1536x1024.png"
alt = "産業と技術革新の基盤をつくろう"
title = "産業と技術革新の基盤をつくろう"
height = "200"
width = "300" >
< / div >
< div


class ="hyou1" >

< input
type = "image"
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs10-1536x1024.png"
alt = "人や国の不平等をなくそう"
title = "人や国の不平等をなくそう"
height = "200"
width = "300" >
< / div >
< div


class ="hyou1" >

< input
type = "image"
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs11-1536x1024.png"
alt = "住み続けられるまちづくりを"
title = "住み続けられるまちづくりを"
height = "200"
width = "300" >
< / div >
< div


class ="hyou1" >

< input
type = "image"
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs12-1536x1024.png"
alt = "つくる責任つかう責任"
title = "つくる責任つかう責任"
height = "200"
width = "300" >
< / div >
< div


class ="hyou1" >

< input
type = "image"
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs13-1536x1024.png"
alt = "気候変動に具体的な対策を"
title = "気候変動に具体的な対策を"
height = "200"
width = "300" >
< / div >
< div


class ="hyou1" >

< input
type = "image"
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs14-1536x1024.png"
alt = "海の豊かさを守ろう"
title = "海の豊かさを守ろう"
height = "200"
width = "300" >
< / div >
< div


class ="hyou1" >

< input
type = "image"
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs15-1536x1024.png"
alt = "陸の豊かさを守ろう"
title = "陸の豊かさを守ろう"
height = "200"
width = "300" >
< / div >
< div


class ="hyou1" >

< input
type = "image"
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs16-1536x1024.png"
alt = "平和と公正をすべての人に"
title = "平和と公正をすべての人に"
height = "200"
width = "300" >
< / div >
< div


class ="hyou1" >

< input
type = "image"
src = "https://naruhodosdgs.jp/wp-content/uploads/2020/06/sdgs17-1536x1024.png"
alt = "パートナーシップで目標を達成しよう"
title = "パートナーシップで目標を達成しよう"
height = "200"
width = "300" >
< / div > -->
< / div >

< / body >
< / html >


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
