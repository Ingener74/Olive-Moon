import sys

from PySide.QtCore import Qt, QPoint, QSettings
from PySide.QtGui import QApplication, QWidget, QPainter, QPixmap, QIcon

from SubtleMonkey import Block, Column


class Window(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle('Liquid Emerald')
        self.setWindowIcon(QIcon(QPixmap('emerald.png')))

        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, 'VenusGames', 'LiquidEmerald')
        self.restoreGeometry(self.settings.value(self.__class__.__name__))

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
        self.settings.setValue(self.__class__.__name__, self.saveGeometry())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
