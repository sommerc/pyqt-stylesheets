import os
import sys
from setuptools import setup
import pyqtcss

__author__ = 'christoph.sommer@imba.oeaw.ac.at'

def compile_css():
    print 'Compiling resources...'
    css_root_path = os.path.dirname(__file__)
    css_src_path = os.path.join(css_root_path, 'pyqtcss/src')
    css_dest_poath = os.path.join(css_root_path, 'pyqtcss')
    for f in os.listdir(css_src_path):
        if os.path.isdir(os.path.join(css_src_path, f)):
            if os.path.exists(os.path.join(css_src_path, f, "style.qrc")):
                print(" * for PyQt5: pyrcc5 {1}/{0}/style.qrc -o pyqtcss/{0}.py".format(f, css_src_path))
                os.system("pyrcc5 {1}/{0}/style.qrc -o {2}/{0}.py".format(f, css_src_path, css_dest_poath))

if __name__ == "__main__":
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
