from PyQt6.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,

)
from utils import *
from main_window import open_main_window



window.setLayout(layout)
window.setWindowTitle("Gerkaa")
logo_text = QLabel("Gerkaaa messenger")

input_name = QLineEdit()
input_lastname = QLineEdit()
input_error = QLabel("input the name!")
button = QPushButton("send...")

layout.addWidget(logo_text)
layout.addWidget(input_name)
layout.addWidget(input_lastname)
layout.addWidget(button)



def button_clicked():
    if input_name.text():
        window.hide()
        open_main_window(input_name.text())
        apply_styles_page_two(window_main)
    else:
        layout.addWidget(input_error)



input_name.setPlaceholderText('Input the name')
input_lastname.setPlaceholderText('Input the lastname')
button.clicked.connect(button_clicked)



apply_styles_page_one(window, logo_text, input_name, input_lastname, button)
window.show()
app.exec()
