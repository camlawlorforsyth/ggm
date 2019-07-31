"""A convenience module to import both the used Qt symbols from."""

import sip
sip.setapi('QDate', 2)
sip.setapi('QDateTime', 2)
sip.setapi('QString', 2)
sip.setapi('QTextStream', 2)
sip.setapi('QTime', 2)
sip.setapi('QUrl', 2)
sip.setapi('QVariant', 2)

from PyQt5.QtCore import pyqtSignal, QLineF, QPointF, QRectF
from PyQt5.QtGui import QPainterPath
from PyQt5.QtWidgets import QApplication, QCheckBox, QGraphicsEllipseItem, QGraphicsItem, QGraphicsPathItem, QGraphicsScene, QGraphicsView, QGridLayout, QLineEdit, QWidget
from PyQt5.uic import loadUi

