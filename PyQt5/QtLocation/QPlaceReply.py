# encoding: utf-8
# module PyQt5.QtLocation
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtLocation.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPlaceReply(__PyQt5_QtCore.QObject):
    """ QPlaceReply(parent: QObject = None) """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def aborted(self): # real signature unknown; restored from __doc__
        """ aborted(self) [signal] """
        pass

    def contentUpdated(self): # real signature unknown; restored from __doc__
        """ contentUpdated(self) [signal] """
        pass

    def error(self, QPlaceReply_Error=None, errorString=''): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QPlaceReply.Error
        error(self, QPlaceReply.Error, errorString: str = '') [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def finished(self): # real signature unknown; restored from __doc__
        """ finished(self) [signal] """
        pass

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def setError(self, QPlaceReply_Error, p_str): # real signature unknown; restored from __doc__
        """ setError(self, QPlaceReply.Error, str) """
        pass

    def setFinished(self, bool): # real signature unknown; restored from __doc__
        """ setFinished(self, bool) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QPlaceReply.Type """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    BadArgumentError = 7
    CancelError = 8
    CategoryDoesNotExistError = 2
    CommunicationError = 3
    ContentReply = 4
    DetailsReply = 1
    IdReply = 5
    MatchReply = 6
    NoError = 0
    ParseError = 4
    PermissionsError = 5
    PlaceDoesNotExistError = 1
    Reply = 0
    SearchReply = 2
    SearchSuggestionReply = 3
    UnknownError = 9
    UnsupportedError = 6


