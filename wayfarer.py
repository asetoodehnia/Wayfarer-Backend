from flask import Flask, request, render_template, redirect, abort, flash, jsonify
app = Flask(__name__)


@app.route("/")
def index():
    render_template("index.html")

if __name__ == "__main__":
    app.run()



