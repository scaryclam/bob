#!/usr/bin/env python

from viewer.application import application

# Flask doesn't handle setting host and port via SERVER_NAME well as it uses
# SERVER_NAME for other things
application.run(
    host=application.config['HOST'],
    port=application.config['PORT'])
