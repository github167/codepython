from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define what happens when a user visits the main page "/"
@app.route("/")
def home():
    return """
    <html>
        <head><title>My Codespace Site</title></head>
        <body>
            <h1>222Hello from GitHub Codespaces!</h1>
            <p>This simple website is running completely in the cloud using Python.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    # Run the server on port 5000
    app.run(host="0.0.0.0", port=5000)

