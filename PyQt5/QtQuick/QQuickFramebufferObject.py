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

class QQuickFramebufferObject(QQuickItem):
    """ QQuickFramebufferObject(parent: QQuickItem = None) """
    def createRenderer(self): # real signature unknown; restored from __doc__
        """ createRenderer(self) -> QQuickFramebufferObject.Renderer """
        pass

    def geometryChanged(self, QRectF, QRectF_1): # real signature unknown; restored from __doc__
        """ geometryChanged(self, QRectF, QRectF) """
        pass

    def isTextureProvider(self): # real signature unknown; restored from __doc__
        """ isTextureProvider(self) -> bool """
        return False

    def mirrorVertically(self): # real signature unknown; restored from __doc__
        """ mirrorVertically(self) -> bool """
        return False

    def mirrorVerticallyChanged(self, bool): # real signature unknown; restored from __doc__
        """ mirrorVerticallyChanged(self, bool) [signal] """
        pass

    def releaseResources(self): # real signature unknown; restored from __doc__
        """ releaseResources(self) """
        pass

    def setMirrorVertically(self, bool): # real signature unknown; restored from __doc__
        """ setMirrorVertically(self, bool) """
        pass

    def setTextureFollowsItemSize(self, bool): # real signature unknown; restored from __doc__
        """ setTextureFollowsItemSize(self, bool) """
        pass

    def textureFollowsItemSize(self): # real signature unknown; restored from __doc__
        """ textureFollowsItemSize(self) -> bool """
        return False

    def textureFollowsItemSizeChanged(self, bool): # real signature unknown; restored from __doc__
        """ textureFollowsItemSizeChanged(self, bool) [signal] """
        pass

    def textureProvider(self): # real signature unknown; restored from __doc__
        """ textureProvider(self) -> QSGTextureProvider """
        return QSGTextureProvider

    def updatePaintNode(self, QSGNode, QQuickItem_UpdatePaintNodeData): # real signature unknown; restored from __doc__
        """ updatePaintNode(self, QSGNode, QQuickItem.UpdatePaintNodeData) -> QSGNode """
        return QSGNode

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass



