# -*- coding: utf-8 -*-
#
# This file is part of Invenio Demosite.
# Copyright (C) 2012, 2013, 2015 CERN.
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
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.


from fixture import DataSet

from invenio.config import CFG_SITE_ADMIN_EMAIL

from invenio_groups.models import PrivacyPolicy, SubscriptionPolicy, \
    MembershipState


class UserData(DataSet):
    class admin:
        id = 1
        email = CFG_SITE_ADMIN_EMAIL
        password = ''
        note = '1'
        nickname = 'admin'

    class jekyll:
        id = 2
        email = 'jekyll@cds.cern.ch'
        password = 'j123ekyll'
        note = '1'
        nickname = 'jekyll'

    class hyde:
        id = 3
        email = 'hyde@cds.cern.ch'
        password = 'h123yde'
        note = '1'
        nickname = 'hyde'

    class dorian:
        id = 4
        email = 'dorian.gray@cds.cern.ch'
        password = 'd123orian'
        note = '1'
        nickname = 'dorian'

    class romeo:
        id = 5
        email = 'romeo.montague@cds.cern.ch'
        password = 'r123omeo'
        note = '1'
        nickname = 'romeo'

    class juliet:
        id = 6
        email = 'juliet.capulet@cds.cern.ch'
        password = 'j123uliet'
        note = '1'
        nickname = 'juliet'

    class benvolio:
        id = 7
        email = 'benvolio.montague@cds.cern.ch'
        password = 'b123envolio'
        note = '1'
        nickname = 'benvolio'

    class balthasar:
        id = 8
        email = 'balthasar.montague@cds.cern.ch'
        password = 'b123althasar'
        note = '1'
        nickname = 'balthasar'


class GroupData(DataSet):

    class thesesViewers:
        id = 1
        name = 'Theses viewers'
        description = 'Theses viewers internal group'
        is_managed = False
        privacy_policy = PrivacyPolicy.ADMINS
        subscription_policy = SubscriptionPolicy.CLOSED

    class montagueFamily:
        id = 2
        name = 'montague-family'
        description = 'The Montague family.'
        is_managed = False
        privacy_policy = PrivacyPolicy.ADMINS
        subscription_policy = SubscriptionPolicy.CLOSED


class MembershipData(DataSet):

    class jekyllThesesViewers:
        user = UserData.jekyll
        group = GroupData.thesesViewers
        state = MembershipState.ACTIVE

    class julietMontagueFamily:
        user = UserData.juliet
        group = GroupData.montagueFamily
        state = MembershipState.ACTIVE

    class benvolioMontagueFamily:
        user = UserData.benvolio
        group = GroupData.montagueFamily
        state = MembershipState.ACTIVE


class GroupAdminData(DataSet):

    class romeoMontagueFamily:
        group = GroupData.montagueFamily
        admin = UserData.romeo

    class romeoThesesViewers:
        group = GroupData.thesesViewers
        admin = UserData.romeo

__all__ = ('UserData', 'GroupData', 'MembershipData', 'GroupAdminData')
