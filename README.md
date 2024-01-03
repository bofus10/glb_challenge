# glb_challenge

Simple python web app that displays notes taken from a DB and lets add more.

To test locally

```shell
#Make sure to have mysql client installed first

#Run a DB Locally (adjust parameters as needed)
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=abc123 -e MYSQL_DATABASE=notes -p 3306:3306 -d mysql:5.7

# Adjust parameters on app.py and run
pip3 install -r requirements.txt
python3 app.py

#Visit the app from browser
http://localhost:5000/
```