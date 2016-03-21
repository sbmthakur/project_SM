# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hospital.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import random
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

T = []
P = []
Q = []
R = []
S = []
U = []



class Ui_HospitalSimulator(object):
    def setupUi(self, HospitalSimulator):
        HospitalSimulator.setObjectName(_fromUtf8("HospitalSimulator"))
        HospitalSimulator.resize(722, 600)
        self.centralwidget = QtGui.QWidget(HospitalSimulator)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 681, 131))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 160, 131, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.download)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 220, 601, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 280, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 320, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 360, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 390, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20,250,601,25))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(300, 280, 41, 26))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget_2 = QtGui.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(290, 360, 41, 26))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.listWidget_3 = QtGui.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(290, 390, 41, 26))
        self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))
        self.listWidget_4 = QtGui.QListWidget(self.centralwidget)
        self.listWidget_4.setGeometry(QtCore.QRect(200, 320, 41, 26))
        self.listWidget_4.setObjectName(_fromUtf8("listWidget_4"))
        HospitalSimulator.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(HospitalSimulator)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        HospitalSimulator.setStatusBar(self.statusbar)

        self.retranslateUi(HospitalSimulator)
        QtCore.QMetaObject.connectSlotsByName(HospitalSimulator)

    def retranslateUi(self, HospitalSimulator):
        HospitalSimulator.setWindowTitle(_translate("HospitalSimulator", "HOSPITAL SIMULATOR", None))
        HospitalSimulator.setToolTip(_translate("HospitalSimulator", "HOSPITAL SIMULATION\n"
"", None))
        self.textBrowser.setHtml(_translate("HospitalSimulator", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">The purpose of this simulation is to decide how many operation theaters with doctors of different levels of expertise. Every ward has doctors with different level of expertise which affects the time of the operation. The simulation provides an idea about how the hospital will work.</span></p></body></html>", None))
        self.pushButton.setText(_translate("HospitalSimulator", "Simulate", None))
        self.label.setText(_translate("HospitalSimulator", "The simulate button starts generating random patients and calculating the amounts of time to be cured in each of the wards.", None))
        self.label_2.setText(_translate("HospitalSimulator", "The total delay suffered by the patients is:", None))
        self.label_3.setText(_translate("HospitalSimulator", "Average delay per patient:", None))
        self.label_4.setText(_translate("HospitalSimulator", "Total time of the patients in the hospital:", None))
        self.label_5.setText(_translate("HospitalSimulator", "Average time of patients in the hospital:", None))




        def generateTBA(rda):
                    if rda == 0:
                            return 4
                    
                    elif rda >= 1 and rda <= 25:
                        return 1
                    
                    elif rda >= 26 and rda <= 65:
                            return 2

                    elif rda >= 66 and rda <= 85:
                            return 3

                    else:
                            return 4

        def ward_1_service_time(rds):
                if rds == 0:
                        return 4
                
                elif rds >= 1 and rds <= 20:
                    return 4
                
                elif rds >= 21 and rds <= 45:
                        return 5

                elif rds >= 46 and rds <= 75:
                        return 3

                else:
                        return 6

        def ward_2_service_time(rds):
                if rds == 0:
                        return 5
                
                elif rds >= 1 and rds <= 30:
                    return 7
                
                elif rds >= 31 and rds <= 58:
                        return 6

                elif rds >= 59 and rds <= 83:
                        return 8

                else:
                        return 5

        def ward_3_service_time(rds):
                if rds == 0:
                        return 6
                
                elif rds >= 1 and rds <= 35:
                    return 7
                
                elif rds >= 36 and rds <= 60:
                        return 10

                elif rds >= 61 and rds <= 80:
                        return 8

                else:
                        return 9
        for i in range(1,101):
            rda = round(random.uniform(0,100))
            rds = round(random.uniform(0,100))
            x = generateTBA(rda)
            P.append(x)
            a= ward_1_service_time(rds)
            b= ward_2_service_time(rds)
            c= ward_3_service_time(rds)
            Q.append(a)
            R.append(b)
            S.append(c)    
    
    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.00005
            self.progressBar.setValue(self.completed)

        cta = 0
        

        ward_1_tsb = 0
        ward_1_st = Q[0]
        ward_1_tse = ward_1_tsb + ward_1_st
        ward_1_tst = ward_1_st



        ward_2_tse = -1
        ward_3_tse = -1

        ward_2_tst = 0
        ward_3_tst = 0

        total_time_queue = 0

        for i in range(len(P)-1):
                cta = cta + P[i]


                if cta >= ward_1_tse:
                        ward_1_tsb = cta
                        ward_1_st = Q[i]
                        ward_1_tse = ward_1_tsb + ward_1_st
                        ward_1_tst = ward_1_tst + ward_1_st

                else:
                        if cta >= ward_2_tse or ward_2_tse == -1:
                                ward_2_tsb = cta
                                ward_2_st = R[i]
                                ward_2_tse = ward_2_tsb + ward_2_st
                                ward_2_tst = ward_2_tst + ward_2_st
                        else:
                                if cta >= ward_3_tse or ward_3_tse == -1:
                                        ward_3_tsb = cta
                                        ward_3_st = S[i]
                                        ward_3_tse = ward_3_tsb + ward_3_st
                                        ward_3_tst = ward_3_tst + ward_3_st

                                else:
                                    w = min(ward_1_tse,ward_2_tse,ward_3_tse)
                        
                                    if w == ward_1_tse:
                                        total_time_queue = total_time_queue + ward_1_tse - cta 
                                        ward_1_tsb = ward_1_tse
                                        ward_1_st = Q[i]
                                        ward_1_tse = ward_1_tsb + ward_1_st
                                        ward_1_tst = ward_1_tst + ward_1_st

                                    elif w == ward_2_tse:
                                        total_time_queue = total_time_queue + ward_2_tse - cta
                                        ward_2_tsb = ward_2_tse
                                        ward_2_st = R[i]
                                        ward_2_tse = ward_2_tsb + ward_2_st
                                        ward_2_tst = ward_2_tst + ward_2_st

                                    else:
                                        total_time_queue = total_time_queue + ward_3_tse - cta
                                        ward_3_tsb = ward_3_tse
                                        ward_3_st = S[i]
                                        ward_3_tse = ward_3_tsb + ward_3_st
                                        ward_3_tst = ward_3_tst + ward_3_st


        total_time_system = ward_1_tst + ward_2_tst + ward_3_tst + total_time_queue
##        print(total_time_system)
        avg_time_system = total_time_system / 100
##        print(avg_time_system)
        avg_delay = total_time_queue / 100
##        print(avg_delay)
        self.listWidget.addItem(str(total_time_queue))
        self.listWidget_4.addItem(str(avg_delay))
        self.listWidget_2.addItem(str(total_time_system))
        self.listWidget_3.addItem(str(avg_time_system))
        
        
            
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HospitalSimulator = QtGui.QMainWindow()
    ui = Ui_HospitalSimulator()
    ui.setupUi(HospitalSimulator)
    HospitalSimulator.show()
    sys.exit(app.exec_())

