from flask import Flask
app = Flask(__name__)

@app.get("/")
def hello():
    return "If you are seeing this message, then its means entire CICD flow is successful.. thank you .. visit again...\n"
