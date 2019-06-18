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


class QQuickTextureFactory(__PyQt5_QtCore.QObject):
    """ QQuickTextureFactory() """
    def createTexture(self, QQuickWindow): # real signature unknown; restored from __doc__
        """ createTexture(self, QQuickWindow) -> QSGTexture """
        return QSGTexture

    def image(self): # real signature unknown; restored from __doc__
        """ image(self) -> QImage """
        pass

    def textureByteCount(self): # real signature unknown; restored from __doc__
        """ textureByteCount(self) -> int """
        return 0

    def textureFactoryForImage(self, QImage): # real signature unknown; restored from __doc__
        """ textureFactoryForImage(QImage) -> QQuickTextureFactory """
        return QQuickTextureFactory

    def textureSize(self): # real signature unknown; restored from __doc__
        """ textureSize(self) -> QSize """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


