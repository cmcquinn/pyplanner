"""View with three columns

Left box shows a list of tasks that can be moved to the middle box.
Middle box shows tasks in progress. Once they are checked, they get moved to done box.
"""

from PySide2.QtWidgets import QGridLayout, QApplication, QListWidget, QListWidgetItem
from PySide2.QtCore import Qt

class TaskLayout(QGridLayout):
    def __init__(self, parent):
        super().__init__(parent)
        