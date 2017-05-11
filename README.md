A simple website for uploading images to a flask python server

<strong>#1 Clone Repo:</strong><br />
git clone https://github.com/aretheregods/imageuploader.git
<br />
cd imageuploader

<strong>#2 Init and Start Virtual Environment:</strong><br />
virtualenv --no-site-packages env<br />
Windows: source env/Scripts/activate<br />
OSX/Linux: source env/bin/activate

<strong>#3 Install Dependencies:</strong><br />
pip install  -r requirements.txt

<strong>#4 Edit config:</strong><br />
Change config.py['SQLALCHEMY_DATABASE_URI'] to your own credentials

<strong>#5 Create Database and table:</strong><br />
python app.py db init<br />
python app.py db migrate

<strong>#6 Start the app:</strong><br />
python app.py runserver

<strong>#7 See the site at:</strong><br />
http://localhost:5000
