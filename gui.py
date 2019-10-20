from PyQt5.QtWidgets import *
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
        if isPathExists(pathProject):
            goto(pathProject)
            if framework == 'Django':
                try:
                    version = runCmdGetOutput('django-admin --version')
                except Exception:
                    alertNoDjango = QMessageBox()
                    alertNoDjango.setText('There is no Django in your system ! \n We will install django for you !')
                    alertNoDjango.exec()
                    runCmd('pip install django')
                if not isPathExists(pathProject + '/' + framework):
                    runCmd('mkdir ' + framework)
                goto(framework)
                if not isPathExists(pathProject + '/' + framework + '/' + projectName):
                    runCmd('django-admin startproject ' + projectName)
                else :
                    alertAlreadyCreated = QMessageBox()
                    alertAlreadyCreated.setText('You have already had project !')
                    alertAlreadyCreated.exec()
                goto(projectName)
                runCmd('code .')
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

def windows():
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    titleScreen = QLabel('Project Automation')
    pathProjectInput = QLineEdit(pathProject)
    newProjectButton = QPushButton('Create New Project')
    openProjectButton = QPushButton('Open Project')
    newProjectButton.clicked.connect(newProjectButtonClicked)
    openProjectButton.clicked.connect(openProjectButtonClicked)
    layout.addWidget(titleScreen)
    layout.addWidget(pathProjectInput)
    layout.addWidget(newProjectButton)
    layout.addWidget(openProjectButton)
    window.setLayout(layout)
    window.show()
    app.exec()

if __name__ == "__main__":
    pathProject = '/home/ahmad364/Documents'
    framework = 'Django'
    projectName = 'portofolio'
    windows()