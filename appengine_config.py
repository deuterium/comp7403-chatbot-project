#https://cloud.google.com/appengine/docs/standard/python/tools/using-libraries-python-27
# appengine_config.py
from google.appengine.ext import vendor

# Add any libraries install in the "lib" folder.
vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))
