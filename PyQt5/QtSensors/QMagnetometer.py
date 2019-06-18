# encoding: utf-8
# module PyQt5.QtSensors
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtSensors.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QSensor import QSensor

class QMagnetometer(QSensor):
    """ QMagnetometer(parent: QObject = None) """
    def reading(self): # real signature unknown; restored from __doc__
        """ reading(self) -> QMagnetometerReading """
        return QMagnetometerReading

    def returnGeoValues(self): # real signature unknown; restored from __doc__
        """ returnGeoValues(self) -> bool """
        return False

    def returnGeoValuesChanged(self, bool): # real signature unknown; restored from __doc__
        """ returnGeoValuesChanged(self, bool) [signal] """
        pass

    def setReturnGeoValues(self, bool): # real signature unknown; restored from __doc__
        """ setReturnGeoValues(self, bool) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


