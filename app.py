from flask import Flask, render_template, request, url_for
from model import predict_sentiment

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        prediction = predict_sentiment(prompt)
        sentiment = prediction["label"]

        if sentiment == "POSITIVE":
            image = url_for('static', filename='images/happy.jpeg')
        else:
            image = url_for('static', filename='images/sad.jpeg')
        print(image)
        try:
            return render_template('index_img.html', image=image)
        except:
            return 'There was an issue.'

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
