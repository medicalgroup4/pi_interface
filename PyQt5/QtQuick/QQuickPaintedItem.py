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


from .QQuickItem import QQuickItem

class QQuickPaintedItem(QQuickItem):
    """ QQuickPaintedItem(parent: QQuickItem = None) """
    def antialiasing(self): # real signature unknown; restored from __doc__
        """ antialiasing(self) -> bool """
        return False

    def contentsBoundingRect(self): # real signature unknown; restored from __doc__
        """ contentsBoundingRect(self) -> QRectF """
        pass

    def contentsScale(self): # real signature unknown; restored from __doc__
        """ contentsScale(self) -> float """
        return 0.0

    def contentsScaleChanged(self): # real signature unknown; restored from __doc__
        """ contentsScaleChanged(self) [signal] """
        pass

    def contentsSize(self): # real signature unknown; restored from __doc__
        """ contentsSize(self) -> QSize """
        pass

    def contentsSizeChanged(self): # real signature unknown; restored from __doc__
        """ contentsSizeChanged(self) [signal] """
        pass

    def fillColor(self): # real signature unknown; restored from __doc__
        """ fillColor(self) -> QColor """
        pass

    def fillColorChanged(self): # real signature unknown; restored from __doc__
        """ fillColorChanged(self) [signal] """
        pass

    def isTextureProvider(self): # real signature unknown; restored from __doc__
        """ isTextureProvider(self) -> bool """
        return False

    def itemChange(self, QQuickItem_ItemChange, QQuickItem_ItemChangeData): # real signature unknown; restored from __doc__
        """ itemChange(self, QQuickItem.ItemChange, QQuickItem.ItemChangeData) """
        pass

    def mipmap(self): # real signature unknown; restored from __doc__
        """ mipmap(self) -> bool """
        return False

    def opaquePainting(self): # real signature unknown; restored from __doc__
        """ opaquePainting(self) -> bool """
        return False

    def paint(self, QPainter): # real signature unknown; restored from __doc__
        """ paint(self, QPainter) """
        pass

    def performanceHints(self): # real signature unknown; restored from __doc__
        """ performanceHints(self) -> QQuickPaintedItem.PerformanceHints """
        pass

    def releaseResources(self): # real signature unknown; restored from __doc__
        """ releaseResources(self) """
        pass

    def renderTarget(self): # real signature unknown; restored from __doc__
        """ renderTarget(self) -> QQuickPaintedItem.RenderTarget """
        pass

    def renderTargetChanged(self): # real signature unknown; restored from __doc__
        """ renderTargetChanged(self) [signal] """
        pass

    def resetContentsSize(self): # real signature unknown; restored from __doc__
        """ resetContentsSize(self) """
        pass

    def setAntialiasing(self, bool): # real signature unknown; restored from __doc__
        """ setAntialiasing(self, bool) """
        pass

    def setContentsScale(self, p_float): # real signature unknown; restored from __doc__
        """ setContentsScale(self, float) """
        pass

    def setContentsSize(self, QSize): # real signature unknown; restored from __doc__
        """ setContentsSize(self, QSize) """
        pass

    def setFillColor(self, Union, QColor=None, Qt_GlobalColor=None): # real signature unknown; restored from __doc__
        """ setFillColor(self, Union[QColor, Qt.GlobalColor]) """
        pass

    def setMipmap(self, bool): # real signature unknown; restored from __doc__
        """ setMipmap(self, bool) """
        pass

    def setOpaquePainting(self, bool): # real signature unknown; restored from __doc__
        """ setOpaquePainting(self, bool) """
        pass

    def setPerformanceHint(self, QQuickPaintedItem_PerformanceHint, enabled=True): # real signature unknown; restored from __doc__
        """ setPerformanceHint(self, QQuickPaintedItem.PerformanceHint, enabled: bool = True) """
        pass

    def setPerformanceHints(self, Union, QQuickPaintedItem_PerformanceHints=None, QQuickPaintedItem_PerformanceHint=None): # real signature unknown; restored from __doc__
        """ setPerformanceHints(self, Union[QQuickPaintedItem.PerformanceHints, QQuickPaintedItem.PerformanceHint]) """
        pass

    def setRenderTarget(self, QQuickPaintedItem_RenderTarget): # real signature unknown; restored from __doc__
        """ setRenderTarget(self, QQuickPaintedItem.RenderTarget) """
        pass

    def setTextureSize(self, QSize): # real signature unknown; restored from __doc__
        """ setTextureSize(self, QSize) """
        pass

    def textureProvider(self): # real signature unknown; restored from __doc__
        """ textureProvider(self) -> QSGTextureProvider """
        return QSGTextureProvider

    def textureSize(self): # real signature unknown; restored from __doc__
        """ textureSize(self) -> QSize """
        pass

    def textureSizeChanged(self): # real signature unknown; restored from __doc__
        """ textureSizeChanged(self) [signal] """
        pass

    def update(self, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ update(self, rect: QRect = QRect()) """
        pass

    def updatePaintNode(self, QSGNode, QQuickItem_UpdatePaintNodeData): # real signature unknown; restored from __doc__
        """ updatePaintNode(self, QSGNode, QQuickItem.UpdatePaintNodeData) -> QSGNode """
        return QSGNode

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    FastFBOResizing = 1
    FramebufferObject = 1
    Image = 0
    InvertedYFramebufferObject = 2


