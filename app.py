# app.py

# 1. Import the Flask class from the Flask package
from flask import Flask, render_template

# 2. Create an instance of the Flask class
#    __name__ determines the root path for the application.
app = Flask(__name__)

# 3. Define a route (URL) that will trigger a function
@app.route('/')
def home():
    return render_template('index.html', message='Welcome to my site!')

# 5. Run the app only if this file is executed directly
#    'debug=True' enables auto-reload for development.
if __name__ == '__main__':
    app.run(debug=True)
