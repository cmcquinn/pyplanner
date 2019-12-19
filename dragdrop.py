import sys
from PySide2 import QtWidgets, QtCore, QtGui

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PySide2 drag and drop - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 60
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.list1 = QtWidgets.QListWidget()
        self.list2 = QtWidgets.QListWidget()

        for i in range(5):
            text = f'Item {i}'
            item = QtWidgets.QListWidgetItem(text)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.list1.addItem(item)

        self.list1.setDragDropMode(QtCore.drag)
        
        taskObj = QtWidgets.QCheckBox('Drag this', self)
        
        taskObj.move(10, 10)
        taskObj.resize(100,32)
        
        button = CustomLabel('Drop here.', self)
        button.move(130,15)
        
        self.show()
    
    @Slot()
    def on_click(self):
        print('PySide2 button click')
    
class CustomLabel(QLabel):
    
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
    
    def dropEvent(self, e):
        self.setText(e.mimeData().text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
