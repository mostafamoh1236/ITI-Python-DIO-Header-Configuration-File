# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DIO_Config.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, SIGNAL)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2 import QtWidgets
from PySide2.QtWidgets import *

import sys
import os


def QString():
  str()
  return
  
DDRA = [0,0,0,0,0,0,0,0]
DDRB = [0,0,0,0,0,0,0,0]
DDRC = [0,0,0,0,0,0,0,0]
DDRD = [0,0,0,0,0,0,0,0]

PORTA = [0,0,0,0,0,0,0,0]
PORTB = [0,0,0,0,0,0,0,0]
PORTC = [0,0,0,0,0,0,0,0]
PORTD = [0,0,0,0,0,0,0,0]



class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(566, 392)
        self.OutputPath_LineEdit = QLineEdit(Form)
        self.OutputPath_LineEdit.setObjectName(u"OutputPath_LineEdit")
        self.OutputPath_LineEdit.setGeometry(QRect(20, 350, 301, 20))
        self.Generate_pushButton = QPushButton(Form)
        self.Generate_pushButton.setObjectName(u"Generate_pushButton")
        self.Generate_pushButton.setGeometry(QRect(360, 350, 75, 23))
        self.PinConfig_groupBox = QGroupBox(Form)
        self.PinConfig_groupBox.setObjectName(u"PinConfig_groupBox")
        self.PinConfig_groupBox.setEnabled(True)
        self.PinConfig_groupBox.setGeometry(QRect(10, 10, 551, 271))
        self.Mode_groupBox = QGroupBox(self.PinConfig_groupBox)
        self.Mode_groupBox.setObjectName(u"Mode_groupBox")
        self.Mode_groupBox.setGeometry(QRect(10, 100, 91, 111))
        self.Output_radioButton = QRadioButton(self.Mode_groupBox)
        self.Output_radioButton.setObjectName(u"Output_radioButton")
        self.Output_radioButton.setGeometry(QRect(10, 30, 83, 18))
        self.Input_radioButton = QRadioButton(self.Mode_groupBox)
        self.Input_radioButton.setObjectName(u"Input_radioButton")
        self.Input_radioButton.setGeometry(QRect(10, 70, 83, 18))
        self.Input_radioButton.setChecked(True)
        self.OutputConfig_groupBox = QGroupBox(self.PinConfig_groupBox)
        self.OutputConfig_groupBox.setObjectName(u"OutputConfig_groupBox")
        self.OutputConfig_groupBox.setEnabled(False)
        self.OutputConfig_groupBox.setGeometry(QRect(120, 110, 281, 41))
        self.OutputConfig_groupBox.setFlat(False)
        self.OutputConfig_groupBox.setCheckable(False)
        self.High__radioButton = QRadioButton(self.OutputConfig_groupBox)
        self.High__radioButton.setObjectName(u"High__radioButton")
        self.High__radioButton.setGeometry(QRect(20, 20, 83, 18))
        self.Low_radioButton = QRadioButton(self.OutputConfig_groupBox)
        self.Low_radioButton.setObjectName(u"Low_radioButton")
        self.Low_radioButton.setGeometry(QRect(130, 20, 83, 18))
        self.Low_radioButton.setChecked(True)
        self.InputConfig_groupBox = QGroupBox(self.PinConfig_groupBox)
        self.InputConfig_groupBox.setObjectName(u"InputConfig_groupBox")
        self.InputConfig_groupBox.setGeometry(QRect(120, 160, 281, 41))
        self.PullUP_radioButton = QRadioButton(self.InputConfig_groupBox)
        self.PullUP_radioButton.setObjectName(u"PullUP_radioButton")
        self.PullUP_radioButton.setGeometry(QRect(20, 20, 83, 18))
        self.HighImp_radioButton = QRadioButton(self.InputConfig_groupBox)
        self.HighImp_radioButton.setObjectName(u"HighImp_radioButton")
        self.HighImp_radioButton.setGeometry(QRect(130, 20, 111, 18))
        self.HighImp_radioButton.setChecked(True)
        self.PinName_LineEdit = QLineEdit(self.PinConfig_groupBox)
        self.PinName_LineEdit.setObjectName(u"PinName_LineEdit")
        self.PinName_LineEdit.setEnabled(False)
        self.PinName_LineEdit.setGeometry(QRect(20, 230, 151, 21))
        self.DefaultName_checkBox = QCheckBox(self.PinConfig_groupBox)
        self.DefaultName_checkBox.setObjectName(u"DefaultName_checkBox")
        self.DefaultName_checkBox.setGeometry(QRect(240, 230, 111, 18))
        self.DefaultName_checkBox.setChecked(True)
        self.PinNum_comboBox = QComboBox(self.PinConfig_groupBox)
        self.PinNum_comboBox.addItem(QString())
        self.PinNum_comboBox.addItem(QString())
        self.PinNum_comboBox.addItem(QString())
        self.PinNum_comboBox.addItem(QString())
        self.PinNum_comboBox.addItem(QString())
        self.PinNum_comboBox.addItem(QString())
        self.PinNum_comboBox.addItem(QString())
        self.PinNum_comboBox.addItem(QString())
        self.PinNum_comboBox.setObjectName(u"PinNum_comboBox")
        self.PinNum_comboBox.setGeometry(QRect(20, 60, 91, 22))
        self.PinNum_comboBox.setEditable(True)
        self.tabWidget = QTabWidget(self.PinConfig_groupBox)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 20, 571, 21))
        self.PORTA_tab = QWidget()
        self.PORTA_tab.setObjectName(u"PORTA_tab")
        self.tabWidget.addTab(self.PORTA_tab, QString())
        self.PORTB_tab = QWidget()
        self.PORTB_tab.setObjectName(u"PORTB_tab")
        self.tabWidget.addTab(self.PORTB_tab, QString())
        self.PORTC_tab = QWidget()
        self.PORTC_tab.setObjectName(u"PORTC_tab")
        self.tabWidget.addTab(self.PORTC_tab, QString())
        self.PORTD_tab = QWidget()
        self.PORTD_tab.setObjectName(u"PORTD_tab")
        self.tabWidget.addTab(self.PORTD_tab, QString())
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 300, 75, 23))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 300, 75, 23))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(220, 300, 75, 23))

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Form)
    # setupUi
    
##connections here
        QObject.connect(self.Input_radioButton,SIGNAL("clicked(bool)"),self.InputConfig_groupBox.setEnabled)
        QObject.connect(self.Input_radioButton,SIGNAL("clicked(bool)"),self.OutputConfig_groupBox.setDisabled)
        QObject.connect(self.Input_radioButton,SIGNAL("clicked(bool)"),self.Update_Port_Status)
        QObject.connect(self.Output_radioButton,SIGNAL("clicked(bool)"),self.OutputConfig_groupBox.setEnabled)
        QObject.connect(self.Output_radioButton,SIGNAL("clicked(bool)"),self.InputConfig_groupBox.setDisabled)
        QObject.connect(self.Output_radioButton,SIGNAL("clicked(bool)"),self.Update_Port_Status)
        QObject.connect(self.DefaultName_checkBox,SIGNAL("clicked(bool)"),self.PinName_LineEdit.setDisabled)
        QObject.connect(self.High__radioButton,SIGNAL("clicked(bool)"),self.Update_Port_Status)
        QObject.connect(self.Low_radioButton,SIGNAL("clicked(bool)"),self.Update_Port_Status)
        QObject.connect(self.HighImp_radioButton,SIGNAL("clicked(bool)"),self.Update_Port_Status)
        QObject.connect(self.PullUP_radioButton,SIGNAL("clicked(bool)"),self.Update_Port_Status)
        
        

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def Update_Port_Status(self):
      if self.tabWidget.currentIndex() == self.PORTA_tab:
        if self.Output_radioButton.isChecked():
          DDRA[self.PinNum_comboBox.currentIndex] = 1
          if self.High__radioButton.isChecked():
            PORTA[self.PinNum_comboBox.currentIndex] = 1
          elif self.Low_radioButton.isChecked():
            PORTA[self.PinNum_comboBox.currentIndex] = 0
        elif self.Input_radioButton.isChecked():
          DDRA[self.PinNum_comboBox.currentIndex] = 0
          if self.HighImp_radioButton.isChecked():
            PORTA[self.PinNum_comboBox.currentIndex] = 0
          elif self.PullUP_radioButton.isChecked():
            PORTA[self.PinNum_comboBox.currentIndex] = 1
            ######################
      elif self.tabWidget.currentIndex() == self.PORTB_tab:
        if self.Output_radioButton.isChecked():
          DDRB[self.PinNum_comboBox.currentIndex] = 1
          if self.High__radioButton.isChecked():
            PORTB[self.PinNum_comboBox.currentIndex] = 1
          elif self.Low_radioButton.isChecked():
            PORTB[self.PinNum_comboBox.currentIndex] = 0
        elif self.Input_radioButton.isChecked():
          DDRB[self.PinNum_comboBox.currentIndex] = 0
          if self.HighImp_radioButton.isChecked():
            PORTB[self.PinNum_comboBox.currentIndex] = 0
          elif self.PullUP_radioButton.isChecked():
            PORTB[self.PinNum_comboBox.currentIndex] = 1
      #######################################      
      elif self.tabWidget.currentIndex() == self.PORTC_tab:
        if self.Output_radioButton.isChecked():
          DDRC[self.PinNum_comboBox.currentIndex] = 1
          if self.High__radioButton.isChecked():
            PORTC[self.PinNum_comboBox.currentIndex] = 1
          elif self.Low_radioButton.isChecked():
            PORTC[self.PinNum_comboBox.currentIndex] = 0
        elif self.Input_radioButton.isChecked():
          DDRC[self.PinNum_comboBox.currentIndex] = 0
          if self.HighImp_radioButton.isChecked():
            PORTC[self.PinNum_comboBox.currentIndex] = 0
          elif self.PullUP_radioButton.isChecked():
            PORTC[self.PinNum_comboBox.currentIndex] = 1
            ##############################
      elif self.tabWidget.currentIndex() == self.PORTD_tab:
        if self.Output_radioButton.isChecked():
          DDRD[self.PinNum_comboBox.currentIndex] = 1
          if self.High__radioButton.isChecked():
            PORTD[self.PinNum_comboBox.currentIndex] = 1
          elif self.Low_radioButton.isChecked():
            PORTD[self.PinNum_comboBox.currentIndex] = 0
        elif self.Input_radioButton.isChecked():
          DDRD[self.PinNum_comboBox.currentIndex] = 0
          if self.HighImp_radioButton.isChecked():
            PORTD[self.PinNum_comboBox.currentIndex] = 0
          elif self.PullUP_radioButton.isChecked():
            PORTD[self.PinNum_comboBox.currentIndex] = 1
    def Switch_index(self):
      index = self.PinNum_comboBox.currentIndex()
      if index == 0:
        self.PinConfig_groupBox.setTitle(QCoreApplication,translate("Form",u"Pin 0 Configuration",None))
      elif index == 1:
        self.PinConfig_groupBox.setTitle(QCoreApplication,translate("Form",u"Pin 1 Configuration",None))
      elif index == 2:
        self.PinConfig_groupBox.setTitle(QCoreApplication,translate("Form",u"Pin 2 Configuration",None))
      elif index == 3:
        self.PinConfig_groupBox.setTitle(QCoreApplication,translate("Form",u"Pin 3 Configuration",None))
      elif index == 4:
        self.PinConfig_groupBox.setTitle(QCoreApplication,translate("Form",u"Pin 4 Configuration",None))
      elif index == 5:
        self.PinConfig_groupBox.setTitle(QCoreApplication,translate("Form",u"Pin 5 Configuration",None))
      elif index == 6:
        self.PinConfig_groupBox.setTitle(QCoreApplication,translate("Form",u"Pin 6 Configuration",None))
      elif index == 7:
        self.PinConfig_groupBox.setTitle(QCoreApplication,translate("Form",u"Pin 7 Configuration",None))
      else:
        None
      self.Update_Config()


    def Generate_Function(self):
      if(os.path.isdir(self.OutputPath_LineEdit.text()) == False):
        ErrorBox = QtWidgets.QErrorMessage()
        ErrorBox.showMessage("This Directory doesn't exist")
        ErrorBox.exec_()
      else:
        DIO_Handler=open(self.OutputPath_lineEdit.text()+r'\PORT_config.h','w')
        DIO_Handler.write ("#define INPUT 0 \n")
        DIO_Handler.write ("#define OUTPUT 1\n")
        DIO_Handler.write ("/* input=0, output=1*/ \n")
        for number in range(8):
          if DDRA[number]==0:
            DIO_Handler.write("#define PORT_U8_PORTA_PIN"+str(i)+"_DIR	INPUT\n")
          elif DDRA[number]==1:
            DIO_Handler.write("#define PORT_U8_PORTA_PIN"+str(i)+"_DIR	OUTPUT\n")
        for number in range(8):
          if DDRB[number]==0:
            DIO_Handler.write("#define PORT_U8_PORTB_PIN"+str(i)+"_DIR	INPUT\n")
          elif DDRB[number]==1:
            DIO_Handler.write("#define PORT_U8_PORTB_PIN"+str(i)+"_DIR	OUTPUT\n")
        for number in range(8):
          if DDRC[number]==0:
            DIO_Handler.write("#define PORT_U8_PORTC_PIN"+str(i)+"_DIR	INPUT\n")
          elif DDRC[number]==1:
            DIO_Handler.write("#define PORT_U8_PORTC_PIN"+str(i)+"_DIR	OUTPUT\n")
        for number in range(8):
          if DDRD[number]==0:
            DIO_Handler.write("#define PORT_U8_PORTD_PIN"+str(i)+"_DIR	INPUT\n")
          elif DDRD[number]==1:
            DIO_Handler.write("#define PORT_U8_PORTD_PIN"+str(i)+"_DIR	OUTPUT\n")
        
        DIO_Handler.write("/**************************************************/\n")
        DIO_Handler.write("#define LOW 0\n")
        DIO_Handler.write("#define HIGH 1\n")
        DIO_Handler.write("/*choose initial value for pins\n")
        DIO_Handler.write(" * 0:Low for output,floating for input\n")
        DIO_Handler.write(" * 1:high for output, internal pull up for input*/\n")
        
        for number in range(8):
            if PORTA[number]==0:
                DIO_Handler.write("#define PORT_U8_PORTA_PIN"+str(i)+"_INITIAL_VALUE	LOW\n")
            elif PORTA [number]==1:
                DIO_Handler.write("#define PORT_U8_PORTA_PIN"+str(i)+"_INITIAL_VALUE	HIGH\n")
        for i in range(8):
            if PORTB[number]==0:
               DIO_Handler.write("#define PORT_U8_PORTB_PIN"+str(i)+"_INITIAL_VALUE	LOW\n")
            elif PORTB [number]==1:
                DIO_Handler.write("#define PORT_U8_PORTB_PIN"+str(i)+"_INITIAL_VALUE	HIGH\n")        
        for i in range(8):
            if PORTC[number]==0:
                DIO_Handler.write("#define PORT_U8_PORTC_PIN"+str(i)+"_INITIAL_VALUE	LOW\n")
            elif PORTC [number]==1:
                DIO_Handler.write("#define PORT_U8_PORTC_PIN"+str(i)+"_INITIAL_VALUE	HIGH\n")
        for i in range(8):
            if PORTD[number]==0:
                DIO_Handler.write("#define PORT_U8_PORTD_PIN"+str(i)+"_INITIAL_VALUE	LOW\n")
            elif PORTD [number]==1:
                DIO_Handler.write("#define PORT_U8_PORTD_PIN"+str(i)+"_INITIAL_VALUE	HIGH\n")                
        DIO_Handler.close()
        print ("done")
    def Browse_Function(self):
      print("Choose Location")
      dialog=QFileDialog()
      path=dialog.getExistingDirectory(None,"Select Folder")
      self.OutputPath_lineEdit.setText(QCoreApplication.translate("Form", path, None))
      return
    def Update_Config(self):
      if DDRA[self.PinNum_comboBox.currentIndex()]==1:
        self.Output_radioButton.setChecked(True)
        self.OutputConfig_groupBox.setEnabled(True)
        self.InputConfig_groupBox.setDisabled(True)
        if PORTA[self.PinNum_comboBox.currentIndex()] == 1:
          self.High__radioButton.setChecked(True)
        elif PORTA[self.PinNum_comboBox.currentIndex()] == 0:
          self.Low_radioButton.setChecked(True)
      elif DDRA[self.PinNum_comboBox.currentIndex()] == 0:
        self.Input_radioButton.setChecked(True)
        self.InputConfig_groupBox.setEnabled(True)
        self.OutputConfig_groupBox.setDisabled(True)
        if PORTA[self.PinNum_comboBox.currentIndex()] == 1:
          self.PullUP_radioButton.setChecked(True)
        elif PORTA[self.PinNum_comboBox.currentIndex()] == 0:
          self.HighImp_radioButton.setChecked(True)
      if DDRB[self.PinNum_comboBox.currentIndex()]==1:
        self.Output_radioButton.setChecked(True)
        self.OutputConfig_groupBox.setEnabled(True)
        self.InputConfig_groupBox.setDisabled(True)
        if PORTB[self.PinNum_comboBox.currentIndex()] == 1:
          self.High__radioButton.setChecked(True)
        elif PORTB[self.PinNum_comboBox.currentIndex()] == 0:
          self.Low_radioButton.setChecked(True)
      elif DDRB[self.PinNum_comboBox.currentIndex()] == 0:
        self.Input_radioButton.setChecked(True)
        self.InputConfig_groupBox.setEnabled(True)
        self.OutputConfig_groupBox.setDisabled(True)
        if PORTB[self.PinNum_comboBox.currentIndex()] == 1:
          self.PullUP_radioButton.setChecked(True)
        elif PORTB[self.PinNum_comboBox.currentIndex()] == 0:
          self.HighImp_radioButton.setChecked(True)
      if DDRC[self.PinNum_comboBox.currentIndex()]==1:
        self.Output_radioButton.setChecked(True)
        self.OutputConfig_groupBox.setEnabled(True)
        self.InputConfig_groupBox.setDisabled(True)
        if PORTC[self.PinNum_comboBox.currentIndex()] == 1:
          self.High__radioButton.setChecked(True)
        elif PORTC[self.PinNum_comboBox.currentIndex()] == 0:
          self.Low_radioButton.setChecked(True)
      elif DDRC[self.PinNum_comboBox.currentIndex()] == 0:
        self.Input_radioButton.setChecked(True)
        self.InputConfig_groupBox.setEnabled(True)
        self.OutputConfig_groupBox.setDisabled(True)
        if PORTC[self.PinNum_comboBox.currentIndex()] == 1:
          self.PullUP_radioButton.setChecked(True)
        elif PORTC[self.PinNum_comboBox.currentIndex()] == 0:
          self.HighImp_radioButton.setChecked(True)
      if DDRD[self.PinNum_comboBox.currentIndex()]==1:
        self.Output_radioButton.setChecked(True)
        self.OutputConfig_groupBox.setEnabled(True)
        self.InputConfig_groupBox.setDisabled(True)
        if PORTD[self.PinNum_comboBox.currentIndex()] == 1:
          self.High__radioButton.setChecked(True)
        elif PORTD[self.PinNum_comboBox.currentIndex()] == 0:
          self.Low_radioButton.setChecked(True)
      elif DDRD[self.PinNum_comboBox.currentIndex()] == 0:
        self.Input_radioButton.setChecked(True)
        self.InputConfig_groupBox.setEnabled(True)
        self.OutputConfig_groupBox.setDisabled(True)
        if PORTD[self.PinNum_comboBox.currentIndex()] == 1:
          self.PullUP_radioButton.setChecked(True)
        elif PORTD[self.PinNum_comboBox.currentIndex()] == 0:
          self.HighImp_radioButton.setChecked(True)
    def New_Tab_Function(self):
    
      for elements in range(8):
        DDRA[elements] = 0
      for elements in range(8):
        DDRB[elements] = 0
      for elements in range(8):
        DDRC[elements] = 0
      for elements in range(8):
        DDRD[elements] = 0
      for elements in range(8):
        PORTA[elements] = 0
      for elements in range(8):
        PORTB[elements] = 0
      for elements in range(8):
        PORTC[elements] = 0
      for elements in range(8):
        PORTD[elements] = 0
      
      self.Update_Config()
      return

    def Save_Tab_Function(self):
      if(os.path.isdir(self.OutputPath_LineEdit.text()) == False):
        ErrorBox = QtWidgets.QErrorMessage()
        ErrorBox.showMessage("This Directory doesn't exist")
        ErrorBox.exec_()
      else:
        Config_Handler = open(self.OutputPath_LineEdit.text()+r'\Configuration.txt','w')
        for element in DDRA:
          Config_Handler.write(str(element)+" ")
        Config_Handler.write("\n")
        for element in DDRB:
          Config_Handler.write(str(element)+" ")
        Config_Handler.write("\n")
        for element in DDRC:
          Config_Handler.write(str(element)+" ")
        Config_Handler.write("\n")
        for element in DDRD:
          Config_Handler.write(str(element)+" ")
        Config_Handler.write("\n")
        for element in PORTA:
          Config_Handler.write(str(element)+" ")
        Config_Handler.write("\n")
        for element in PORTB:
          Config_Handler.write(str(element)+" ")
        Config_Handler.write("\n")
        for element in PORTC:
          Config_Handler.write(str(element)+" ")
        Config_Handler.write("\n")
        for element in PORTD:
          Config_Handler.write(str(element)+" ")
        Config_Handler.write("\n")
        
        Config_Handler.close()
        self.Update_Config()
        return

    def Load_Tab_Function(self):
      if(os.path.isfile(self.OutputPath_LineEdit.text()+r'\configuration.txt') == False):
        ErrorBox = QtWidgets.QErrorMessage()
        ErrorBox.showMessage("The configuration file doesn't exist")
        ErrorBox.exec_()
      else:
        Config_Handler = open(self.OutputPath_LineEdit.text()+r'\Configuration.txt','r')
        line = Config_Handler.readline()
        Line_Array= line.split()
        for elements in range(8):
          DDRA[elements] = int(Line_Array[elements])
        line = Config_Handler.readline()
        Line_Array= line.split()
        for elements in range(8):
          DDRB[elements] = int(Line_Array[elements])
    
        line = Config_Handler.readline()
        Line_Array= line.split()
        for elements in range(8):
          DDRC[elements] = int(Line_Array[elements])
    
        line = Config_Handler.readline()
        Line_Array= line.split()
        for elements in range(8):
          DDRD[elements] = int(Line_Array[elements])
    
        line = Config_Handler.readline()
        Line_Array= line.split()
        for elements in range(8):
          PORTA[elements] = int(Line_Array[elements])
    
        line = Config_Handler.readline()
        Line_Array= line.split()
        for elements in range(8):
          PORTB[elements] = int(Line_Array[elements])
    
        line = Config_Handler.readline()
        Line_Array= line.split()
        for elements in range(8):
          PORTC[elements] = int(Line_Array[elements])
    
        line = Config_Handler.readline()
        Line_Array= line.split()
        for elements in range(8):
          PORTD[elements] = int(Line_Array[elements])
          
        Config_Handler.close()
        self.Update_Config()
        return




    

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.OutputPath_LineEdit.setText(QCoreApplication.translate("Form", u"Enter Output Path", None))
        self.Generate_pushButton.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.PinConfig_groupBox.setTitle(QCoreApplication.translate("Form", u"Pin Configuration", None))
        self.Mode_groupBox.setTitle(QCoreApplication.translate("Form", u"Mode", None))
        self.Output_radioButton.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input_radioButton.setText(QCoreApplication.translate("Form", u"Input", None))
        self.OutputConfig_groupBox.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.High__radioButton.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low_radioButton.setText(QCoreApplication.translate("Form", u"Low", None))
        self.InputConfig_groupBox.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PullUP_radioButton.setText(QCoreApplication.translate("Form", u"Pull-Up", None))
        self.HighImp_radioButton.setText(QCoreApplication.translate("Form", u"High Impedence", None))
        self.PinName_LineEdit.setText(QCoreApplication.translate("Form", u"Enter Pin Name", None))
        self.DefaultName_checkBox.setText(QCoreApplication.translate("Form", u"Use Default Name", None))
        self.PinNum_comboBox.setItemText(0, QCoreApplication.translate("Form", u"Pin 0", None))
        self.PinNum_comboBox.setItemText(1, QCoreApplication.translate("Form", u"Pin 1", None))
        self.PinNum_comboBox.setItemText(2, QCoreApplication.translate("Form", u"Pin 2", None))
        self.PinNum_comboBox.setItemText(3, QCoreApplication.translate("Form", u"Pin 3", None))
        self.PinNum_comboBox.setItemText(4, QCoreApplication.translate("Form", u"Pin 4", None))
        self.PinNum_comboBox.setItemText(5, QCoreApplication.translate("Form", u"Pin 5", None))
        self.PinNum_comboBox.setItemText(6, QCoreApplication.translate("Form", u"Pin 6", None))
        self.PinNum_comboBox.setItemText(7, QCoreApplication.translate("Form", u"Pin 7", None))

        self.PinNum_comboBox.setCurrentText(QCoreApplication.translate("Form", u"Pin 0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PORTA_tab), QCoreApplication.translate("Form", u"PORTA", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PORTB_tab), QCoreApplication.translate("Form", u"PORTB", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PORTC_tab), QCoreApplication.translate("Form", u"PORTC", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PORTD_tab), QCoreApplication.translate("Form", u"PORTD", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"New", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Save", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Load", None))
    # retranslateUi

App= QApplication(sys.argv)
Widget= QWidget()
Form= Ui_Form()
Form.setupUi(Widget)
Widget.show()
App.exec_()