import os

conf_module = os.environ.get('BOB_CONF', 'conf.local')

try:
    module = __import__(conf_module, globals(), locals(), ['*'])
except ImportError:
    print("Unable to import %s" % conf_module)
else:
    for k in dir(module):
        if not k.startswith("__"):
            locals()[k] = getattr(module, k)
