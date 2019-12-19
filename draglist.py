import sys

from PySide2.QtWidgets import QApplication, QListWidget, QListWidgetItem
from PySide2.QtCore import Qt

if __name__ == '__main__':
    app = QApplication(sys.argv)

    lw = QListWidget()
    for i in range(5):
        text = f'Item {i}'
        item = QListWidgetItem(text)
        item.setCheckState(Qt.Unchecked)
        lw.addItem(item)
    lw.setDragDropMode(lw.InternalMove)
    lw.show()
    sys.exit(app.exec_())