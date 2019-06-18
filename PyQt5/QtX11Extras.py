# encoding: utf-8
# module PyQt5.QtX11Extras
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtX11Extras.so
# by generator 1.147
# no doc

# imports
import sip as __sip


# no functions
# classes

class Display(__sip.simplewrapper):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QX11Info(__sip.simplewrapper):
    """ QX11Info(QX11Info) """
    def appDpiX(self, screen=-1): # real signature unknown; restored from __doc__
        """ appDpiX(screen: int = -1) -> int """
        return 0

    def appDpiY(self, screen=-1): # real signature unknown; restored from __doc__
        """ appDpiY(screen: int = -1) -> int """
        return 0

    def appRootWindow(self, screen=-1): # real signature unknown; restored from __doc__
        """ appRootWindow(screen: int = -1) -> int """
        return 0

    def appScreen(self): # real signature unknown; restored from __doc__
        """ appScreen() -> int """
        return 0

    def appTime(self): # real signature unknown; restored from __doc__
        """ appTime() -> int """
        return 0

    def appUserTime(self): # real signature unknown; restored from __doc__
        """ appUserTime() -> int """
        return 0

    def connection(self): # real signature unknown; restored from __doc__
        """ connection() -> xcb_connection_t """
        return xcb_connection_t

    def display(self): # real signature unknown; restored from __doc__
        """ display() -> Display """
        return Display

    def getTimestamp(self): # real signature unknown; restored from __doc__
        """ getTimestamp() -> int """
        return 0

    def isPlatformX11(self): # real signature unknown; restored from __doc__
        """ isPlatformX11() -> bool """
        return False

    def nextStartupId(self): # real signature unknown; restored from __doc__
        """ nextStartupId() -> QByteArray """
        pass

    def setAppTime(self, p_int): # real signature unknown; restored from __doc__
        """ setAppTime(int) """
        pass

    def setAppUserTime(self, p_int): # real signature unknown; restored from __doc__
        """ setAppUserTime(int) """
        pass

    def setNextStartupId(self, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ setNextStartupId(Union[QByteArray, bytes, bytearray]) """
        pass

    def __init__(self, QX11Info): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class xcb_connection_t(__sip.simplewrapper):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values



