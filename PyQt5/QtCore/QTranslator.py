# encoding: utf-8
# module PyQt5.QtCore
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtCore.so
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QTranslator(QObject):
    """ QTranslator(parent: QObject = None) """
    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, str, directory: str = '', searchDelimiters: str = '', suffix: str = '') -> bool
        load(self, QLocale, str, prefix: str = '', directory: str = '', suffix: str = '') -> bool
        """
        return False

    def loadFromData(self, bytes, directory=''): # real signature unknown; restored from __doc__
        """ loadFromData(self, bytes, directory: str = '') -> bool """
        return False

    def translate(self, p_str, p_str_1, disambiguation=None, n=-1): # real signature unknown; restored from __doc__
        """ translate(self, str, str, disambiguation: str = None, n: int = -1) -> str """
        return ""

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


