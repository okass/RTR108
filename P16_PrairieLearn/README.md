# Uzdevums - Vienkāršs attēlu skatītājs izmantojot python Qt 

Izmantojot python Qt bibliotēku var uztaisīt vienkāršu attēlu skatītāju.

Sāk ar nepieciešamo bibliotēku importēšanu.

```python
# python sistēmas bibliotēka
import sys

# saknes objekts programmai
from PyQt5.QtWidgets import QApplication
# saknes logs
from PyQt5.QtWidgets import QMainWindow
# etiķetes (labels)
from PyQt5.QtWidgets import QLabel
# failu dialogs (tiks izmantots vēlāk bilžu lasīšanai)
from PyQt5.QtWidgets import QFileDialog
# ritināms objekts (tiks izmanots)
from PyQt5.QtWidgets import QScrollArea
# objekts attēlu lasīšanai
from PyQt5.QtGui import QImageReader
# objekts attēlu rādīšanai
from PyQt5.QtGui import QPixmap
# rīki failu atrašanās vietas apstrādei
from PyQt5.QtCore import QFileInfo
# kodola saknes objekts (tiks izmantots priekš "uzskaitītāja"(enum))
from PyQt5.QtCore import Qt
```

Pēc nepieciešamo bibliotēku piesaukšanas, varam sākt definēt programmu.

Izveido galveno aplikācijas objektu.

```python
app = QApplication(sys.argv)
```


Programmas saknes objekta(galvenā loga) definēšanas un izmēru uzstādīšana.

```python
# galvenais logs
window = QMainWindow()
window.setWindowTitle("Image viewer RTR108")

# loga izmēri un atrašanās vieta
# nolasa pieejamo vietu uz pašreizējā ekrāna
avail_size = app.primaryScreen().availableSize()

# izmaina loga izmērus
window.resize(avail_size * 3 / 5) 

# nocentrē logu ekrāna vidū
window.move(app.desktop().screen().rect().center() - window.rect().center())
```


Izveido rīkjoslu programmas augšpusē un statusa joslu programmas loga apakšpusē.

```python
# augšējās rīkjoslas definēšana
# pievieno izvēlni "File" ("Fails")
menu_file = window.menuBar().addMenu("&File")

# zem izvēlnes "File" pievieno opciju "Load image"("Ielādēt attēlu") 
# un "Exit"("Iziet")
# uzspiežot uz opcijas "Load Image" tiks izsaukta funkcija loadImage(), kuru vēlāk definēsim
menu_file.addAction("&Load Image", loadImage)
menu_file.addAction("&Exit", window.close)


# statusa josla apakšpusē
sb = window.statusBar()
# izveido noklusējuma teksta etiķeti 
# un pievieno to zem status joslas objekta kā pastāvošu tekstu.
sb_txt = QLabel("No file loaded.")
sb.addPermanentWidget(sb_txt)
```


Nodefinē loga galveno saturu: attēla rādīšanas vietu.

```python
# etiķete, kuru izmantosim attēla parādīšanai
imageLabel = QLabel()

# tā kā attēls var būt lielāks par logu vai pat lielāks par ekrānu, 
# uz kura logs atrodas, izmantosim ritināmu zonu lai atvieglinātu dzīvi
scroll_a = QScrollArea()

# iestata ritināmās zonas fona krāsu
scroll_a.setBackgroundRole(4) #QPalette::Dark = 4

# iestata ritināmo zonu kā vecāka objektu attēla etiķetei
scroll_a.setWidget(imageLabel)

# nocentrē visus objektus ritināmajā zonā
scroll_a.setAlignment(Qt.AlignCenter)
# iestata attēla etiķeti kā centrālo objektu
window.setCentralWidget(scroll_a)
```


Iepriekš nodefinējām, ka izvēlnes `"File"` opcija `"Load Image"` izsauks funkciju `loadImage()`. Tagad tā ir jānodefinē.

```python
# nodefinē funkciju loadImage()
def loadImage():
	# failu atlasītāja objekta definēšana
	f_diag = QFileDialog()
	# failu atlasītāja loga virsraksts
	f_diag.labelText = "Open image"
	
	# failu atlasītājam ir nepieciešams definēt atļautos failu tipu, 
	# lai atvieglotu bilžu ielasīšanu
	# vispirms iegūst List objektu no QImageReader klases ar atļautajiem mime tipiem
	# vairāk par mime tipiem: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types
	mimeTypes = QImageReader.supportedMimeTypes()
	# bet tas atgriež tos baitu masīva formātā, tāpēc ir jāpārveido par tekstu
	for x in range(len(mimeTypes)): 
		mimeTypes[x] = str(mimeTypes[x], 'utf-8')
	
	
	# iestata atlasītos mime tipus
	f_diag.setMimeTypeFilters(mimeTypes)
	
	# iestata failu atlasītāju failu atlases režīmā
	f_diag.setFileMode(QFileDialog.ExistingFile)
	
	# izpilda faila atlases dialogu un ja tas atgriež vērtību turpina izpildi
	if f_diag.exec():
		# mēģina ielasīt attēla failu
		# šī funkcija ir jānodefinē
		res = loadImageFile(f_diag.selectedFiles()[0])
```


Attēla ielasīšanas funkcija

```python
# funkcija pieņem attēla atrašanās vietu kā argumentu
def loadImageFile(fname):
	# attēla lasītājs
	reader = QImageReader(fname)
	# nosaka vai attēla pielietot attēlā definētās funkcijas kā pagriešanu
	reader.setAutoTransform(True)
	# ielasa attēlu
	newImage = reader.read()
	# ja attēla ielasīšana neizdevās iestata status joslā ziņu ar faila nosaukumu
	# un kļūdas tekstu un funkcijas atgriež False
	if newImage.isNull():
		msg = ("couldnt load "
				+ QFileInfo(fname).fileName()
				+ ": "
				+ reader.errorString())
		sb_txt.setText(msg)
		return False
	# ja attēla ielasīšana izdevās atgriež jauniegūto attēla objektu tālākām darbībām
	else:
		return newImage
		

Atgriežoties pie loadImage()

```python
		# ja funkcija atgrieza attēla objektu turpina izpildi
		if res:
			# iestata statusa joslā ielasītā faila nosaukumu
			sb_txt.setText("current image: "
				+ QFileInfo(f_diag.selectedFiles()[0]).fileName())
			# izveido pikseļu "karti" no ielasītā attēla un iestata to
			# kā attēla etiķetes bildi
			imageLabel.setPixmap(QPixmap.fromImage(res))
			# attiecīgi nomaina attēla etiķetes izmērus uz pašreizējo bildi
			imageLabel.resize(res.width(), res.height())
```


Kad visi lietotāja interfeisa elementi ir iestatīti un funkcijas nodefinētas varam galu galā parādīt iznākumu.

```python
# parāda galveno logu
window.show()
```


Sakārtojo iepriekš aplūkoto kodu iegūstam gatavu programmu.

```python
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtGui import QImageReader
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QFileInfo
from PyQt5.QtCore import Qt

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
	f_diag = QFileDialog()
	f_diag.labelText = "Open image"
	
	mimeTypes = QImageReader.supportedMimeTypes()
	for x in range(len(mimeTypes)): 
		mimeTypes[x] = str(mimeTypes[x], 'utf-8')
	
	f_diag.setMimeTypeFilters(mimeTypes)
	
	f_diag.setFileMode(QFileDialog.ExistingFile)
	
	if f_diag.exec():
		res = loadImageFile(f_diag.selectedFiles()[0])
		if res:
			sb_txt.setText("current image: "
				+ QFileInfo(f_diag.selectedFiles()[0]).fileName())
			imageLabel.setPixmap(QPixmap.fromImage(res))
			imageLabel.resize(res.width(), res.height())


app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("test application RTR108")
avail_size = app.primaryScreen().availableSize()
window.resize(avail_size * 3 / 5)
window.move(app.desktop().screen().rect().center() - window.rect().center())

menu_file = window.menuBar().addMenu("&File")
menu_file.addAction("&Load Image", loadImage)
menu_file.addAction("&Exit", window.close)

sb = window.statusBar()
sb_txt = QLabel("No file loaded.")
sb.addPermanentWidget(sb_txt)

imageLabel = QLabel()
scroll_a = QScrollArea()
scroll_a.setBackgroundRole(4)
scroll_a.setWidget(imageLabel)
scroll_a.setAlignment(Qt.AlignCenter)
window.setCentralWidget(scroll_a)

window.show()
```