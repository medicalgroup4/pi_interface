# encoding: utf-8
# module PyQt5.QtGui
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtGui.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QTextFrame import QTextFrame

class QTextTable(QTextFrame):
    """ QTextTable(QTextDocument) """
    def appendColumns(self, p_int): # real signature unknown; restored from __doc__
        """ appendColumns(self, int) """
        pass

    def appendRows(self, p_int): # real signature unknown; restored from __doc__
        """ appendRows(self, int) """
        pass

    def cellAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        cellAt(self, int, int) -> QTextTableCell
        cellAt(self, int) -> QTextTableCell
        cellAt(self, QTextCursor) -> QTextTableCell
        """
        return QTextTableCell

    def columns(self): # real signature unknown; restored from __doc__
        """ columns(self) -> int """
        return 0

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> QTextTableFormat """
        return QTextTableFormat

    def insertColumns(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ insertColumns(self, int, int) """
        pass

    def insertRows(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ insertRows(self, int, int) """
        pass

    def mergeCells(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        mergeCells(self, int, int, int, int)
        mergeCells(self, QTextCursor)
        """
        pass

    def removeColumns(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ removeColumns(self, int, int) """
        pass

    def removeRows(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ removeRows(self, int, int) """
        pass

    def resize(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ resize(self, int, int) """
        pass

    def rowEnd(self, QTextCursor): # real signature unknown; restored from __doc__
        """ rowEnd(self, QTextCursor) -> QTextCursor """
        return QTextCursor

    def rows(self): # real signature unknown; restored from __doc__
        """ rows(self) -> int """
        return 0

    def rowStart(self, QTextCursor): # real signature unknown; restored from __doc__
        """ rowStart(self, QTextCursor) -> QTextCursor """
        return QTextCursor

    def setFormat(self, QTextTableFormat): # real signature unknown; restored from __doc__
        """ setFormat(self, QTextTableFormat) """
        pass

    def splitCell(self, p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
        """ splitCell(self, int, int, int, int) """
        pass

    def __init__(self, QTextDocument): # real signature unknown; restored from __doc__
        pass

