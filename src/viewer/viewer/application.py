from flask import Flask

from viewer import settings
from viewer.urls import create_routes


application = Flask(__name__)
application.config.from_object('viewer.settings')

host = settings.HOST
port = settings.PORT

create_routes(application)


if __name__ == '__main__':
    application.run()
