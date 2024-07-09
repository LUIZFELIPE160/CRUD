# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1059, 620)
        MainWindow.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_8.setFont(font)
        self.label_8.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label_8.setAcceptDrops(False)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setStyleSheet("background-color: rgb(193, 193, 193);\n"
"color: rgb(0, 0, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(2, 0, 11, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(135, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(193, 193, 193);border-radius:5px")
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.l_cpf = QtWidgets.QLineEdit(self.frame)
        self.l_cpf.setMinimumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_cpf.setFont(font)
        self.l_cpf.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.l_cpf.setObjectName("l_cpf")
        self.horizontalLayout.addWidget(self.l_cpf)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(135, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(193, 193, 193);\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.l_nome = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_nome.sizePolicy().hasHeightForWidth())
        self.l_nome.setSizePolicy(sizePolicy)
        self.l_nome.setMinimumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_nome.setFont(font)
        self.l_nome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.l_nome.setObjectName("l_nome")
        self.horizontalLayout_2.addWidget(self.l_nome)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(135, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.l_idade = QtWidgets.QLineEdit(self.frame)
        self.l_idade.setMinimumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_idade.setFont(font)
        self.l_idade.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"")
        self.l_idade.setObjectName("l_idade")
        self.horizontalLayout_3.addWidget(self.l_idade)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(135, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.l_funcao = QtWidgets.QLineEdit(self.frame)
        self.l_funcao.setMinimumSize(QtCore.QSize(350, 30))
        self.l_funcao.setBaseSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_funcao.setFont(font)
        self.l_funcao.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.l_funcao.setObjectName("l_funcao")
        self.horizontalLayout_4.addWidget(self.l_funcao)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(143, 0))
        self.label_5.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.l_date = QtWidgets.QDateEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_date.sizePolicy().hasHeightForWidth())
        self.l_date.setSizePolicy(sizePolicy)
        self.l_date.setMinimumSize(QtCore.QSize(135, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.l_date.setFont(font)
        self.l_date.setMouseTracking(False)
        self.l_date.setAcceptDrops(False)
        self.l_date.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.l_date.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"")
        self.l_date.setReadOnly(False)
        self.l_date.setKeyboardTracking(True)
        self.l_date.setCalendarPopup(True)
        self.l_date.setCurrentSectionIndex(2)
        self.l_date.setDate(QtCore.QDate(2000, 1, 2))
        self.l_date.setObjectName("l_date")
        self.horizontalLayout_5.addWidget(self.l_date)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setMinimumSize(QtCore.QSize(135, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.l_remuneracao = QtWidgets.QLineEdit(self.frame)
        self.l_remuneracao.setMinimumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_remuneracao.setFont(font)
        self.l_remuneracao.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.l_remuneracao.setObjectName("l_remuneracao")
        self.horizontalLayout_6.addWidget(self.l_remuneracao)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setMinimumSize(QtCore.QSize(135, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.l_observacao = QtWidgets.QLineEdit(self.frame)
        self.l_observacao.setMinimumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_observacao.setFont(font)
        self.l_observacao.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.l_observacao.setObjectName("l_observacao")
        self.horizontalLayout_7.addWidget(self.l_observacao)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(-1, -1, 50, -1)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_adicionar = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_adicionar.sizePolicy().hasHeightForWidth())
        self.btn_adicionar.setSizePolicy(sizePolicy)
        self.btn_adicionar.setMinimumSize(QtCore.QSize(120, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_adicionar.setFont(font)
        self.btn_adicionar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_adicionar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"")
        self.btn_adicionar.setAutoDefault(False)
        self.btn_adicionar.setFlat(False)
        self.btn_adicionar.setObjectName("btn_adicionar")
        self.verticalLayout_2.addWidget(self.btn_adicionar)
        self.btn_atualizar = QtWidgets.QPushButton(self.frame_2)
        self.btn_atualizar.setMinimumSize(QtCore.QSize(120, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_atualizar.setFont(font)
        self.btn_atualizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_atualizar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.btn_atualizar.setObjectName("btn_atualizar")
        self.verticalLayout_2.addWidget(self.btn_atualizar)
        self.btn_delete = QtWidgets.QPushButton(self.frame_2)
        self.btn_delete.setMinimumSize(QtCore.QSize(120, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_delete.setFont(font)
        self.btn_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_delete.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.btn_delete.setObjectName("btn_delete")
        self.verticalLayout_2.addWidget(self.btn_delete)
        spacerItem = QtWidgets.QSpacerItem(20, 173, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.btn_veritem = QtWidgets.QPushButton(self.frame_2)
        self.btn_veritem.setMinimumSize(QtCore.QSize(120, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_veritem.setFont(font)
        self.btn_veritem.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_veritem.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.btn_veritem.setObjectName("btn_veritem")
        self.verticalLayout_2.addWidget(self.btn_veritem)
        self.horizontalLayout_8.addWidget(self.frame_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.tw_funcionarios = QtWidgets.QTreeWidget(self.centralwidget)
        self.tw_funcionarios.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tw_funcionarios.sizePolicy().hasHeightForWidth())
        self.tw_funcionarios.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tw_funcionarios.setFont(font)
        self.tw_funcionarios.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.tw_funcionarios.setDragEnabled(True)
        self.tw_funcionarios.setDragDropOverwriteMode(False)
        self.tw_funcionarios.setUniformRowHeights(False)
        self.tw_funcionarios.setItemsExpandable(True)
        self.tw_funcionarios.setAllColumnsShowFocus(False)
        self.tw_funcionarios.setExpandsOnDoubleClick(True)
        self.tw_funcionarios.setColumnCount(7)
        self.tw_funcionarios.setObjectName("tw_funcionarios")
        self.tw_funcionarios.header().setVisible(True)
        self.tw_funcionarios.header().setCascadingSectionResizes(False)
        self.tw_funcionarios.header().setDefaultSectionSize(152)
        self.tw_funcionarios.header().setMinimumSectionSize(152)
        self.tw_funcionarios.header().setSortIndicatorShown(False)
        self.verticalLayout_3.addWidget(self.tw_funcionarios)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "Cadastro de funcionários"))
        self.label.setText(_translate("MainWindow", "CPF"))
        self.label_2.setText(_translate("MainWindow", "Nome"))
        self.label_3.setText(_translate("MainWindow", "Idade"))
        self.label_4.setText(_translate("MainWindow", "Função"))
        self.label_5.setText(_translate("MainWindow", "Data da Admissão"))
        self.label_6.setText(_translate("MainWindow", "Remuneração"))
        self.label_7.setText(_translate("MainWindow", "Observações"))
        self.btn_adicionar.setText(_translate("MainWindow", "ADICIONAR"))
        self.btn_atualizar.setText(_translate("MainWindow", "ATUALIZAR"))
        self.btn_delete.setText(_translate("MainWindow", "DELETE"))
        self.btn_veritem.setText(_translate("MainWindow", "LIMPAR"))
        self.tw_funcionarios.headerItem().setText(0, _translate("MainWindow", "CPF"))
        self.tw_funcionarios.headerItem().setText(1, _translate("MainWindow", "Nome"))
        self.tw_funcionarios.headerItem().setText(2, _translate("MainWindow", "Idade"))
        self.tw_funcionarios.headerItem().setText(3, _translate("MainWindow", "Função"))
        self.tw_funcionarios.headerItem().setText(4, _translate("MainWindow", "Data da Admissão"))
        self.tw_funcionarios.headerItem().setText(5, _translate("MainWindow", "Função"))
        self.tw_funcionarios.headerItem().setText(6, _translate("MainWindow", "Obs"))