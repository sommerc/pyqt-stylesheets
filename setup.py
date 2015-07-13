import os

def compile_all():
    files = os.listdir('.')
    for f in files:
        if os.path.isdir(f) and os.path.exists(os.path.join(f, "style.qss")):
            print("Compiling for PyQt5: pyrcc5 %s/style.qrc -o ../%s.py" % (f,f))
            os.system("pyrcc5 %s/style.qrc -o ../%s.py" % (f,f))

__author__ = 'christoph.sommer@imba.oeaw.ac.at'

import sys

from distutils.core import setup
import pyqtcss

setup(name='pyqtcss',
      version = pyqtcss.version,
      description = 'PyQt5 style sheets',
      author = 'Christoph Sommer',
      author_email = 'christoph.sommer@imba.oeaw.ac.at',
      license = 'BSD',
      url = 'http://cellh5.org',
      package_dir = {'hmm_wrapper': 'pysrc/hmm_wrapper', '': 'pysrc'},
      py_modules = ['cellh5', 'cellh5write'],
      packages=['hmm_wrapper'],
      package_data={'hmm_wrapper': ['hmm_constraint.xsd']},
      )
