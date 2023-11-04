# Backend CS3560

1. `pipenv install` -- Run ONCE
2. `pipenv shell`-- Begin here if first command has already been used once
3. make a `.env` file and paste in the information i give

### Installing

[Documentation for installing dependencies through pipenv](https://stackoverflow.com/questions/46330327/how-are-pipfile-and-pipfile-lock-used)

1. `pipenv install [package-name]`

## using flask

make sure your virtual environment is activated
in terminal type `pipenv run flask run`
all flask envrionment variable is done on `.flaskenv` and should be committed whereas `.env` file shouldnt

# mysql setup

1. Download Mysql over here https://dev.mysql.com/downloads/installer/ ( i downloaded the file that was 331.3 M)

2. Do the setup and do the full download (spam next until you see the password portion)

3. Make sure you are not using the legacy version, select the 8.x version a. Make sure you remember your passwords and username(username is by default root)

4. Spam next until you finish and then you’re done Make sure you write the username and password in your.env file.
5. Open a terminal and make sure mysql is installed by typing in mysql -V a. If the command doesn’t work it may be because mysql isn’t added to your path. The default location for mysql server should be: C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe i. Possible solution: https://stackoverflow.com/questions/5920136/mysql-is-not-recognised-as-an-internal-or-external-command-operable-program-or-b

6. go into yoyur mysql workbench, click add mysql instance. Name it whatebver you want. Hostname should be local(or 127.0.0.1) and port could be whatever.

7. once that is done you can direct back to the backend run pipenv run app and your flask application should work
