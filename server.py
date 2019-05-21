from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def the_home_page():
    print('Someone is visiting the home page!')
    random_number = 2
    dice_rolls = [5, 3, 4, 2, 2]
    return render_template(
        'index.html',
        a_very_random_number=random_number,
        rolls=dice_rolls
    )

@app.route('/ada')
def ada_page():
    return 'The ada cohort is my favorite data science cohort!'

@app.route('/roll-dice')
def roll_dice():
    return '''
    <h1>Here is your number: {}</h1>
    <p>This is a <em>very</em> random number</p>
    '''.format(4)

@app.route('/fancy-math-form')
def fancy_math():
    return render_template('fancy-math-form.html')

@app.route('/the-result-page', methods=['POST'])
def math_results():
    number = request.form['n']
    result = int(number) + 3
    return render_template(
        'math-results.html',
        result=result
    )

@app.route('/bootstrap-demo')
def bootstrap_demo():
    return render_template('bootstrap.html')