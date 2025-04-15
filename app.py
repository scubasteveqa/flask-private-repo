from flask import Flask, render_template
# Import from private package
from private_utils import format_message

app = Flask(__name__)

@app.route('/')
def home():
    formatted_message = format_message("Hello from private package!")
    return render_template('index.html', message=formatted_message)

if __name__ == '__main__':
    app.run(debug=True)
