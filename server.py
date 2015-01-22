import os
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

import simple_file_blueprint

app.register_blueprint(simple_file_blueprint.blueprint, url_prefix='/fileserver')

@app.route('/')
def entry():
    return render_template('index.html')


if __name__ == '__main__':
  app.run(port=3000)