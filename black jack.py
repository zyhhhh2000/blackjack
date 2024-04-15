import sys
import numpy as np
from PyQt6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QPushButton, QWidget
from PyQt6 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.label1 = QLabel("本家")
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        self.label2 = QLabel("庄家")
        self.input3 = QLineEdit()
        self.label3 = QLabel("")
        self.label4 = QLabel("")
        self.label5 = QLabel("")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.input1)

        self.layout.addWidget(self.input2)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.input3)
        self.button1 = QPushButton("GO!")
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(self.label4)
        self.layout.addWidget(self.label5)

        self.container = QWidget()
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

        self.button1.clicked.connect(self.cal)

    def cal(self):
        a1 = int(self.input1.text())
        a2 = int(self.input2.text())
        b0 = int(self.input3.text())

        #######庄家 P = pbb
        # bb = [17,18,19,20,21,0]
        pbb = np.zeros(6)
        q = 1 / 13
        if b0 == 11:
            A0 = 1
        else:
            A0 = 0
        for i1 in range(10):
            p1 = 1
            b1 = b0
            if i1 + 2 == 11:
                A1 = A0 + 1
            else:
                A1 = A0
            if i1 + 2 == 10:
                p1 = p1 * 4
            if b1 + i1 + 2 > 21 and A1 > 0:
                A1 = A1 - 1
                b1 = b1 - 10
            if b1 + i1 + 2 >= 17:
                if b1 + i1 + 2 > 21:
                    pbb[5] = pbb[5] + p1 * q
                else:
                    pbb[b1 + i1 + 2 - 17] = pbb[b1 + i1 + 2 - 17] + p1 * q
                continue
            else:
                for i2 in range(10):
                    p2 = p1 * q
                    b2 = b1 + i1 + 2
                    if i2 + 2 == 11:
                        A2 = A1 + 1
                    else:
                        A2 = A1
                    if i2 + 2 == 10:
                        p2 = p2 * 4
                    if b2 + i2 + 2 > 21 and A2 > 0:
                        A2 = A2 - 1
                        b2 = b2 - 10
                    if b2 + i2 + 2 >= 17:
                        if b2 + i2 + 2 > 21:
                            pbb[5] = pbb[5] + p2 * q
                        else:
                            pbb[b2 + i2 + 2 - 17] = pbb[b2 + i2 + 2 - 17] + p2 * q
                        continue
                    else:
                        for i3 in range(10):
                            p3 = p2 * q
                            b3 = b2 + i2 + 2
                            if i3 + 2 == 11:
                                A3 = A2 + 1
                            else:
                                A3 = A2
                            if i3 + 2 == 10:
                                p3 = p3 * 4
                            if b3 + i3 + 2 > 21 and A3 > 0:
                                A3 = A3 - 1
                                b3 = b3 - 10
                            if b3 + i3 + 2 >= 17:
                                if b3 + i3 + 2 > 21:
                                    pbb[5] = pbb[5] + p3 * q
                                else:
                                    pbb[b3 + i3 + 2 - 17] = pbb[b3 + i3 + 2 - 17] + p3 * q
                                continue
                            else:
                                for i4 in range(10):
                                    p4 = p3 * q
                                    b4 = b3 + i3 + 2
                                    if i4 + 2 == 11:
                                        A4 = A3 + 1
                                    else:
                                        A4 = A3
                                    if i4 + 2 == 10:
                                        p4 = p4 * 4
                                    if b4 + i4 + 2 > 21 and A4 > 0:
                                        A4 = A4 - 1
                                        b4 = b4 - 10
                                    if b4 + i4 + 2 >= 17:
                                        if b4 + i4 + 2 > 21:
                                            pbb[5] = pbb[5] + p4 * q
                                        else:
                                            pbb[b4 + i4 + 2 - 17] = pbb[b4 + i4 + 2 - 17] + p4 * q
                                        continue
                                    else:
                                        for i5 in range(10):
                                            p5 = p4 * q
                                            b5 = b4 + i4 + 2
                                            if i5 + 2 == 11:
                                                A5 = A4 + 1
                                            else:
                                                A5 = A4
                                            if i5 + 2 == 10:
                                                p5 = p5 * 4
                                            if b5 + i5 + 2 > 21 and A5 > 0:
                                                A5 = A5 - 1
                                                b5 = b5 - 10
                                            if b5 + i5 + 2 >= 17:
                                                if b5 + i5 + 2 > 21:
                                                    pbb[5] = pbb[5] + p5 * q
                                                else:
                                                    pbb[b5 + i5 + 2 - 17] = pbb[b5 + i5 + 2 - 17] + p5 * q
                                                continue

        # print(b0, "庄家17:", round(pbb[0]*1000)/10,"%")
        # print(b0, "庄家18:", round(pbb[1]*1000)/10,"%")
        # print(b0, "庄家19:", round(pbb[2]*1000)/10,"%")
        # print(b0, "庄家20:", round(pbb[3]*1000)/10,"%")
        # print(b0, "庄家21:", round(pbb[4]*1000)/10,"%")
        # print(b0, "庄家爆:", round(pbb[5]*1000)/10,"%")
        # print(b0, "其他:", (1-sum(pbb))*100,"%")

        #######自家
        a0 = a1 + a2
        AA0 = 0
        if a1 == 11:
            AA0 = AA0 + 1
        if a2 == 11:
            AA0 = AA0 + 1

        ####pwin0
        pwin0 = 0
        if a0 > 21:
            pwin0 = 0
        else:
            pwin0 = pwin0 + pbb[5]
        if 21 >= a0 > 17:
            for i in range(a0 - 16):
                if i == a0 - 17:
                    pwin0 = pwin0 + 1 / 2 * pbb[i]
                else:
                    pwin0 = pwin0 + pbb[i]
        print("stop赢的概率:", round(pwin0 * 1000) / 10, "%")

        ####pwin1
        q = 1 / 13
        pwin1 = 0
        for i1 in range(10):
            p1 = 1
            a1 = a0
            if i1 + 2 == 11:
                AA1 = AA0 + 1
            else:
                AA1 = AA0
            if i1 + 2 == 10:
                p1 = p1 * 4
            if a1 + i1 + 2 > 21 and AA1 > 0:
                AA1 = AA1 - 1
                a1 = a1 - 10
            if a1 + i1 + 2 > 21:
                pwin1 = pwin1
            else:
                pwin1 = pwin1 + pbb[5] * p1 * q
            if 21 >= a1 + i1 + 2 > 17:
                for i in range(a1 + i1 + 2 - 16):
                    if i == a1 + i1 + 2 - 17:
                        pwin1 = pwin1 + 1 / 2 * pbb[i] * p1 * q
                    else:
                        pwin1 = pwin1 + pbb[i] * p1 * q

        print("go赢的概率:", round(pwin1 * 1000) / 10, "%")

        if pwin1 > pwin0:
            self.label3.setText("GO！")
        else:
            self.label3.setText("STOP！")

        self.label4.setText(str(round(np.abs(pwin0) * 1000) / 10))
        self.label5.setText(str(round(np.abs(pwin1) * 1000) / 10))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
