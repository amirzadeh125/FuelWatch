from flask import Flask, redirect, url_for, render_template, request 
import feedparser
from urllib.parse import urlencode
import pprint
from suburbs import suburbs, header, product
import datetime
from flask_mail import Mail, Message
import smtplib


tod = datetime.date.today()
tom = tod+ datetime. timedelta(days=1)
tod = tod.strftime("%d-%b-%Y")
tom = tom.strftime("%d-%b-%Y")

def base():
    urls = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?' 
    feed = feedparser.parse(urls)
    data_to_populate=[{
                          'date':datetime.date.today(),
                          'product':'Unleaded Petrol',
                          'today_price': i['price'],
                          'brand': i['brand'],
                          'address': i['address'],
                          'suburb': i['location']} for i in feed['entries'] ]
                 
    return data_to_populate


def generate_url(FuelType ='1', location='perth', Day='today',surronding ='None' ):
    urls = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?' + urlencode({
            'Product': FuelType,
            'Suburb':location,
            'Day': Day})
    feed = feedparser.parse(urls)
    if Day == 'today':
        Day = tod
    else:
        Day = tom 
    if surronding == 'yes':
        data_to_populate=[{
                          'date':Day,
                          'product':product[FuelType],
                          'today_price': i['price'],
                          'brand': i['brand'],
                          'address': i['address'],
                          'suburb': i['location']} for i in feed['entries'] ]
    else:
        data_to_populate=[{
                          'date':Day,
                          'product':product[FuelType],
                          'today_price': i['price'],
                          'brand': i['brand'],
                          'address': i['address'],
                          'suburb': i['location']} for i in feed['entries'] if i['location'] == location.upper()  ]                
           
    return data_to_populate
  

app = Flask(__name__)

@app.route("/")
def home():
    FuelType = request.args.get('FuelType')
    location = request.args.get('Suburb')
    Day = request.args.get('Day')
    surronding = request.args.get('surronding')

    if Day == 'today_tomorrow' :
            tod = generate_url(FuelType , location , 'today',surronding)
            tmw = generate_url(FuelType, location, 'tomorrow',surronding)
            data_to_populate = sorted( list( tod ) + list( tmw ), key = lambda i: i['today_price'])
            return render_template("index.html", suburbs = suburbs , header = header , table_content= data_to_populate ) 
 
    elif Day =='today' or Day == 'tomorrow': 
            data_to_populate = generate_url(FuelType, location, Day, surronding)
            return render_template("index.html", suburbs = suburbs , header = header , table_content= data_to_populate ) 
            
    elif Day == None:
        data_to_populate = base()
        
        return render_template("index.html", suburbs = suburbs , header = header, table_content= data_to_populate )
               
    return render_template("index.html", suburbs = suburbs , header = header , table_content= data_to_populate ) 

@app.route("/home")
def home1():
    return redirect(url_for("home"))
    
contact={}

@app.route("/contacted", methods=["POST"])
def contacted():
    first_name=request.form.get("firstname")
    last_name=request.form.get("lastname")
    email=request.form.get("email")
    
    message= "Your email is send"
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("maryakargaranrokni@gmail.com","PASSWORD")
    server.sendmail("maryakargaranrokni@gmail", email, message)
    
    if not first_name or not last_name or not email:
        error_statement= "All Form Fields Required"
        return render_template("contact.html", 
            error_statement=error_statement,
            first_name=first_name,
            last_name=last_name,
            email=email)
    
    contact.append(f"{first_name}{last_name} {email}")
    return render_template("contact.html")
  
@app.route("/contact")
def contact():
    return render_template("contact.html")
    
    
@app.route("/about")
def about():
    return render_template("about.html") 



    


if __name__ == "__main__":
    app.run(debug=True)