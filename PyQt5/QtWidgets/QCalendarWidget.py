# encoding: utf-8
# module PyQt5.QtWidgets
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtWidgets.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QWidget import QWidget

class QCalendarWidget(QWidget):
    """ QCalendarWidget(parent: QWidget = None) """
    def activated(self, Union, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ activated(self, Union[QDate, datetime.date]) [signal] """
        pass

    def clicked(self, Union, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ clicked(self, Union[QDate, datetime.date]) [signal] """
        pass

    def currentPageChanged(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ currentPageChanged(self, int, int) [signal] """
        pass

    def dateEditAcceptDelay(self): # real signature unknown; restored from __doc__
        """ dateEditAcceptDelay(self) -> int """
        return 0

    def dateTextFormat(self, Union=None, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        dateTextFormat(self) -> Dict[QDate, QTextCharFormat]
        dateTextFormat(self, Union[QDate, datetime.date]) -> QTextCharFormat
        """
        return {}

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ eventFilter(self, QObject, QEvent) -> bool """
        return False

    def firstDayOfWeek(self): # real signature unknown; restored from __doc__
        """ firstDayOfWeek(self) -> Qt.DayOfWeek """
        pass

    def headerTextFormat(self): # real signature unknown; restored from __doc__
        """ headerTextFormat(self) -> QTextCharFormat """
        pass

    def horizontalHeaderFormat(self): # real signature unknown; restored from __doc__
        """ horizontalHeaderFormat(self) -> QCalendarWidget.HorizontalHeaderFormat """
        pass

    def isDateEditEnabled(self): # real signature unknown; restored from __doc__
        """ isDateEditEnabled(self) -> bool """
        return False

    def isGridVisible(self): # real signature unknown; restored from __doc__
        """ isGridVisible(self) -> bool """
        return False

    def isNavigationBarVisible(self): # real signature unknown; restored from __doc__
        """ isNavigationBarVisible(self) -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, QKeyEvent) """
        pass

    def maximumDate(self): # real signature unknown; restored from __doc__
        """ maximumDate(self) -> QDate """
        pass

    def minimumDate(self): # real signature unknown; restored from __doc__
        """ minimumDate(self) -> QDate """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> QSize """
        pass

    def monthShown(self): # real signature unknown; restored from __doc__
        """ monthShown(self) -> int """
        return 0

    def mousePressEvent(self, QMouseEvent): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, QMouseEvent) """
        pass

    def paintCell(self, QPainter, QRect, Union, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ paintCell(self, QPainter, QRect, Union[QDate, datetime.date]) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ resizeEvent(self, QResizeEvent) """
        pass

    def selectedDate(self): # real signature unknown; restored from __doc__
        """ selectedDate(self) -> QDate """
        pass

    def selectionChanged(self): # real signature unknown; restored from __doc__
        """ selectionChanged(self) [signal] """
        pass

    def selectionMode(self): # real signature unknown; restored from __doc__
        """ selectionMode(self) -> QCalendarWidget.SelectionMode """
        pass

    def setCurrentPage(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setCurrentPage(self, int, int) """
        pass

    def setDateEditAcceptDelay(self, p_int): # real signature unknown; restored from __doc__
        """ setDateEditAcceptDelay(self, int) """
        pass

    def setDateEditEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setDateEditEnabled(self, bool) """
        pass

    def setDateRange(self, Union, QDate=None, datetime_date=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setDateRange(self, Union[QDate, datetime.date], Union[QDate, datetime.date]) """
        pass

    def setDateTextFormat(self, Union, QDate=None, datetime_date=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setDateTextFormat(self, Union[QDate, datetime.date], QTextCharFormat) """
        pass

    def setFirstDayOfWeek(self, Qt_DayOfWeek): # real signature unknown; restored from __doc__
        """ setFirstDayOfWeek(self, Qt.DayOfWeek) """
        pass

    def setGridVisible(self, bool): # real signature unknown; restored from __doc__
        """ setGridVisible(self, bool) """
        pass

    def setHeaderTextFormat(self, QTextCharFormat): # real signature unknown; restored from __doc__
        """ setHeaderTextFormat(self, QTextCharFormat) """
        pass

    def setHorizontalHeaderFormat(self, QCalendarWidget_HorizontalHeaderFormat): # real signature unknown; restored from __doc__
        """ setHorizontalHeaderFormat(self, QCalendarWidget.HorizontalHeaderFormat) """
        pass

    def setMaximumDate(self, Union, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ setMaximumDate(self, Union[QDate, datetime.date]) """
        pass

    def setMinimumDate(self, Union, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ setMinimumDate(self, Union[QDate, datetime.date]) """
        pass

    def setNavigationBarVisible(self, bool): # real signature unknown; restored from __doc__
        """ setNavigationBarVisible(self, bool) """
        pass

    def setSelectedDate(self, Union, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ setSelectedDate(self, Union[QDate, datetime.date]) """
        pass

    def setSelectionMode(self, QCalendarWidget_SelectionMode): # real signature unknown; restored from __doc__
        """ setSelectionMode(self, QCalendarWidget.SelectionMode) """
        pass

    def setVerticalHeaderFormat(self, QCalendarWidget_VerticalHeaderFormat): # real signature unknown; restored from __doc__
        """ setVerticalHeaderFormat(self, QCalendarWidget.VerticalHeaderFormat) """
        pass

    def setWeekdayTextFormat(self, Qt_DayOfWeek, QTextCharFormat): # real signature unknown; restored from __doc__
        """ setWeekdayTextFormat(self, Qt.DayOfWeek, QTextCharFormat) """
        pass

    def showNextMonth(self): # real signature unknown; restored from __doc__
        """ showNextMonth(self) """
        pass

    def showNextYear(self): # real signature unknown; restored from __doc__
        """ showNextYear(self) """
        pass

    def showPreviousMonth(self): # real signature unknown; restored from __doc__
        """ showPreviousMonth(self) """
        pass

    def showPreviousYear(self): # real signature unknown; restored from __doc__
        """ showPreviousYear(self) """
        pass

    def showSelectedDate(self): # real signature unknown; restored from __doc__
        """ showSelectedDate(self) """
        pass

    def showToday(self): # real signature unknown; restored from __doc__
        """ showToday(self) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def updateCell(self, Union, QDate=None, datetime_date=None): # real signature unknown; restored from __doc__
        """ updateCell(self, Union[QDate, datetime.date]) """
        pass

    def updateCells(self): # real signature unknown; restored from __doc__
        """ updateCells(self) """
        pass

    def verticalHeaderFormat(self): # real signature unknown; restored from __doc__
        """ verticalHeaderFormat(self) -> QCalendarWidget.VerticalHeaderFormat """
        pass

    def weekdayTextFormat(self, Qt_DayOfWeek): # real signature unknown; restored from __doc__
        """ weekdayTextFormat(self, Qt.DayOfWeek) -> QTextCharFormat """
        pass

    def yearShown(self): # real signature unknown; restored from __doc__
        """ yearShown(self) -> int """
        return 0

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    ISOWeekNumbers = 1
    LongDayNames = 3
    NoHorizontalHeader = 0
    NoSelection = 0
    NoVerticalHeader = 0
    ShortDayNames = 2
    SingleLetterDayNames = 1
    SingleSelection = 1


