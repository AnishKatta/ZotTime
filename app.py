from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('classes.html')

@app.route('/get_locations_of_courses/<year>/<quarter>/<ccode1>/<ccode2>')
def get_locations_of_courses(year, quarter, ccode1, ccode2):
    course_1_url = f"https://api.peterportal.org/rest/v0/schedule/soc?term={year} {quarter}&sectionCodes={ccode1}"
    course_2_url = f"https://api.peterportal.org/rest/v0/schedule/soc?term={year} {quarter}&sectionCodes={ccode2}"
    course_1_info = requests.get(course_1_url).json()
    course_2_info = requests.get(course_2_url).json()
    course_1_name = course_1_info['schools'][0]['departments'][0]['courses'][0]['sections'][0]['meetings'][0]['bldg']
    course_2_name = course_2_info['schools'][0]['departments'][0]['courses'][0]['sections'][0]['meetings'][0]['bldg']
    return render_template('classes.html', loc1 = course_1_name, loc2 = course_2_name)



@app.route('/submit-form', methods = ["POST"])
def submit_form():
    year = request.form.get('year')
    quarter = request.form.get('quarter')
    ccode1 = request.form.get('ccode1')
    ccode2 = request.form.get('ccode2')
    return redirect(url_for('get_locations_of_courses', year = year, quarter = quarter, ccode1 = ccode1, ccode2 = ccode2))






if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000,debug=True)

