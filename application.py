#!/usr/bin/env python3
import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index_route():
  return render_template("index.html")

if __name__ == "__main__":
  print("listing jokes")
  for joke in jokes_list:
    print(joke.contents)

  app.run(debug=True)
