A simple website for uploading images to a flask python server

#1 Clone Repo: 
git clone https://github.com/aretheregods/imageuploader.git
&&
cd imageuploader

#2 Init and Start Virtual Environment: 
virtualenv --no-site-packages env
#
source env/Scripts/activate

#3 Install Dependencies: 
pip install -r requirements.txt

#4 Edit config: 
Change config.py['SQLALCHEMY_DATABASE_URI'] to your own credentials

#5 Create Database and table: 
python app.py db init
#
python app.py db migrate

#6 Start the app: 
python app.py runserver

#7 See the site at: 
http://localhost:5000

