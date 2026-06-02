from PyQt6.QtWidgets import (
        QApplication,
        QLineEdit,
        QLabel,
        QWidget,
        QVBoxLayout,
        QPushButton
)
from PyQt6.QtCore import QTimer
from db import *


timer = QTimer()


def start_timer(success):
    timer.timeout.connect(success.hide)
    timer.start(2000)
    return timer


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

window.resize(500, 700)
window.setLayout(layout)
window.setStyleSheet("""
    background-color: black;
    color: white;
""")

text = QLabel("Viewer and adding information to the database")

container_create_table = QWidget()
layout_create_table = QVBoxLayout(container_create_table)

container_add_users = QWidget()
layout_add_users = QVBoxLayout(container_add_users)
widget_show_users = QWidget()
layout_show_users = QVBoxLayout(widget_show_users)

container_create_table.setStyleSheet("border: 2px solid white")
widget_show_users.setStyleSheet("border: 2px solid white")
container_add_users.setStyleSheet("border: 2px solid white")

table = QLineEdit()
name = QLineEdit()
family = QLineEdit()

table_name = QLabel("Enter table name")
button_create_table = QPushButton("Create")

add = QLabel("Add user")
button_add = QPushButton("Add")

show = QLabel("Show users")
button_show = QPushButton("Show")


def clicked():
    add_users(name.text(), family.text(), table.text())

def creation():
    creation_table(table.text())
    success = QLabel("Table created")
    layout_create_table.addWidget(success)
    success.show()
    start_timer(success)

def clicked_show():
        show_users(table.text())

button_create_table.clicked.connect(creation)
button_add.clicked.connect(clicked)
button_show.clicked.connect(clicked_show)


layout_create_table.addWidget(table_name)
layout_create_table.addWidget(table)
layout_create_table.addWidget(button_create_table)

layout_add_users.addWidget(add)
layout_add_users.addWidget(name)
layout_add_users.addWidget(family)
layout_add_users.addWidget(button_add)

layout_show_users.addWidget(show)
layout_show_users.addWidget(button_show)

container_create_table.resize(200,300)
widget_show_users.resize(200,300)
container_add_users.resize(200,300)

name.setPlaceholderText("Enter username")
family.setPlaceholderText("Enter username")
table.setPlaceholderText("Enter table name")
layout.addWidget(text)


layout.addWidget(container_create_table)
layout.addWidget(container_add_users)
layout.addWidget(widget_show_users)
window.show()
app.exec()