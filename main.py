from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define the root route
@app.route('/')
def home():
    return "Hello, World! This is a jjjjjjjjjdummy Flask app."

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
