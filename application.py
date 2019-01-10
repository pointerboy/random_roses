#!/usr/bin/env python3
import requests
import random
from flask import Flask, render_template
app = Flask(__name__)

words_f = "/usr/share/dict/words"
words = open(words_f).read().splitlines()

@app.route('/')
def index_route():
  setenc = "Roses are red, violets are blue"

  for i in range(0, random.randrange(0, 5)):
    rad_index = random.randrange(0, len(words))
    setenc += " " + words[rad_index]
  print(setenc)
  return render_template("index.html", setenc=setenc)

if __name__ == "__main__":
  app.run(debug=True)
