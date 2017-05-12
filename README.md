A simple website for uploading images to a flask python server

<strong>#1 Clone Repo:</strong><br />
<pre>git clone https://github.com/aretheregods/imageuploader.git
<br />
cd imageuploader</pre>

<strong>#2 Init and Start Virtual Environment:</strong><br />
<em>(If virtualenv isn't installed)</em><br />
<pre><em>pip install virtualenv</em></pre><br />
<pre>virtualenv --no-site-packages env</pre><br />
Windows CMD(Or Powershell): <pre>env/Scripts/activate</pre><br />
Windows Bash(Git Bash or MinGW): <pre>source env/Scripts/activate</pre><br />
OSX/Linux: <pre>source env/bin/activate</pre>

<strong>#3 Install Dependencies:</strong><br />
<pre>install  -r requirements.txt</pre>

<strong>#4 Edit database config:</strong><br />
Change app.py <pre>engine = engine.create_engine(<strong><em>your_database_address</em></strong>)</pre><br />
Change config.py['SQLALCHEMY_DATABASE_URI'] to your own credentials

<strong>#5 Create Database and table:</strong><br />
<pre>python app.py db init<br />
python app.py db migrate<br />
python app.py db upgrade</pre>

<strong>#6 Start the app:</strong><br />
<pre>python app.py runserver</pre>

<strong>#7 See the site at:</strong><br />
http://localhost:5000

<strong style="color:red">#<em>Just in case~</em>Delete mysql photos database:</strong><br />
In a terminal window -> <pre>mysql -u your_username -p</pre>
Put in your password when prompted<br />
<pre>-> USE photos;<br />
(If this database exists already, delete it)<br />
-> DROP DATABASE photos;<br />
(Go back to terminal with \q)<br />
-> \q</pre><br />
(Retry previous steps 5 - 7)
