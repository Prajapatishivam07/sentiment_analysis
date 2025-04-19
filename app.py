from flask import Flask, render_template, request, redirect, url_for
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
        description = "The sentiment of the text is positive, indicating happiness or satisfaction."
        suggestion = "Stay positive and share your energy!"
        return render_template('result.html', sentiment=sentiment, description=description, suggestion=suggestion, redirect_to='positive')
    elif polarity < 0:
        sentiment = "Negative"
        description = "The sentiment of the text is negative, reflecting sadness or frustration."
        suggestion = "Take some time to rest or talk to a friend."
        return render_template('result.html', sentiment=sentiment, description=description, suggestion=suggestion, redirect_to='negative')
    else:
        sentiment = "Neutral"
        description = "The sentiment of the text is neutral — a calm, balanced tone."
        suggestion = "Try expressing more emotions or views!"
        return render_template('result.html', sentiment=sentiment, description=description, suggestion=suggestion, redirect_to='neutral')

@app.route('/positive')
def positive():
    return render_template('positive.html')

@app.route('/negative')
def negative():
    return render_template('negative.html')

@app.route('/neutral')
def neutral():
    return render_template('neutral.html')

if __name__ == '__main__':
    app.run(debug=True)
