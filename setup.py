import os
import sys
from setuptools import setup
import pyqtcss

__author__ = 'christoph.sommer@imba.oeaw.ac.at'

def compile_css():
    for f in os.listdir('pyqtcss/src/'):
        if os.path.isdir(os.path.join('pyqtcss/src/', f)):
            if os.path.exists(os.path.join('pyqtcss/src/', f, "style.qrc")):
                print(" * for PyQt5: pyrcc5 pyqtcss/src/{0}/style.qrc -o pyqtcss/{0}.py".format(f))
                os.system("pyrcc5 pyqtcss/src/{0}/style.qrc -o pyqtcss/{0}.py".format(f))

print 'Compiling resources...'
compile_css()

setup(name='pyqtcss',
      version = pyqtcss.version,
      description = 'PyQt5 style sheets',
      author = 'Christoph Sommer',
      author_email = 'christoph.sommer@imba.oeaw.ac.at',
      license = 'BSD',
      url = 'https://github.com/sommerc/pyqt-stylesheets',
      include_package_data=True,
      )
