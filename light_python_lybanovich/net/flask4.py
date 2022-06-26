from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def home():
    thing = request.values.get('thing')
    height = request.values.get('height')
    color = request.values.get('color')
    return render_template('flask4.html',
        thing=thing, height=height, color=color)
app.run(debug=True)