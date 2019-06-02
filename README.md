# let's-chat
let's chat is a bi-directional chat application build with flask socket io.

## Steps to run this app.
- `apt-get install python3`
- `apt-get install python3-pip`
- `pip3 install -r requirements.txt`
- `gunicorn --worker-class eventlet app:app`

* Fire up your browser and navigate to `http://localhost:8000`.
* Open another browser window , try to enter the same room as different user and you will be able to chat with anyone who joins the room. 
