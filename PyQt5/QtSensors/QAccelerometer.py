# encoding: utf-8
# module PyQt5.QtSensors
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtSensors.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QSensor import QSensor

class QAccelerometer(QSensor):
    """ QAccelerometer(parent: QObject = None) """
    def accelerationMode(self): # real signature unknown; restored from __doc__
        """ accelerationMode(self) -> QAccelerometer.AccelerationMode """
        pass

    def accelerationModeChanged(self, QAccelerometer_AccelerationMode): # real signature unknown; restored from __doc__
        """ accelerationModeChanged(self, QAccelerometer.AccelerationMode) [signal] """
        pass

    def reading(self): # real signature unknown; restored from __doc__
        """ reading(self) -> QAccelerometerReading """
        return QAccelerometerReading

    def setAccelerationMode(self, QAccelerometer_AccelerationMode): # real signature unknown; restored from __doc__
        """ setAccelerationMode(self, QAccelerometer.AccelerationMode) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    Combined = 0
    Gravity = 1
    User = 2


