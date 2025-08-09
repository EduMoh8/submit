from flask import Flask, render_template
import os

app = Flask(__name__)

# Home/Main Page
@app.route('/')
def index():
    return render_template('ook_main.html')

# Leaderboard Page
@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')

# Generator Page (fixes your BuildError)
@app.route('/generator')
def generator():
    return render_template('generator.html')

if __name__ == '__main__':
    # Make sure templates and static folders exist in the same directory
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
