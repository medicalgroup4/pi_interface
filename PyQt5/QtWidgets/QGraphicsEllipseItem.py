# encoding: utf-8
# module PyQt5.QtWidgets
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtWidgets.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAbstractGraphicsShapeItem import QAbstractGraphicsShapeItem

class QGraphicsEllipseItem(QAbstractGraphicsShapeItem):
    """
    QGraphicsEllipseItem(parent: QGraphicsItem = None)
    QGraphicsEllipseItem(QRectF, parent: QGraphicsItem = None)
    QGraphicsEllipseItem(float, float, float, float, parent: QGraphicsItem = None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> QRectF """
        pass

    def contains(self, Union, QPointF=None, QPoint=None): # real signature unknown; restored from __doc__
        """ contains(self, Union[QPointF, QPoint]) -> bool """
        return False

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ isObscuredBy(self, QGraphicsItem) -> bool """
        return False

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ opaqueArea(self) -> QPainterPath """
        pass

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None): # real signature unknown; restored from __doc__
        """ paint(self, QPainter, QStyleOptionGraphicsItem, widget: QWidget = None) """
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> QRectF """
        pass

    def setRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setRect(self, QRectF)
        setRect(self, float, float, float, float)
        """
        pass

    def setSpanAngle(self, p_int): # real signature unknown; restored from __doc__
        """ setSpanAngle(self, int) """
        pass

    def setStartAngle(self, p_int): # real signature unknown; restored from __doc__
        """ setStartAngle(self, int) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> QPainterPath """
        pass

    def spanAngle(self): # real signature unknown; restored from __doc__
        """ spanAngle(self) -> int """
        return 0

    def startAngle(self): # real signature unknown; restored from __doc__
        """ startAngle(self) -> int """
        return 0

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


