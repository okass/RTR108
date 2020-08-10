import sys

# qt py binds
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtGui import QImageReader
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QFileInfo
from PyQt5.QtCore import Qt

# image loading logic

# load image file
# returns false if loaded file isnt correct image
# returns image object if file load as successful
def loadImageFile(fname):
	reader = QImageReader(fname)
	reader.setAutoTransform(True)
	newImage = reader.read()
	if newImage.isNull():
		msg = ("couldnt load "
				+ QFileInfo(fname).fileName()
				+ ": "
				+ reader.errorString())
		sb_txt.setText(msg)
		return False
	else:
		return newImage

def loadImage():
	# file picker
	f_diag = QFileDialog()
	f_diag.labelText = "Open image"
	
	# lets pick supported file types
	mimeTypes = QImageReader.supportedMimeTypes()
	for x in range(len(mimeTypes)): 
		mimeTypes[x] = str(mimeTypes[x], 'utf-8')
	
	f_diag.setMimeTypeFilters(mimeTypes)
	
	f_diag.setFileMode(QFileDialog.ExistingFile)
	
	# checks wherever anything was picked
	if f_diag.exec():
		res = loadImageFile(f_diag.selectedFiles()[0])
		if res:
			sb_txt.setText("current image: "
				+ QFileInfo(f_diag.selectedFiles()[0]).fileName())
			imageLabel.setPixmap(QPixmap.fromImage(res))
			imageLabel.resize(res.width(), res.height())


# init GUI elements
# main app
app = QApplication(sys.argv)

# main window
window = QMainWindow()
window.setWindowTitle("test application RTR108")
# window size and location
avail_size = app.primaryScreen().availableSize()
window.resize(avail_size * 3 / 5)
window.move(app.desktop().screen().rect().center() - window.rect().center())

# top menu bar
menu_file = window.menuBar().addMenu("&File")
menu_file.addAction("&Load Image", loadImage)
menu_file.addAction("&Exit", window.close)

# status bar at the bottom
sb = window.statusBar()
# add text to it so it doesnt reset
sb_txt = QLabel("No file loaded.")
sb.addPermanentWidget(sb_txt)

# label used for displaying image
imageLabel = QLabel()
# scroll area for image
scroll_a = QScrollArea()
scroll_a.setBackgroundRole(4) #QPalette::Dark = 4
scroll_a.setWidget(imageLabel)
scroll_a.setAlignment(Qt.AlignCenter) # set alignment for image
window.setCentralWidget(scroll_a)

# display main window
window.show()
# exit fnc though button is used to exit
sys.exit(app.exec_())