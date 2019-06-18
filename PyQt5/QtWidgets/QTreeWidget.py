# encoding: utf-8
# module PyQt5.QtWidgets
# from /home/noah/PycharmProjects/pi_interface/venv/lib/python3.6/site-packages/PyQt5/QtWidgets.so
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QTreeView import QTreeView

class QTreeWidget(QTreeView):
    """ QTreeWidget(parent: QWidget = None) """
    def addTopLevelItem(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ addTopLevelItem(self, QTreeWidgetItem) """
        pass

    def addTopLevelItems(self, Iterable, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ addTopLevelItems(self, Iterable[QTreeWidgetItem]) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def closePersistentEditor(self, QTreeWidgetItem, column=0): # real signature unknown; restored from __doc__
        """ closePersistentEditor(self, QTreeWidgetItem, column: int = 0) """
        pass

    def collapseItem(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ collapseItem(self, QTreeWidgetItem) """
        pass

    def columnCount(self): # real signature unknown; restored from __doc__
        """ columnCount(self) -> int """
        return 0

    def currentColumn(self): # real signature unknown; restored from __doc__
        """ currentColumn(self) -> int """
        return 0

    def currentItem(self): # real signature unknown; restored from __doc__
        """ currentItem(self) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def currentItemChanged(self, QTreeWidgetItem, QTreeWidgetItem_1): # real signature unknown; restored from __doc__
        """ currentItemChanged(self, QTreeWidgetItem, QTreeWidgetItem) [signal] """
        pass

    def dropEvent(self, QDropEvent): # real signature unknown; restored from __doc__
        """ dropEvent(self, QDropEvent) """
        pass

    def dropMimeData(self, QTreeWidgetItem, p_int, QMimeData, Qt_DropAction): # real signature unknown; restored from __doc__
        """ dropMimeData(self, QTreeWidgetItem, int, QMimeData, Qt.DropAction) -> bool """
        return False

    def editItem(self, QTreeWidgetItem, column=0): # real signature unknown; restored from __doc__
        """ editItem(self, QTreeWidgetItem, column: int = 0) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def expandItem(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ expandItem(self, QTreeWidgetItem) """
        pass

    def findItems(self, p_str, Union, Qt_MatchFlags=None, Qt_MatchFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ findItems(self, str, Union[Qt.MatchFlags, Qt.MatchFlag], column: int = 0) -> List[QTreeWidgetItem] """
        pass

    def headerItem(self): # real signature unknown; restored from __doc__
        """ headerItem(self) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def indexFromItem(self, QTreeWidgetItem, column=0): # real signature unknown; restored from __doc__
        """ indexFromItem(self, QTreeWidgetItem, column: int = 0) -> QModelIndex """
        pass

    def indexOfTopLevelItem(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ indexOfTopLevelItem(self, QTreeWidgetItem) -> int """
        return 0

    def insertTopLevelItem(self, p_int, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ insertTopLevelItem(self, int, QTreeWidgetItem) """
        pass

    def insertTopLevelItems(self, p_int, Iterable, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ insertTopLevelItems(self, int, Iterable[QTreeWidgetItem]) """
        pass

    def invisibleRootItem(self): # real signature unknown; restored from __doc__
        """ invisibleRootItem(self) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def isFirstItemColumnSpanned(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ isFirstItemColumnSpanned(self, QTreeWidgetItem) -> bool """
        return False

    def isPersistentEditorOpen(self, QTreeWidgetItem, column=0): # real signature unknown; restored from __doc__
        """ isPersistentEditorOpen(self, QTreeWidgetItem, column: int = 0) -> bool """
        return False

    def itemAbove(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ itemAbove(self, QTreeWidgetItem) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def itemActivated(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ itemActivated(self, QTreeWidgetItem, int) [signal] """
        pass

    def itemAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        itemAt(self, QPoint) -> QTreeWidgetItem
        itemAt(self, int, int) -> QTreeWidgetItem
        """
        return QTreeWidgetItem

    def itemBelow(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ itemBelow(self, QTreeWidgetItem) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def itemChanged(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ itemChanged(self, QTreeWidgetItem, int) [signal] """
        pass

    def itemClicked(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ itemClicked(self, QTreeWidgetItem, int) [signal] """
        pass

    def itemCollapsed(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ itemCollapsed(self, QTreeWidgetItem) [signal] """
        pass

    def itemDoubleClicked(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ itemDoubleClicked(self, QTreeWidgetItem, int) [signal] """
        pass

    def itemEntered(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ itemEntered(self, QTreeWidgetItem, int) [signal] """
        pass

    def itemExpanded(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ itemExpanded(self, QTreeWidgetItem) [signal] """
        pass

    def itemFromIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ itemFromIndex(self, QModelIndex) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def itemPressed(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ itemPressed(self, QTreeWidgetItem, int) [signal] """
        pass

    def itemSelectionChanged(self): # real signature unknown; restored from __doc__
        """ itemSelectionChanged(self) [signal] """
        pass

    def itemWidget(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ itemWidget(self, QTreeWidgetItem, int) -> QWidget """
        return QWidget

    def mimeData(self, Iterable, QTreeWidgetItem=None): # real signature unknown; restored from __doc__
        """ mimeData(self, Iterable[QTreeWidgetItem]) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ mimeTypes(self) -> List[str] """
        return []

    def openPersistentEditor(self, QTreeWidgetItem, column=0): # real signature unknown; restored from __doc__
        """ openPersistentEditor(self, QTreeWidgetItem, column: int = 0) """
        pass

    def removeItemWidget(self, QTreeWidgetItem, p_int): # real signature unknown; restored from __doc__
        """ removeItemWidget(self, QTreeWidgetItem, int) """
        pass

    def scrollToItem(self, QTreeWidgetItem, hint=None): # real signature unknown; restored from __doc__
        """ scrollToItem(self, QTreeWidgetItem, hint: QAbstractItemView.ScrollHint = QAbstractItemView.EnsureVisible) """
        pass

    def selectedItems(self): # real signature unknown; restored from __doc__
        """ selectedItems(self) -> List[QTreeWidgetItem] """
        return []

    def setColumnCount(self, p_int): # real signature unknown; restored from __doc__
        """ setColumnCount(self, int) """
        pass

    def setCurrentItem(self, QTreeWidgetItem, p_int=None, Union=None, QItemSelectionModel_SelectionFlags=None, QItemSelectionModel_SelectionFlag=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setCurrentItem(self, QTreeWidgetItem)
        setCurrentItem(self, QTreeWidgetItem, int)
        setCurrentItem(self, QTreeWidgetItem, int, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag])
        """
        pass

    def setFirstItemColumnSpanned(self, QTreeWidgetItem, bool): # real signature unknown; restored from __doc__
        """ setFirstItemColumnSpanned(self, QTreeWidgetItem, bool) """
        pass

    def setHeaderItem(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ setHeaderItem(self, QTreeWidgetItem) """
        pass

    def setHeaderLabel(self, p_str): # real signature unknown; restored from __doc__
        """ setHeaderLabel(self, str) """
        pass

    def setHeaderLabels(self, Iterable, p_str=None): # real signature unknown; restored from __doc__
        """ setHeaderLabels(self, Iterable[str]) """
        pass

    def setItemWidget(self, QTreeWidgetItem, p_int, QWidget): # real signature unknown; restored from __doc__
        """ setItemWidget(self, QTreeWidgetItem, int, QWidget) """
        pass

    def setModel(self, *args, **kwargs): # real signature unknown
        pass

    def setSelectionModel(self, QItemSelectionModel): # real signature unknown; restored from __doc__
        """ setSelectionModel(self, QItemSelectionModel) """
        pass

    def sortColumn(self): # real signature unknown; restored from __doc__
        """ sortColumn(self) -> int """
        return 0

    def sortItems(self, p_int, Qt_SortOrder): # real signature unknown; restored from __doc__
        """ sortItems(self, int, Qt.SortOrder) """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ supportedDropActions(self) -> Qt.DropActions """
        pass

    def takeTopLevelItem(self, p_int): # real signature unknown; restored from __doc__
        """ takeTopLevelItem(self, int) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def topLevelItem(self, p_int): # real signature unknown; restored from __doc__
        """ topLevelItem(self, int) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def topLevelItemCount(self): # real signature unknown; restored from __doc__
        """ topLevelItemCount(self) -> int """
        return 0

    def visualItemRect(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ visualItemRect(self, QTreeWidgetItem) -> QRect """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


