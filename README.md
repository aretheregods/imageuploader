A simple website for uploading images to a flask python server

#1 Clone Repo:\n
git clone https://github.com/aretheregods/imageuploader.git
&&
cd imageuploader

#2 Init and Start Virtual Environment:\n
virtualenv --no-site-packages env\n
Windows: source env/Scripts/activate\n
OSX/Linux: source env/bin/activate

#3 Install Dependencies:\n
pip install -r requirements.txt

#4 Edit config:\n
Change config.py['SQLALCHEMY_DATABASE_URI'] to your own credentials

#5 Create Database and table:\n
python app.py db init\n
python app.py db migrate

#6 Start the app:\n
python app.py runserver

#7 See the site at:\n
http://localhost:5000
