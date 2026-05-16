from PyQt6.QtWidgets import (QApplication,
                             QGridLayout,
                            QHBoxLayout,
                             QWidget)

app = QApplication([])
window = QWidget()
layout = QGridLayout()
switch_layout =  QHBoxLayout()

window.setLayout(layout)

layout.addLayout(switch_layout, 2, 0)
window.resize(500, 700)

