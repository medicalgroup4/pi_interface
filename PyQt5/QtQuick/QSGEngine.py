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


class QSGEngine(__PyQt5_QtCore.QObject):
    """ QSGEngine(parent: QObject = None) """
    def createImageNode(self): # real signature unknown; restored from __doc__
        """ createImageNode(self) -> QSGImageNode """
        return QSGImageNode

    def createRectangleNode(self): # real signature unknown; restored from __doc__
        """ createRectangleNode(self) -> QSGRectangleNode """
        return QSGRectangleNode

    def createRenderer(self): # real signature unknown; restored from __doc__
        """ createRenderer(self) -> QSGAbstractRenderer """
        return QSGAbstractRenderer

    def createTextureFromId(self, p_int, QSize, options, QSGEngine_CreateTextureOptions=None, QSGEngine_CreateTextureOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createTextureFromId(self, int, QSize, options: Union[QSGEngine.CreateTextureOptions, QSGEngine.CreateTextureOption] = QSGEngine.CreateTextureOption()) -> QSGTexture """
        pass

    def createTextureFromImage(self, QImage, options, QSGEngine_CreateTextureOptions=None, QSGEngine_CreateTextureOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createTextureFromImage(self, QImage, options: Union[QSGEngine.CreateTextureOptions, QSGEngine.CreateTextureOption] = QSGEngine.CreateTextureOption()) -> QSGTexture """
        pass

    def initialize(self, QOpenGLContext): # real signature unknown; restored from __doc__
        """ initialize(self, QOpenGLContext) """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def rendererInterface(self): # real signature unknown; restored from __doc__
        """ rendererInterface(self) -> QSGRendererInterface """
        return QSGRendererInterface

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    TextureCanUseAtlas = 8
    TextureHasAlphaChannel = 1
    TextureIsOpaque = 16
    TextureOwnsGLTexture = 4


