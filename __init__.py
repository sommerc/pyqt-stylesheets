from pyqtcss import available_styles, get_style

if len(available_styles()) == 0:
    from setup import compile_css
    compile_css()