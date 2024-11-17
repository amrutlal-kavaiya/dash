from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/dash')
def dash():
    with open('data.json') as f:
        data = json.load(f)
    return render_template('dash.html', data=json.dumps(data))

if __name__ == '__main__':
    app.run(debug=True)