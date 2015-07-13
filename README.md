# pyqt-stylesheets



## Installation
```
python setup.py build
python setup.py install
```
or
```
python setup.py sdist
pip install dist/pyqtcss-1.0.zip
```

## How to use

```
import pyqtcss

pyqtcss.available_styles()
    ['classic', 'dark_blue', 'dark_orange']
    
style_string = pyqtcss.get_style("dark_blue")
qt_widget.setStyleSheet(style_string)
```

## Extend
* create new folder in src. The folder name will be the name of the style
* create pyqt resource file `style.qrc` containing `style.qss` and other files such as icon pngs
* create pyqt resource file `style.qss`

The resource python file will be automatically generated

## Dependencies
PyQt5
