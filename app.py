import os
from flask import Flask, render_template, send_from_directory
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import CHAR, INTEGER, DOUBLE_PRECISION
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
engine = create_engine(['postgresql://postgres:root@localhost/viz_data'])
Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy.ext.declarative import declarative_base


#-----------------------------
# initialization
# -----------------------------

app = Flask(__name__)

app.config.update(
    DEBUG=True,
)

#------------------------------
#database config
#------------------------------

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ['postgresql://postgres:root@localhost/viz_data']
db = SQLAlchemy(app)

#------------------------------
#database models
#------------------------------
Base = declarative_base()
class Bankruptcy(Base):
    __tablename__ = 'bankruptcy'
    city = Column(CHAR(125), primary_key=False)
    state = Column(CHAR(125))
    population = Column(INTEGER)
    unemployment = Column(DOUBLE_PRECISION)


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


