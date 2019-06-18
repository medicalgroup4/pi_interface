# encoding: utf-8
# module PyQt5.QtCore
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtCore.so
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractState import QAbstractState

class QFinalState(QAbstractState):
    """ QFinalState(parent: QState = None) """
    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def onEntry(self, QEvent): # real signature unknown; restored from __doc__
        """ onEntry(self, QEvent) """
        pass

    def onExit(self, QEvent): # real signature unknown; restored from __doc__
        """ onExit(self, QEvent) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


