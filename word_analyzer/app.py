from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    analysis = {}
    if request.method == 'POST':
        user_input = request.form['text'].lower()
        words = user_input.split()
        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        repeated_words = {word: count for word, count in freq.items() if count > 1}
        sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        most_common = max(freq.items(), key=lambda item: item[1]) if freq else ("None", 0)
        least_common = min(freq.items(), key=lambda item: item[1]) if freq else ("None", 0)

        analysis = {
            'freq': freq,
            'repeated': repeated_words,
            'sorted_freq': sorted_freq,
            'most_common': most_common,
            'least_common': least_common
        }

    return render_template('index.html', analysis=analysis)

if __name__ == '__main__':
    app.run(debug=True)
