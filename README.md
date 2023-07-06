# Server-Sent Events
This repo illustrates the use of [Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) (SSE) with a React.js frontend and a Flask-based python backend.

## Getting Started
1. Clone the repo
    ```sh
    git clone <this repository>
    ```

## Installation
### Backend
```sh
backend> python3 -m venv venv
backend> source venv/bin/activate
backend> pip install -r requirements.txt
backend> sh run.sh
```

### Test without a browser to make sure the backend is working
```sh
# Configure the server listening port
cp .env.example .env

# start a test SSE client
backend> python client.py 

# trigger a message to be sent to all listeners via SSE using curl or, optionally, the REST Client for Visual Studio Code (api.http file)

> curl http://localhost:5000/ping
```

[REST Client for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)

### Frontend

```sh
frontend> npm install
```

_Make sure the PORT value in `src/SSE.js` matches the Flask server port (default 5000)._

```
frontend> npm start
```

## Usage
Once the UI is started, trigger a message using the `curl` command or `api.http` file from before.

**If everything is working correctly, the word 'pong' should display on the UI after invoking  the backend with `curl`.**

### **Proxy cache issue**
If using webpack proxy as URL to backend there is an issue with proxy caching of stream responses:
https://github.com/facebook/create-react-app/issues/1633

_2 Options for solving this:_
* [disable caching in Flask](https://stackoverflow.com/questions/34066804/disabling-caching-in-flask)
* add CORS and don't proxy through webproxy and directly hit the Flask server from the UI in the `SSE.js` component.  _See `backend/app.py` for the CORS implementation._

