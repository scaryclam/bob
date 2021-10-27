DEBUG = False

# For example only
RABBITMQ = {
    'consumer': {
        'HOST': '127.0.0.1',
        'VHOST': '/',
        'USER': 'manager',
        'PASSWORD': 'vagrant',
        'EXCHANGE': 'bob-jobs',
        'QUEUE': 'execute'
    },
    'publisher': {
        'HOST': '127.0.0.1',
        'VHOST': '/',
        'USER': 'manager',
        'PASSWORD': 'vagrant',
        'EXCHANGE': 'bob',
        'QUEUE': 'job'
    }
}
