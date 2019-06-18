# encoding: utf-8
# module PyQt5.QtLocation
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtLocation.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPlaceReply import QPlaceReply

class QPlaceMatchReply(QPlaceReply):
    """ QPlaceMatchReply(parent: QObject = None) """
    def places(self): # real signature unknown; restored from __doc__
        """ places(self) -> List[QPlace] """
        return []

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> QPlaceMatchRequest """
        return QPlaceMatchRequest

    def setPlaces(self, Iterable, QPlace=None): # real signature unknown; restored from __doc__
        """ setPlaces(self, Iterable[QPlace]) """
        pass

    def setRequest(self, QPlaceMatchRequest): # real signature unknown; restored from __doc__
        """ setRequest(self, QPlaceMatchRequest) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QPlaceReply.Type """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


