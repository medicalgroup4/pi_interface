# encoding: utf-8
# module PyQt5.QtWidgets
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtWidgets.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QGesture import QGesture

class QSwipeGesture(QGesture):
    """ QSwipeGesture(parent: QObject = None) """
    def horizontalDirection(self): # real signature unknown; restored from __doc__
        """ horizontalDirection(self) -> QSwipeGesture.SwipeDirection """
        pass

    def setSwipeAngle(self, p_float): # real signature unknown; restored from __doc__
        """ setSwipeAngle(self, float) """
        pass

    def swipeAngle(self): # real signature unknown; restored from __doc__
        """ swipeAngle(self) -> float """
        return 0.0

    def verticalDirection(self): # real signature unknown; restored from __doc__
        """ verticalDirection(self) -> QSwipeGesture.SwipeDirection """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    Down = 4
    Left = 1
    NoDirection = 0
    Right = 2
    Up = 3


