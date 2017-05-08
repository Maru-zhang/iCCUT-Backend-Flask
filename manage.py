# -*- coding: utf-8 -*-

from flask.ext.script import Manager, Server
from app import app

manager = Manager(app)
manager.add_command("runserver", 
        Server(host="127.0.0.1", port=5050, use_debugger=True))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5050)