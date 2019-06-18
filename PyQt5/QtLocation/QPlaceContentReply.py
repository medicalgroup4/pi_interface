# encoding: utf-8
# module PyQt5.QtLocation
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtLocation.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QPlaceReply import QPlaceReply

class QPlaceContentReply(QPlaceReply):
    """ QPlaceContentReply(parent: QObject = None) """
    def content(self): # real signature unknown; restored from __doc__
        """ content(self) -> Dict[int, QPlaceContent] """
        return {}

    def nextPageRequest(self): # real signature unknown; restored from __doc__
        """ nextPageRequest(self) -> QPlaceContentRequest """
        return QPlaceContentRequest

    def previousPageRequest(self): # real signature unknown; restored from __doc__
        """ previousPageRequest(self) -> QPlaceContentRequest """
        return QPlaceContentRequest

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> QPlaceContentRequest """
        return QPlaceContentRequest

    def setContent(self, Dict, p_int=None, QPlaceContent=None): # real signature unknown; restored from __doc__
        """ setContent(self, Dict[int, QPlaceContent]) """
        pass

    def setNextPageRequest(self, QPlaceContentRequest): # real signature unknown; restored from __doc__
        """ setNextPageRequest(self, QPlaceContentRequest) """
        pass

    def setPreviousPageRequest(self, QPlaceContentRequest): # real signature unknown; restored from __doc__
        """ setPreviousPageRequest(self, QPlaceContentRequest) """
        pass

    def setRequest(self, QPlaceContentRequest): # real signature unknown; restored from __doc__
        """ setRequest(self, QPlaceContentRequest) """
        pass

    def setTotalCount(self, p_int): # real signature unknown; restored from __doc__
        """ setTotalCount(self, int) """
        pass

    def totalCount(self): # real signature unknown; restored from __doc__
        """ totalCount(self) -> int """
        return 0

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QPlaceReply.Type """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


