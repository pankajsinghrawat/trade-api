from flask import Flask
from apis.coreapi import coreapiblueprint

app = Flask(__name__)
app.register_blueprint(coreapiblueprint, url_prefix='/api')

def main():
        app.run(debug=True)

if __name__ == "__main__":
    main()
