# encoding: utf-8
# module PyQt5.QtSensors
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtSensors.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QSensor import QSensor

class QHumiditySensor(QSensor):
    """ QHumiditySensor(parent: QObject = None) """
    def reading(self): # real signature unknown; restored from __doc__
        """ reading(self) -> QHumidityReading """
        return QHumidityReading

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


