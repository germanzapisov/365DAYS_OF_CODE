from PyQt6.QtWidgets import (
    QApplication,
    QTabWidget,
    QWidget,
    QVBoxLayout
)

app = QApplication([])
window = QWidget()
window_main = QWidget()
window.setFixedSize(500, 500)

tabs = QTabWidget()
tab_one = QWidget()
tab_two = QWidget()

tabs.addTab(tab_one, 'reg')
tabs.addTab(tab_two, 'home')

layout = QVBoxLayout()
layout_main = QVBoxLayout()

tab_layout = QVBoxLayout()

tab_one.setLayout(tab_layout)
tab_two.setLayout(tab_layout)


layout.addWidget(tabs)



