#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Copyright 2009 Piotr Maliński, riklaunim@gmail.com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

qapp = QApplication(sys.argv)

view = QWebView()
view.load(QUrl('test.html'))
view.show()

sys.exit(qapp.exec_())