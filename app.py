from flask import Flask, render_template

flask_app =  Flask(__name__)

@flask_app.route('/')
def home():
    return render_template('index.html')

@flask_app.route('/interview-section')
def interview():
    return render_template('interview-section.html')


@flask_app.route('/interview-zone')
def interviewzone():
    return render_template('interview-zone.html')

@flask_app.route('/about-us')
def aboutus():
    return render_template('about-us.html')


@flask_app.route('/help')
def help():
    return render_template('help.html')

if __name__ =='__main__':
    flask_app.run(host='127.0.0.1',port=5002,debug=True)