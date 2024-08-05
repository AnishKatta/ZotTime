from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

API_KEY = "AIzaSyDr0z0C-1w5yxssvIn9_1gJHPmAnY_fMmI"


@app.route('/')
def index():
    return render_template('form.html')

@app.route('/find-classroom/<year>/<quarter>/<ccode>')
def find_classroom(year, quarter, ccode):
    peterportal_api_url = f"https://api.peterportal.org/rest/v0/schedule/soc?term={year} {quarter}&sectionCodes={ccode}"
    course_info = requests.get(peterportal_api_url).json()
    course_classroom = course_info['schools'][0]['departments'][0]['courses'][0]['sections'][0]['meetings'][0]['bldg']
    return course_classroom



@app.route('/submit-form', methods = ["POST"])
def submit_form():
    year = request.form.get('year')
    quarter = request.form.get('quarter')
    ccode1 = request.form.get('ccode1')
    ccode2 = request.form.get('ccode2')




@app.route("/locate-classroom/<course_classroom>")
def locate_classroom(course_classroom):
    address = f"{course_classroom}, University of California, Irvine, CA"
    places_api_url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={address}&key={API_KEY}"
    places_api_obj = requests.get(places_api_url).json()
    place_id = places_api_obj["results"][0]["place_id"]
    return place_id





if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000,debug=True)

