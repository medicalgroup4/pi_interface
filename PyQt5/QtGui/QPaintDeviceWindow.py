# encoding: utf-8
# module PyQt5.QtGui
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtGui.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QWindow import QWindow

from .QPaintDevice import QPaintDevice

class QPaintDeviceWindow(QWindow, QPaintDevice):
    # no doc
    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def exposeEvent(self, QExposeEvent): # real signature unknown; restored from __doc__
        """ exposeEvent(self, QExposeEvent) """
        pass

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ metric(self, QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ paintEvent(self, QPaintEvent) """
        pass

    def update(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        update(self, QRect)
        update(self, QRegion)
        update(self)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


