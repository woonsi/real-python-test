from flask import Flask

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")

def hello_world():
    return "Hello, World!!???!?!?!?"

@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael" :
        return "Hello, {}".format(name)
    else:
        return "Not Found", 404

if __name__ == "__main__":
    app.run()
    

