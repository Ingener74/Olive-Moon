# -*- coding: utf-8 -*-

# Resource object code
#
# Created: чт янв 14 14:07:53 2016
#      by: The Resource Compiler for PySide (Qt v4.8.4)
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore

qt_resource_name = "\x00\x07\x0a\xc1W\xa7\x00s\x00u\x00n\x00.\x00p\x00n\x00g"
qt_resource_struct = "\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00"
def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()