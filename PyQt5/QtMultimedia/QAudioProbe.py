# encoding: utf-8
# module PyQt5.QtMultimedia
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtMultimedia.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QAudioProbe(__PyQt5_QtCore.QObject):
    """ QAudioProbe(parent: QObject = None) """
    def audioBufferProbed(self, QAudioBuffer): # real signature unknown; restored from __doc__
        """ audioBufferProbed(self, QAudioBuffer) [signal] """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) [signal] """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def setSource(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setSource(self, QMediaObject) -> bool
        setSource(self, QMediaRecorder) -> bool
        """
        return False

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


