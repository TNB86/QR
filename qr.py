import sys
from tempfile import TemporaryFile

import pyqrcode
from PIL import Image
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import *
from pyzbar.pyzbar import decode

from design import Ui_MainWindow

# create app
app = QApplication()

# init
Window = QMainWindow(None)
ui = Ui_MainWindow()
ui.setupUi(Window)
Window.show()


# hook logic
def error():
    return ('H', 'Q', 'M', 'L')[ui.correction_level.currentIndex()]


def version():
    return ui.version.value()


def scale():
    return 177 / (21 + 4 * (version() - 1)) * 1.66


def get_qr():
    try:
        qr = pyqrcode.create(ui.text.toPlainText(), error(), version())
    except ValueError:
        ui.qr_content.setText('Invalid version or error level\nChoose another version or error level')
        # QMessageBox.critical(Window, 'Error', 'Invalid version or error level\nChoose another version or error level')
        return
    with TemporaryFile('wb+') as f:
        qr.svg(f, scale=scale())
        f.seek(0)
        pixmap = QPixmap()
        pixmap.loadFromData(f.read())
        ui.qr_content.setPixmap(pixmap)


def decode_qr():
    fileName = QFileDialog.getOpenFileName(filter='Images (*.png *.jpg)')
    df = decode(Image.open(fileName[0]))
    try:
        ui.decoded_text.setPlainText(df[0].data.decode('ascii'))
    except IndexError:
        ui.decoded_qr_content.setText('Invalid image')
        return
    pixmap = QPixmap(fileName[0])
    sp = QPixmap.scaled(pixmap, 300, 300)
    ui.decoded_qr_content.setPixmap(sp)


ui.generate.clicked.connect(get_qr)

ui.open_file.clicked.connect(decode_qr)

# mail loop
sys.exit(app.exec_())
