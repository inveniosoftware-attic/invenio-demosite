# -*- coding: utf-8 -*-
#
# This file is part of Invenio Demosite.
# Copyright (C) 2014 CERN.
#
# Invenio Demosite is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio Demosite is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02D111-1307, USA.

from invenio.base.config import PACKAGES as _PACKAGES

PACKAGES = [
    "invenio_demosite.base",
    "invenio_demosite.modules.*",
] + _PACKAGES

DEPOSIT_TYPES = [
    'invenio_demosite.modules.deposit.workflows.article.article',
]
