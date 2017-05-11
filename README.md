A simple website for uploading images to a flask python server

#1 Clone Repo:<br />
git clone https://github.com/aretheregods/imageuploader.git
<br />
cd imageuploader

#2 Init and Start Virtual Environment:<br />
virtualenv --no-site-packages env<br />
Windows: source env/Scripts/activate<br />
OSX/Linux: source env/bin/activate

#3 Install Dependencies:<br />
pip install  -r requirements.txt

#4 Edit config:<br />
Change config.py['SQLALCHEMY_DATABASE_URI'] to your own credentials

#5 Create Database and table:<br />
python app.py db init<br />
python app.py db migrate

#6 Start the app:<br />
python app.py runserver

#7 See the site at:<br />
http://localhost:5000
