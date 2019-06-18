# encoding: utf-8
# module PyQt5.QtSensors
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtSensors.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QSensor import QSensor

class QRotationSensor(QSensor):
    """ QRotationSensor(parent: QObject = None) """
    def hasZ(self): # real signature unknown; restored from __doc__
        """ hasZ(self) -> bool """
        return False

    def hasZChanged(self, bool): # real signature unknown; restored from __doc__
        """ hasZChanged(self, bool) [signal] """
        pass

    def reading(self): # real signature unknown; restored from __doc__
        """ reading(self) -> QRotationReading """
        return QRotationReading

    def setHasZ(self, bool): # real signature unknown; restored from __doc__
        """ setHasZ(self, bool) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


