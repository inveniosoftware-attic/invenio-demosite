# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2014 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Access module configuration values."""

from invenio.modules.access.local_config import VIEWRESTRCOLL

# Demo site roles
DEF_DEMO_ROLES = (
    ('photocurator', 'Photo collection curator', 'deny any'),
    ('thesesviewer', 'Theses and Drafts viewer',
     'allow group "Theses and Drafts viewers"'),
    ('ALEPHviewer', 'ALEPH viewer',
     'allow group "ALEPH viewers"'),
    ('ISOLDEnotesviewer', 'ISOLDE Internal Notes viewer',
     'allow group "ISOLDE Internal Notes viewers"'),
    ('thesescurator', 'Theses collection curator', 'deny any'),
    ('swordcurator', 'BibSword client curator', 'deny any'),
    ('referee_DEMOBOO_*', 'Book collection curator', 'deny any'),
    ('restrictedpicturesviewer',
    'Restricted pictures viewer', 'deny any'),
    ('curator', 'Curator', 'deny any'),
    ('basketusers', 'Users who can use baskets',
    'deny email "hyde@cds.cern.ch"\nallow any'),
    ('claimpaperusers', 'Users who can perform changes to their own paper '
     'attributions without the need for an operator\'s approval',
     'deny email "hyde@cds.cern.ch"\nallow any'),
    ('submit_DEMOJRN_*',
     'Users who can submit (and modify) "Atlantis Times" articles',
     'deny all'),
    ('atlantiseditor',
     'Users who can configure "Atlantis Times" journal', 'deny all'),
    ('commentmoderator',
     'Users who can moderate comments', 'deny all'),
    ('poetrycommentreader', 'Users who can view comments in Poetry collection',
     'deny all'))

DEF_DEMO_USER_ROLES = (('jekyll@cds.cern.ch', 'thesesviewer'),
                       ('balthasar.montague@cds.cern.ch', 'ALEPHviewer'),
                       ('dorian.gray@cds.cern.ch', 'ISOLDEnotesviewer'),
                       ('jekyll@cds.cern.ch', 'swordcurator'),
                       ('jekyll@cds.cern.ch', 'claimpaperusers'),
                       ('dorian.gray@cds.cern.ch', 'referee_DEMOBOO_*'),
                       ('balthasar.montague@cds.cern.ch', 'curator'),
                       ('romeo.montague@cds.cern.ch',
                        'restrictedpicturesviewer'),
                       ('romeo.montague@cds.cern.ch', 'swordcurator'),
                       ('romeo.montague@cds.cern.ch', 'thesescurator'),
                       ('juliet.capulet@cds.cern.ch',
                        'restrictedpicturesviewer'),
                       ('juliet.capulet@cds.cern.ch', 'photocurator'),
                       ('romeo.montague@cds.cern.ch', 'submit_DEMOJRN_*'),
                       ('juliet.capulet@cds.cern.ch', 'submit_DEMOJRN_*'),
                       ('balthasar.montague@cds.cern.ch', 'atlantiseditor'),
                       ('romeo.montague@cds.cern.ch', 'poetrycommentreader'),
                       ('jekyll@cds.cern.ch', 'authorlistusers'),)

# Demo site authorizations
#    role          action        arguments
DEF_DEMO_AUTHS = (
    ('photocurator', 'runwebcoll', {'collection': 'Pictures'}),
    ('restrictedpicturesviewer', 'viewrestrdoc',
     {'status': 'restricted_picture'}),
    ('thesesviewer', VIEWRESTRCOLL, {'collection': 'Theses'}),
    ('thesesviewer', VIEWRESTRCOLL, {'collection': 'Drafts'}),
    ('ALEPHviewer', VIEWRESTRCOLL, {'collection': 'ALEPH Theses'}),
    ('ALEPHviewer', VIEWRESTRCOLL, {'collection': 'ALEPH Internal Notes'}),
    ('ISOLDEnotesviewer', VIEWRESTRCOLL,
     {'collection': 'ISOLDE Internal Notes'}),
    ('referee_DEMOBOO_*', 'referee', {'doctype': 'DEMOBOO', 'categ': '*'}),
    ('curator', 'cfgbibknowledge', {}),
    ('curator', 'runbibedit', {}),
    ('curator', 'runbibeditmulti', {}),
    ('curator', 'runbibmerge', {}),
    ('swordcurator', 'runbibswordclient', {}),
    ('thesescurator', 'runbibedit', {'collection': 'Theses'}),
    ('thesescurator', VIEWRESTRCOLL, {'collection': 'Theses'}),
    ('photocurator', 'runbibedit', {'collection': 'Pictures'}),
    ('referee_DEMOBOO_*', 'runbibedit', {'collection': 'Books'}),
    ('submit_DEMOJRN_*', 'submit',
     {'doctype': 'DEMOJRN', 'act': 'SBI', 'categ': '*'}),
    ('submit_DEMOJRN_*', 'submit',
     {'doctype': 'DEMOJRN', 'act': 'MBI', 'categ': '*'}),
    ('submit_DEMOJRN_*', 'cfgwebjournal',
     {'name': 'AtlantisTimes', 'with_editor_rights': 'no'}),
    ('atlantiseditor', 'cfgwebjournal', {
     'name': 'AtlantisTimes', 'with_editor_rights': 'yes'}),
    ('referee_DEMOBOO_*', 'runbatchuploader', {'collection': 'Books'}),
    ('poetrycommentreader', 'viewcomment', {'collection': 'Poetry'}),
    ('atlantiseditor', VIEWRESTRCOLL, {'collection': 'Atlantis Times Drafts'}),
    ('anyuser', 'submit', {
     'doctype': 'DEMOART', 'act': 'SBI', 'categ': 'ARTICLE'}),
)
