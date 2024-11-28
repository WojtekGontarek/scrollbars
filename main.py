import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class Myform(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.gluScroll.valueChanged.connect(self.change_spin_box)
        self.ui.choBar.valueChanged.connect(self.change_spin_box)
        self.ui.hemoBar.valueChanged.connect(self.change_spin_box)

        self.ui.gluSpin.valueChanged.connect(self.change_bar)
        self.ui.choSpin.valueChanged.connect(self.change_bar)
        self.ui.hemoSpin.valueChanged.connect(self.change_bar)
        self.show()

    def change_spin_box(self):
        self.ui.hemoSpin.setValue(self.ui.hemoBar.value())
        self.ui.choSpin.setValue(self.ui.choBar.value())
        self.ui.gluSpin.setValue(self.ui.gluScroll.value())
        self.death()

    def change_bar(self):
        self.ui.hemoBar.setValue(self.ui.hemoSpin.value())
        self.ui.choBar.setValue(self.ui.choSpin.value())
        self.ui.gluScroll.setValue(self.ui.gluSpin.value())
        self.death()


    def death(self):
        hemo = self.ui.hemoSpin.value()
        chol = self.ui.choSpin.value()
        glu = self.ui.gluSpin.value()

        hemo_death = 0
        if hemo<12:
            hemo_death = (1/12 * (12-hemo))*100

        chol_death = 0
        if chol> 200:
            chol_death = (1/200 * (chol-200))*100

        glu_death = 0
        if glu>130:
            glu_death = (1/370*(glu-130))*100
        elif glu<70:
            glu_death = (1/70*(70-glu))*100

        death = int((glu_death + hemo_death + chol_death)/3)
        self.ui.smiercProgress.setValue(death)

        self.ui.smiercEmoticon.setFont(QFont('Arial', 30))
        if death < 33:
            self.ui.smiercEmoticon.setText("😀")
        elif death <66:
            self.ui.smiercEmoticon.setText("😐")
        else:
            self.ui.smiercEmoticon.setText("☠️")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Myform()
    sys.exit(app.exec())