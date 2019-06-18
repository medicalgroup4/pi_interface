# encoding: utf-8
# module PyQt5.QtCore
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtCore.so
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QPluginLoader(QObject):
    """
    QPluginLoader(parent: QObject = None)
    QPluginLoader(str, parent: QObject = None)
    """
    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def instance(self): # real signature unknown; restored from __doc__
        """ instance(self) -> QObject """
        return QObject

    def isLoaded(self): # real signature unknown; restored from __doc__
        """ isLoaded(self) -> bool """
        return False

    def load(self): # real signature unknown; restored from __doc__
        """ load(self) -> bool """
        return False

    def loadHints(self): # real signature unknown; restored from __doc__
        """ loadHints(self) -> QLibrary.LoadHints """
        pass

    def setFileName(self, p_str): # real signature unknown; restored from __doc__
        """ setFileName(self, str) """
        pass

    def setLoadHints(self, Union, QLibrary_LoadHints=None, QLibrary_LoadHint=None): # real signature unknown; restored from __doc__
        """ setLoadHints(self, Union[QLibrary.LoadHints, QLibrary.LoadHint]) """
        pass

    def staticInstances(self): # real signature unknown; restored from __doc__
        """ staticInstances() -> List[QObject] """
        return []

    def unload(self): # real signature unknown; restored from __doc__
        """ unload(self) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


