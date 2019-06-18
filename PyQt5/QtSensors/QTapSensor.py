# encoding: utf-8
# module PyQt5.QtSensors
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtSensors.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QSensor import QSensor

class QTapSensor(QSensor):
    """ QTapSensor(parent: QObject = None) """
    def reading(self): # real signature unknown; restored from __doc__
        """ reading(self) -> QTapReading """
        return QTapReading

    def returnDoubleTapEvents(self): # real signature unknown; restored from __doc__
        """ returnDoubleTapEvents(self) -> bool """
        return False

    def returnDoubleTapEventsChanged(self, bool): # real signature unknown; restored from __doc__
        """ returnDoubleTapEventsChanged(self, bool) [signal] """
        pass

    def setReturnDoubleTapEvents(self, bool): # real signature unknown; restored from __doc__
        """ setReturnDoubleTapEvents(self, bool) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


