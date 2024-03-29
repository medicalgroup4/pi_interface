from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from MQTT import *

mqtt = MQTT(ip="51.83.42.157", port=1883, qos=2, mode=Message_mode.NON_BLOCKING)

app = QApplication([])

def message_callback(topic, measurement):
    print("Received message from patient \"%s\" on topic \"%s\"" % (measurement, topic))
    systolic = measurement.systolic
    diastolic = measurement.diastolic
    heartrate = measurement.heartrate
    oxygen = measurement.oxygen

    lblSysVal.setText(str(systolic))
    lblDiaVal.setText(str(diastolic))
    lblHeartVal.setText(str(heartrate))
    lblOxyVal.setText(str(oxygen))


mqtt.message_callback = message_callback
mqtt.sub_to_topic('database/measurement')
mqtt.connect()

# Saxion image
lblSaxPic = QLabel()

btntest = QPushButton('test')

# 1st column
btnStart = QPushButton('Start')
btnStop = QPushButton('Stop')
btnOk = QPushButton('Ok')
lblInterface = QLabel('Press start to start a measurement')

# 2nd column
lblSysPic = QLabel()
lblDiaPic = QLabel()
lblHeartPic = QLabel()
lblOxyPic = QLabel()

# 3rd column
lblSysVal = QLabel('0')
lblDiaVal = QLabel('0')
lblHeartVal = QLabel('0')
lblOxyVal = QLabel('0')

# 4th column
lblSysUni = QLabel('mmHg')
lblDiaUni = QLabel('mmHg')
lblHeartUni = QLabel('BPM')
lblOxyUni = QLabel('%')


saxpic = QPixmap("./img/saxion.jpg")
scaled = saxpic.scaled(175, 64, Qt.IgnoreAspectRatio, Qt.FastTransformation)
lblSaxPic.setPixmap(scaled)

uppic = QPixmap("./img/chevron.png")
scaled = uppic.scaled(40, 40, Qt.IgnoreAspectRatio, Qt.FastTransformation)
lblSysPic.setPixmap(scaled)

downpic = QPixmap("./img/chevrondown.png")
scaled = downpic.scaled(40, 40, Qt.IgnoreAspectRatio, Qt.FastTransformation)
lblDiaPic.setPixmap(scaled)

heartpic = QPixmap("./img/cardiology.png")
scaled = heartpic.scaled(40, 40, Qt.IgnoreAspectRatio, Qt.FastTransformation)
lblHeartPic.setPixmap(scaled)

oxypic = QPixmap("./img/oxygen.png")
scaled = oxypic.scaled(40, 40, Qt.IgnoreAspectRatio, Qt.FastTransformation)
lblOxyPic.setPixmap(scaled)

window = QWidget()
window.resize(640, 480)
layout = QGridLayout()

def init():

    layout.addWidget(btnOk, 0, 0)
    layout.addWidget(btnStart, 1, 0)
    layout.addWidget(btnStop, 2, 0)
    layout.addWidget(btntest, 3, 0)

    layout.addWidget(lblSysPic, 0, 1)
    layout.addWidget(lblDiaPic, 1, 1)
    layout.addWidget(lblHeartPic, 2, 1)
    layout.addWidget(lblOxyPic, 3, 1)

    layout.addWidget(lblSysVal, 0, 2)
    layout.addWidget(lblDiaVal, 1, 2)
    layout.addWidget(lblHeartVal, 2, 2)
    layout.addWidget(lblOxyVal, 3, 2)

    layout.addWidget(lblSysUni, 0, 3)
    layout.addWidget(lblDiaUni, 1, 3)
    layout.addWidget(lblHeartUni, 2, 3)
    layout.addWidget(lblOxyUni, 3, 3)

    window.setLayout(layout)


def update():
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)
    init()


def on_start_clicked():
    message = 'start'
    mqtt.publish_string('measurement/control', message)


def on_stop_clicked():
    message = 'stop'
    mqtt.publish_string('measurement/control', message)


init()
window.showFullScreen()
btnStart.clicked.connect(on_start_clicked)
btnStop.clicked.connect(on_stop_clicked)


app.exec()




