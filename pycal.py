import sys
from ics import Calendar
import requests
from PySide2 import QtCore, QtGui, QtWidgets, QtDataVisualization

url = 'https://learningsuite.byu.edu/iCalFeed/ical.php?courseID=bgN1BtkiKZZg'

class Backend:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cal = Calendar(requests.get(url).text)
        self.classEvents = []
        self.assignments = []
        for event in list(self.cal.events):
            if event.name == event.description:
                self.classEvents.append(event)
            else:
                self.assignments.append(event)

class PyPlanner(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bend = Backend()
        self.combobox = QtWidgets.QComboBox()
        self.combobox.addItems([event.name for event in self.events])

        self.lwidget = QtWidgets.QListWidget()
        # self.lwidget.setSource()

        # self.model = QtDataVisualization.QStand
        self.mapper = QtWidgets.QDataWidgetMapper()

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.combobox)
        self.setLayout(self.layout)

if __name__ == "__main__":
    # app = QtWidgets.QApplication()
    
    # planner = PyPlanner()
    # planner.resize(800,600)
    # planner.show()

    # sys.exit(app.exec_())
    bend = Backend()
    print('Assignments:')
    for assignment in bend.assignments:
        print(assignment.name)

    print('Class Events:')
    for event in bend.classEvents:
        print(event.name)