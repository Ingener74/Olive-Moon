import sys

from PySide.QtCore import Qt, QPoint
from PySide.QtGui import QApplication, QWidget, QPainter, QPixmap, QIcon

from SubtleMonkey import Block, Column

WINDOW = 'window'


class Window(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle('Liquid Emerald')
        self.setWindowIcon(QIcon(QPixmap('emerald.png')))

        # self.settings = QSettings()
        # self.restoreGeometry(self.settings.value(WINDOW))

        self.block = Block(
                columns=[
                    Column(
                            blocks=[
                                Block(),
                                Block()
                            ]
                    ),
                    Column()
                ]
        )

    def paintEvent(self, event):
        self.block.paint(QPainter(self), QPoint(5, 5))

    def closeEvent(self, event):
        # self.settings.setValue(WINDOW, self.saveGeometry())
        pass

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
