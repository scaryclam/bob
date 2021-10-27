DEBUG = False

# For example only
RABBITMQ = {
    'consumer': {
        'HOST': '127.0.0.1',
        'VHOST': '/',
        'USER': 'manager',
        'PASSWORD': 'vagrant',
        'EXCHANGE': 'bob',
        'QUEUE': 'job'
    },
    'publisher': {
        'HOST': '127.0.0.1',
        'VHOST': '/',
        'USER': 'manager',
        'PASSWORD': 'vagrant',
        'EXCHANGE': 'bob-jobs',
        'QUEUE': 'execute'
    }
}

DATABASES = {
    'default': {
        'name': 'manager',
        'user': 'vagrant',
        'password': 'vagrant',
        'host': '127.0.0.1',
        'port': 5432
    }
}
