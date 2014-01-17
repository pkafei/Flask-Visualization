import os
from flask import Flask, render_template, send_from_directory
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#-----------------------------
# initialization
# -----------------------------

app = Flask(__name__)

app.config.update(
    DEBUG=True,
)

#------------------------------
#database
#------------------------------

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/viz_data'
db = SQLAlchemy(app)
from sqlalchemy import create_engine
engine = create_engine(['postgresql://postgres:root@localhost/viz_data'])
#------------------------------
#controllers
#------------------------------

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def base():
    return render_template('index.html')


#------------------------------
#launch
#------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


