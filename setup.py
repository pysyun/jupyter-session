from setuptools import setup

setup (
   name = 'jupyter_session',
   version = '1.0',
   scripts=['script/jupyter-session-folder.sh'],
   description = 'Syun\'s Jupyter Notebook extension for handling sessions.',
   author = 'Py Syun',
   author_email = 'pysyun@vitche.com',
   py_modules = ['jupyter.session'],
   install_requires = [],
   url='https://github.com/pysyun/jupyter-session'
)
