# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'labassist.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(614, 441)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(9, 290, 293, 23))
        self.pushButton.setMinimumSize(QtCore.QSize(293, 23))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(308, 138, 70, 17))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSession = QtWidgets.QMenu(self.menubar)
        self.menuSession.setObjectName("menuSession")
        self.menuBachelors = QtWidgets.QMenu(self.menuSession)
        self.menuBachelors.setObjectName("menuBachelors")
        self.menuMasters = QtWidgets.QMenu(self.menuSession)
        self.menuMasters.setObjectName("menuMasters")
        self.menuThird_Semester = QtWidgets.QMenu(self.menuMasters)
        self.menuThird_Semester.setObjectName("menuThird_Semester")
        self.menuFourth_Semester = QtWidgets.QMenu(self.menuMasters)
        self.menuFourth_Semester.setObjectName("menuFourth_Semester")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionNew_Session = QtWidgets.QAction(MainWindow)
        self.actionNew_Session.setObjectName("actionNew_Session")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.actionCustom = QtWidgets.QAction(MainWindow)
        self.actionCustom.setObjectName("actionCustom")
        self.actionFirst_Year = QtWidgets.QAction(MainWindow)
        self.actionFirst_Year.setObjectName("actionFirst_Year")
        self.actionSecond_Year = QtWidgets.QAction(MainWindow)
        self.actionSecond_Year.setObjectName("actionSecond_Year")
        self.actionThird_Year = QtWidgets.QAction(MainWindow)
        self.actionThird_Year.setObjectName("actionThird_Year")
        self.actionFirst_Semester = QtWidgets.QAction(MainWindow)
        self.actionFirst_Semester.setObjectName("actionFirst_Semester")
        self.actionSecond_Semester = QtWidgets.QAction(MainWindow)
        self.actionSecond_Semester.setObjectName("actionSecond_Semester")
        self.actionCondensed_Matter = QtWidgets.QAction(MainWindow)
        self.actionCondensed_Matter.setObjectName("actionCondensed_Matter")
        self.actionParticle_and_Nuclear = QtWidgets.QAction(MainWindow)
        self.actionParticle_and_Nuclear.setObjectName("actionParticle_and_Nuclear")
        self.actionSolid_State = QtWidgets.QAction(MainWindow)
        self.actionSolid_State.setObjectName("actionSolid_State")
        self.actionMaterial_Physics = QtWidgets.QAction(MainWindow)
        self.actionMaterial_Physics.setObjectName("actionMaterial_Physics")
        self.actionLaser = QtWidgets.QAction(MainWindow)
        self.actionLaser.setObjectName("actionLaser")
        self.actionCondensed_Matter_2 = QtWidgets.QAction(MainWindow)
        self.actionCondensed_Matter_2.setObjectName("actionCondensed_Matter_2")
        self.actionParticle_and_Nuclear_2 = QtWidgets.QAction(MainWindow)
        self.actionParticle_and_Nuclear_2.setObjectName("actionParticle_and_Nuclear_2")
        self.actionSolid_State_2 = QtWidgets.QAction(MainWindow)
        self.actionSolid_State_2.setObjectName("actionSolid_State_2")
        self.actionLaser_2 = QtWidgets.QAction(MainWindow)
        self.actionLaser_2.setObjectName("actionLaser_2")
        self.actionLaser_3 = QtWidgets.QAction(MainWindow)
        self.actionLaser_3.setObjectName("actionLaser_3")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew_Session)
        self.menuFile.addAction(self.actionClose)
        self.menuView.addAction(self.actionNew)
        self.menuView.addAction(self.actionOpen_2)
        self.menuBachelors.addAction(self.actionFirst_Year)
        self.menuBachelors.addAction(self.actionSecond_Year)
        self.menuBachelors.addAction(self.actionThird_Year)
        self.menuThird_Semester.addAction(self.actionCondensed_Matter)
        self.menuThird_Semester.addAction(self.actionParticle_and_Nuclear)
        self.menuThird_Semester.addAction(self.actionSolid_State)
        self.menuThird_Semester.addAction(self.actionMaterial_Physics)
        self.menuThird_Semester.addAction(self.actionLaser)
        self.menuFourth_Semester.addAction(self.actionCondensed_Matter_2)
        self.menuFourth_Semester.addAction(self.actionParticle_and_Nuclear_2)
        self.menuFourth_Semester.addAction(self.actionSolid_State_2)
        self.menuFourth_Semester.addAction(self.actionLaser_2)
        self.menuFourth_Semester.addAction(self.actionLaser_3)
        self.menuMasters.addAction(self.actionFirst_Semester)
        self.menuMasters.addAction(self.actionSecond_Semester)
        self.menuMasters.addAction(self.menuThird_Semester.menuAction())
        self.menuMasters.addAction(self.menuFourth_Semester.menuAction())
        self.menuSession.addAction(self.menuBachelors.menuAction())
        self.menuSession.addAction(self.menuMasters.menuAction())
        self.menuSession.addSeparator()
        self.menuSession.addAction(self.actionCustom)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSession.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Load"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "Editor"))
        self.menuSession.setTitle(_translate("MainWindow", "Session"))
        self.menuBachelors.setTitle(_translate("MainWindow", "Bachelors"))
        self.menuMasters.setTitle(_translate("MainWindow", "Masters"))
        self.menuThird_Semester.setTitle(_translate("MainWindow", "Third Semester"))
        self.menuFourth_Semester.setTitle(_translate("MainWindow", "Fourth Semester"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionOpen.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Open"))
        self.actionSave_2.setText(_translate("MainWindow", "Save"))
        self.actionNew_Session.setText(_translate("MainWindow", "New Session"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen_2.setText(_translate("MainWindow", "Open"))
        self.actionCustom.setText(_translate("MainWindow", "Custom"))
        self.actionFirst_Year.setText(_translate("MainWindow", "First Year"))
        self.actionSecond_Year.setText(_translate("MainWindow", "Second Year"))
        self.actionThird_Year.setText(_translate("MainWindow", "Third Year"))
        self.actionFirst_Semester.setText(_translate("MainWindow", "First Semester"))
        self.actionSecond_Semester.setText(_translate("MainWindow", "Second Semester"))
        self.actionCondensed_Matter.setText(_translate("MainWindow", "Condensed Matter"))
        self.actionParticle_and_Nuclear.setText(_translate("MainWindow", "Particle and Nuclear"))
        self.actionSolid_State.setText(_translate("MainWindow", "Solid State"))
        self.actionMaterial_Physics.setText(_translate("MainWindow", "Material Physics"))
        self.actionLaser.setText(_translate("MainWindow", "Laser"))
        self.actionCondensed_Matter_2.setText(_translate("MainWindow", "Condensed Matter"))
        self.actionParticle_and_Nuclear_2.setText(_translate("MainWindow", "Particle and Nuclear"))
        self.actionSolid_State_2.setText(_translate("MainWindow", "Solid State "))
        self.actionLaser_2.setText(_translate("MainWindow", "Material Physics"))
        self.actionLaser_3.setText(_translate("MainWindow", "Laser"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
