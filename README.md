# Vesuvius
run `pipenv shell`
then run `pipenv intall` 

#First time setup 
create instance/development.cfg

add to development.cfg

```
DEBUG=True

SQLALCHEMY_DATABASE_URI='sqlite://db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS=False
```
`flask run` 

close the server then run `flask create-all`

run `flask run` again

#For Linux and Mac 
run these commands every time a new terminal is opened

`export FLASK_APP=src`

`export FLASK_ENV=development`

`flask run`

#For Windows
run these commands every time a new terminal is opened

`set FLASK_APP=src`

`set FLASK_ENV=development`

`flask run`
