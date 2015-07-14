import os
import traceback
import importlib
import imp

from PyQt5.QtCore import QFile, QTextStream

version = 1.0

def available_styles():
    styles = [] 
    package_dir = os.path.dirname(os.path.abspath(__file__))
    for style_file in os.listdir(package_dir):
        if style_file.endswith(".py") and  not style_file.startswith("__"):
            style_module = os.path.splitext(style_file)[0]
            try:
                imp.find_module(style_module, [package_dir])
                is_ok = True
            except ImportError:
                is_ok = False
            if is_ok:
                styles.append(style_module)
                
    return styles        

def get_style(style_sheet):
    try:
        mod = importlib.import_module("." + style_sheet, __name__)
        hasattr(mod, "qt_resource_name")
        f = QFile(":/%s/style.qss" % style_sheet)                                
        f.open(QFile.ReadOnly | QFile.Text)
        ts = QTextStream(f)
        stylesheet = ts.readAll()    
    except ImportError as e:
        print "Style sheet not available. Use available_styles() to check for valid styles"
        return u""
    except Exception as e:
        print "Style sheet available, but an error occured..."
        traceback.print_exc()
        return u""
        
    return stylesheet
    
