from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#create an instance of Flask
app = Flask(__name__)

#Use Pymongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
#delete in production
mongo.db.collection.drop()

#route to render index.html template using data from mongo
@app.route("/")
def index():

    #find one record of data from moongo database
    mars_data = mongo.db.mars_data.find_one()
    
    #return template and data
    return render_template("index.html", mars_data=mars_data)
    
#route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    mars = mongo.db.mars_data
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    
    return redirect("/", code=302)
    


if __name__ == "__main__":
    app.run(debug=True)     



