# encoding: utf-8
# module PyQt5.QtQuick
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtQuick.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import PyQt5.QtQml as __PyQt5_QtQml
import sip as __sip


from .QQuickWindow import QQuickWindow

class QQuickView(QQuickWindow):
    """
    QQuickView(parent: QWindow = None)
    QQuickView(QQmlEngine, QWindow)
    QQuickView(QUrl, parent: QWindow = None)
    """
    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> QQmlEngine """
        pass

    def errors(self): # real signature unknown; restored from __doc__
        """ errors(self) -> List[QQmlError] """
        return []

    def initialSize(self): # real signature unknown; restored from __doc__
        """ initialSize(self) -> QSize """
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyReleaseEvent(self, QKeyEvent) """
        pass

    def mouseMoveEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseMoveEvent(self, QMouseEvent) """
        pass

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QMouseEvent) """
        pass

    def mouseReleaseEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mouseReleaseEvent(self, QMouseEvent) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def resizeMode(self): # real signature unknown; restored from __doc__
        """ resizeMode(self) -> QQuickView.ResizeMode """
        pass

    def rootContext(self): # real signature unknown; restored from __doc__
        """ rootContext(self) -> QQmlContext """
        pass

    def rootObject(self): # real signature unknown; restored from __doc__
        """ rootObject(self) -> QQuickItem """
        return QQuickItem

    def setResizeMode(self, QQuickView_ResizeMode): # real signature unknown; restored from __doc__
        """ setResizeMode(self, QQuickView.ResizeMode) """
        pass

    def setSource(self, QUrl): # real signature unknown; restored from __doc__
        """ setSource(self, QUrl) """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> QUrl """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QQuickView.Status """
        pass

    def statusChanged(self, QQuickView_Status): # real signature unknown; restored from __doc__
        """ statusChanged(self, QQuickView.Status) [signal] """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Error = 3
    Loading = 2
    Null = 0
    Ready = 1
    SizeRootObjectToView = 1
    SizeViewToRootObject = 0


