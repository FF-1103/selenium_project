import os
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))
path = os.path.dirname(os.path.dirname(__file__)) + '/screenshots'
print(path)