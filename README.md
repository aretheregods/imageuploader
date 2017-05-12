A simple website for uploading images to a flask python server

<strong>#1 Clone Repo:</strong><br />
git clone https://github.com/aretheregods/imageuploader.git
<br />
cd imageuploader

<strong>#2 Init and Start Virtual Environment:</strong><br />
<em>(If virtualenv isn't installed)</em><br />
<em>pip install virtualenv</em><br />
virtualenv --no-site-packages env<br />
Windows CMD(Or Powershell): env/Scripts/activate<br />
Windows Bash(Git Bash or MinGW): source env/Scripts/activate<br />
OSX/Linux: source env/bin/activate

<strong>#3 Install Dependencies:</strong><br />
pip install  -r requirements.txt

<strong>#4 Edit database config:</strong><br />
Change app.py <pre>engine = engine.create_engine(<strong><em>your_database_address</em></strong>)</pre><br />
Change config.py['SQLALCHEMY_DATABASE_URI'] to your own credentials

<strong>#5 Create Database and table:</strong><br />
python app.py db init<br />
python app.py db migrate<br />
python app.py db upgrade

<strong>#6 Start the app:</strong><br />
python app.py runserver

<strong>#7 See the site at:</strong><br />
http://localhost:5000

<strong>#<em>Just in case~</em>Delete mysql photos database:</strong><br />
In a terminal window -> mysql -u your_username -p<br />
-> USE photos;<br />
(If this database exists already, delete it)<br />
-> DROP DATABASE photos;<br />
(Go back to terminal with \q)<br />
-> \q<br />
(Retry previous steps 5 - 7)
