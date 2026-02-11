from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CI/CD Pipeline Successful</h1>
    <p>This Docker image was built automatically using Jenkins.</p>
    <p>Source Code → Jenkins → Docker Image</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
