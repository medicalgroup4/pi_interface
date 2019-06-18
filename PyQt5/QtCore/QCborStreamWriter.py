# encoding: utf-8
# module PyQt5.QtCore
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtCore.so
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QCborStreamWriter(__sip.simplewrapper):
    """
    QCborStreamWriter(QIODevice)
    QCborStreamWriter(Union[QByteArray, bytes, bytearray])
    """
    def append(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        append(self, QCborSimpleType)
        append(self, QCborKnownTags)
        append(self, str)
        append(self, Union[QByteArray, bytes, bytearray])
        append(self, bool)
        append(self, float)
        append(self, int)
        """
        pass

    def appendNull(self): # real signature unknown; restored from __doc__
        """ appendNull(self) """
        pass

    def appendUndefined(self): # real signature unknown; restored from __doc__
        """ appendUndefined(self) """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QIODevice """
        return QIODevice

    def endArray(self): # real signature unknown; restored from __doc__
        """ endArray(self) -> bool """
        return False

    def endMap(self): # real signature unknown; restored from __doc__
        """ endMap(self) -> bool """
        return False

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ setDevice(self, QIODevice) """
        pass

    def startArray(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        startArray(self)
        startArray(self, int)
        """
        pass

    def startMap(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        startMap(self)
        startMap(self, int)
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



