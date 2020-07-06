import os

from flask import Flask, render_template, request

app = Flask(__name__)
#static_path = os.path.join(app.route(self="__main__"), '../client/static')
@app.route("/")
def index():

    return render_template("app.html")
@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':

        amount = float(request.form['num1'])
        pct = float(request.form['num2'])
        years = float(request.form['num3'])
        if pct!=0:
            pct = pct / 100
            month_pay = round((amount * pct * (1 + pct) ** years) / (12 * ((1 + pct) ** years - 1)),2)
            sum = round(month_pay * years * 12,2)
            return render_template('app.html', sum="Your monthly payment will be: "+str(month_pay)+ "\n    For the entire period you will pay:"+ str(sum))
        else:
            month_pay = round(amount/(years*12),2)
            sum = amount
            return render_template('app.html', sum="Your monthly payment will be: "+str(month_pay)+ "\n    For the entire period you will pay:"+ str(sum))

if __name__ == "__main__":
    app.run(debug=True)