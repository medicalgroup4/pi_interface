# encoding: utf-8
# module PyQt5.QtMultimedia
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtMultimedia.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaRecorder import QMediaRecorder

class QAudioRecorder(QMediaRecorder):
    """ QAudioRecorder(parent: QObject = None) """
    def audioInput(self): # real signature unknown; restored from __doc__
        """ audioInput(self) -> str """
        return ""

    def audioInputChanged(self, p_str): # real signature unknown; restored from __doc__
        """ audioInputChanged(self, str) [signal] """
        pass

    def audioInputDescription(self, p_str): # real signature unknown; restored from __doc__
        """ audioInputDescription(self, str) -> str """
        return ""

    def audioInputs(self): # real signature unknown; restored from __doc__
        """ audioInputs(self) -> List[str] """
        return []

    def availableAudioInputsChanged(self): # real signature unknown; restored from __doc__
        """ availableAudioInputsChanged(self) [signal] """
        pass

    def defaultAudioInput(self): # real signature unknown; restored from __doc__
        """ defaultAudioInput(self) -> str """
        return ""

    def setAudioInput(self, p_str): # real signature unknown; restored from __doc__
        """ setAudioInput(self, str) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


