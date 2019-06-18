# encoding: utf-8
# module PyQt5.QtSensors
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtSensors.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QSensor import QSensor

class QLightSensor(QSensor):
    """ QLightSensor(parent: QObject = None) """
    def fieldOfView(self): # real signature unknown; restored from __doc__
        """ fieldOfView(self) -> float """
        return 0.0

    def fieldOfViewChanged(self, p_float): # real signature unknown; restored from __doc__
        """ fieldOfViewChanged(self, float) [signal] """
        pass

    def reading(self): # real signature unknown; restored from __doc__
        """ reading(self) -> QLightReading """
        return QLightReading

    def setFieldOfView(self, p_float): # real signature unknown; restored from __doc__
        """ setFieldOfView(self, float) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


