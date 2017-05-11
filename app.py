#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, flash, render_template, request, redirect, url_for
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import logging
from logging import Formatter, FileHandler
from werkzeug.utils import secure_filename
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Create Database
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
engine.execute('CREATE DATABASE IF NOT EXISTS photos')
engine.execute('USE photos')

# Create Tables
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Photos(db.Model):
    __tablename__ = 'Photos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    file_location = db.Column(db.String(120), unique=True)
    upload_date = db.Column(db.DateTime, unique=True, default=datetime.now)

    def __init__(self, name=None, file_location=None, upload_date=datetime.now):
        self.name = name
        self.file_location = file_location
        self.upload_date = upload_date

    def __repr__(self):
        return '<id {}>'.format(self.id)

# Routing
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            ts = time.time()
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            timestamp = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            image_data = Photos(name=filename, file_location=filepath, upload_date=timestamp)
            file.save(filepath)
            db.session.add(image_data)
            db.session.commit()
            flash('You uploaded %s' % filename)
            return redirect(url_for('upload_file',
                                    filename=filename))
    return render_template('pages/home.html')

# Error Handling Routes
@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    manager.run()
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
