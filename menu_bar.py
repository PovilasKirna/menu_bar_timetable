from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon("color.png")

clipboard = QApplication.clipboard()
dialog = QColorDialog()


# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()
action1 = QAction("Hex")
menu.addAction(action1)

action2 = QAction("RGB")
menu.addAction(action2)

action3 = QAction("HSV")
menu.addAction(action3)

# Add the menu to the tray
tray.setContextMenu(menu)

app.exec_()


pirm=  ['', '', 'English HL', 'English HL', 'IP', 'Lithuanian Literature SL', 'Lithuanian Literature SL', 'CS SL', 'CS SL' ]
antr=  ['CS SL', 'CS SL', 'Mathematics SL', 'Mathematics SL', 'IP', 'Physics SL', 'Physics SL', 'Economics SL', 'Economics SL' ]
trec=  ['St. Mess', 'English HL', 'English HL', 'Mathematics HL', 'Mathematics HL', 'IP', 'Religion', 'Physics SL', 'Physics SL' ]
ketv=  ['Lithuanian Literature SL', 'Lithuanian Literature SL', 'Economics SL', 'Economics SL', 'IP', 'TOK', 'TOK', 'CS HL', 'CS HL' ]
penkt=  ['Mathematics SL', 'Mathematics SL', 'English HL', 'English HL', '', '', '', '', '']

time = ['8:00-8:45', '8:55-9:40', '9:50-10:35']