# encoding: utf-8
# module PyQt5.QtCore
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtCore.so
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractTransition import QAbstractTransition

class QSignalTransition(QAbstractTransition):
    """
    QSignalTransition(sourceState: QState = None)
    QSignalTransition(pyqtBoundSignal, sourceState: QState = None)
    """
    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventTest(self, QEvent): # real signature unknown; restored from __doc__
        """ eventTest(self, QEvent) -> bool """
        return False

    def onTransition(self, QEvent): # real signature unknown; restored from __doc__
        """ onTransition(self, QEvent) """
        pass

    def senderObject(self): # real signature unknown; restored from __doc__
        """ senderObject(self) -> QObject """
        return QObject

    def senderObjectChanged(self): # real signature unknown; restored from __doc__
        """ senderObjectChanged(self) [signal] """
        pass

    def setSenderObject(self, QObject): # real signature unknown; restored from __doc__
        """ setSenderObject(self, QObject) """
        pass

    def setSignal(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setSignal(self, Union[QByteArray, bytes, bytearray]) """
        pass

    def signal(self): # real signature unknown; restored from __doc__
        """ signal(self) -> QByteArray """
        return QByteArray

    def signalChanged(self): # real signature unknown; restored from __doc__
        """ signalChanged(self) [signal] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

