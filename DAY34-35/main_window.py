from PyQt6.QtWidgets import (
    QLabel
)
from utils import *



def open_main_window(username):

    window_main.setFixedSize(500, 500)

    window_main.show()
    main_text = QLabel(f"Welcome, {username}")

    layout_main.addWidget(main_text)