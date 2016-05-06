from flask import Flask, render_template, request

from db import get_db
app = Flask(__name__, template_folder='.')


@app.route("/")
@app.route("/homepage.html")
def homepage():
    return render_template('homepage.html')

@app.route("/aboutus.html")
def aboutus():
    return render_template('aboutus.html')
@app.route("/audi.html")
def audi():
    return render_template('audi.html')
@app.route("/bently.html")
def bently():
    return render_template('bently.html')
@app.route("/classic.html")
def classic():
    return render_template('classic.html')
@app.route("/contactus.html")
def contactus():
    return render_template('contactus.html')
@app.route("/currentinventory.html")
def currentinventory():
    return render_template('currentinventory.html')
@app.route("/ferrari.html")
def ferrari():
    return render_template('ferrari.html')
@app.route("/lamborghini.html")
def lamborghini():
    return render_template('lamborghini.html')
@app.route("/merc.html")
def merc():
    return render_template('merc.html')
@app.route("/porshe.html")
def porshe():
    return render_template('porshe.html')
@app.route("/previouslysold.html")
def previouslysold():
    return render_template('previouslysold.html')
@app.route("/rangerover.html")
def rangerover():
    return render_template('rangerover.html')
@app.route("/rolls.html")
def rolls():
    return render_template('rolls.html')
@app.route("/sellingyourcar.html")
def sellingyourcar():
    return render_template('sellingyourcar.html')
@app.route("/testimonial.html")
def testimonial():
    return render_template('testimonial.html')
@app.route("/submit.html", methods=['POST'])
def submit():
    
    connection = get_db()
    
    c = connection.cursor()
    
    firstname,_,surname = request.form['name'].partition(' ')
    
    
    c.execute('INSERT INTO sales       (title,firstname,surname,organisation,email,telepone,carmileage,carmodel,carmake,careregistration,carregdate,comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)',
                            (request.form['title'],firstname,surname,request.form['organisation'],request.form['email'],request.form['phone'],
                              request.form['carmileage'],request.form['carmodel'],request.form['make'],
                              request.form['carreg'], request.form['date'], request.form['comment']))
    
    connection.commit()
    
    
    
    return render_template('submit.html')
@app.route("/customerinfo.html")
def customerinfo():
    
    connection = get_db()
    
    c = connection.cursor()
    
    sales = c.execute('SELECT * FROM sales')
    
    
    
    return render_template('customerinfo.html', sales=sales)

if __name__ == "__main__":
    import os
    app.debug = True
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', '8080')))
