
def apply_styles_page_one(window, logo_text, input_name, input_lastname, button):
    window.setStyleSheet("""
        background-color: rgba(80, 180, 255, 200);
    """)

    logo_text.setStyleSheet("""
        font-size: 40px;
    
    """)

    input_name.setStyleSheet("""
        padding: 17px 30px;
        background-color: rgba(40, 90, 140, 220);
        border: none;
    """)

    input_lastname.setStyleSheet("""
        padding: 17px 30px;
        background-color: rgba(40, 90, 140, 220);
        border: none;
    """)

    button.setStyleSheet("""
        background-color: rgba(25, 60, 110, 230);
        color: white;
        border-radius: 40px;
        border: none;
        padding: 15px 30px;
    """)

def apply_styles_page_two(window_main):
    window_main.setStyleSheet("""
        background-color: rgba(80, 180, 255, 200);
    """)