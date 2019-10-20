from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import os
import sys

def isLinux():
    platform = sys.platform
    if platform == 'linux':
        return True
    return False

def runCmd(command):
    os.system(command)

def goto(folder):
    os.chdir(folder)

def runCmdGetOutput(command):
    return os.popen(command).read()

def isPathExists(path):
    return os.path.exists(path)

def newProjectButtonClicked():
    if isLinux():
        if isPathExists(App.pathProject):
            goto(App.pathProject)
            if App.selected_framework == 'Django':
                try:
                    version = runCmdGetOutput('django-admin --version')
                except Exception:
                    alertNoDjango = QMessageBox()
                    alertNoDjango.setText('There is no Django in your system ! \n We will install django for you !')
                    alertNoDjango.exec()
                    runCmd('pip install django')
                if not isPathExists(App.pathProject + '/' + App.selected_framework):
                    runCmd('mkdir ' + App.selected_framework)
                goto(App.pathProject + '/' + App.selected_framework)
                if " " in App.projectName:
                    alertProjectCase = QMessageBox()
                    alertProjectCase.setText('Project Name must not have space!')
                    alertProjectCase.exec()
                else:
                    if not isPathExists(App.pathProject + '/' + App.selected_framework + '/' + App.projectName):
                        runCmd('django-admin startproject ' + App.projectName)
                    else :
                        alertAlreadyCreated = QMessageBox()
                        alertAlreadyCreated.setText('You have already had project !')
                        alertAlreadyCreated.exec()
                    goto(App.pathProject + '/' + App.selected_framework + '/' + App.projectName)
                    runCmd('code .')
            else:
                alertFrameworkNotAvailable = QMessageBox()
                alertFrameworkNotAvailable.setText('Unsupported Framework')
                alertFrameworkNotAvailable.exec()
        else:
            alertPathProject = QMessageBox()
            alertPathProject.setText('No Directory in that path !')
            alertPathProject.exec()
    else:
        alertLinux = QMessageBox()
        alertLinux.setText('Not Available in Windows or MacOs')
        alertLinux.exec()

def openProjectButtonClicked():
    pass

def pathProjectEdit(text):
    App.pathProject = text

def projectNameEdit(text):
    App.projectName = text
class App(QWidget):
    pathProject = '/home/ahmad364/Documents'
    selected_framework = 'Django'
    list_framework = ['Django', 'Vue', 'Angular', 'React']
    projectName = 'portofolio'

    def __init__(self):
        super().__init__()
        self.title = 'Project Automation'
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        newProjectButton = QPushButton('Create New Project')
        openProjectButton = QPushButton('Open Project')
        pathProjectInput = QLineEdit(self.pathProject)
        projectNameInput = QLineEdit(self.projectName)
        frameworkInput = QComboBox()
        frameworkInput.addItems(self.list_framework)
        pathProjectInput.textChanged.connect(pathProjectEdit)
        projectNameInput.textChanged.connect(projectNameEdit)
        newProjectButton.clicked.connect(newProjectButtonClicked)
        openProjectButton.clicked.connect(openProjectButtonClicked)
        layout.addWidget(pathProjectInput)
        layout.addWidget(projectNameInput)
        layout.addWidget(frameworkInput)
        layout.addWidget(newProjectButton)
        layout.addWidget(openProjectButton)
        self.setLayout(layout)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())