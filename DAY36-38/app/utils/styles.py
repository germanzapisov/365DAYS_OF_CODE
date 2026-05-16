def apply_styles_page_one(logo, window, light_swither, dark_swither, text, button, success, chat):
    logo.setStyleSheet(
        """
        background-color: transparent;
    """
    )

    window.setStyleSheet(
        """
        font-family: Helvetica;
        background: qlineargradient(
            x1:0, y1:0,
            x2:1, y2:1,
            stop:0 #eef9ff,
            stop:0.35 #cfeeff,
            stop:0.7 #9fddff,
            stop:1 #63c7ff
        );
        
        margin: 0px;
        padding: 0px;
    """
    )

    light_swither.setStyleSheet(
        """
        background-color: rgba(40, 90, 140, 220);
        border-radius: 10px;
        color: white;
    """
    )

    dark_swither.setStyleSheet(
        """
        background-color: rgba(40, 90, 140, 220);
        color: white;
        border-radius: 10px;
    """
    )

    text.setStyleSheet(
        """
    background-color: rgba(40, 90, 140, 220);
    padding: 10 25px;
    border: 5px solid rgba(40, 90, 140, 220);
    """
    )

    button.setStyleSheet(
        """
    background-color: rgba(40, 90, 140, 220);
    border: 5px solid rgba(40, 90, 140, 220);
    padding: 10 25;
    font-size: 18px;
    """
    )

    success.setStyleSheet(
        """
    background: transparent;
    font-size: 20px;
    border: none;
    """
    )

    chat.setStyleSheet(
        """
                  padding: 10 10;
                  border: 5px solid  rgba(100, 190, 255, 180);
                  font-size: 22px;
                  background-color: rgba(40, 90, 140, 220);
              """
    )

def apply_dark_theme(window):
    window.setStyleSheet(
        """
                font-family: Helvetica;
                background-color: #0B1120;
                margin: 0px;
                padding: 0px;
            """
    )

def style_for_messages(label):
    label.setStyleSheet("""
        background-color: white;
        font-size: 18px;
        color: rgba(0, 122, 255, 0.9);
        border: none;
        border-radius: 25px;
        """)