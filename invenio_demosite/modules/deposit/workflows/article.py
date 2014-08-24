# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2012, 2013, 2014 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

from __future__ import absolute_import, print_function

from wtforms import validators
from werkzeug.local import LocalProxy
from invenio.base.i18n import _, language_list_long
from datetime import date
from invenio.modules.deposit.types import SimpleRecordDeposition
from invenio.modules.deposit.form import WebDepositForm
from invenio.modules.deposit import fields
from invenio.modules.deposit.filter_utils import strip_string, sanitize_html, \
    strip_prefixes
from invenio.modules.deposit.field_widgets import date_widget, \
    plupload_widget, ExtendedListWidget, CKEditorWidget, \
    ColumnInput, ItemWidget
from invenio.modules.deposit.validation_utils import required_if, \
    list_length, doi_syntax_validator


def keywords_autocomplete(form, field, term, limit=50):
    return [{'value': "Keyword 1"}, {'value': "Keyword 2"}]


def missing_doi_warning(dummy_form, field, submit=False, fields=None):
    """
    Field processor, checking for existence of a DOI, and otherwise
    asking people to provide it.
    """
    if not field.errors and not field.data:
        field.add_message("Please provide a DOI if possible.", state="warning")
        raise StopIteration()


#
# Helpers
#
def filter_empty_helper(keys=None):
    """ Remove empty elements from a list"""
    def _inner(elem):
        if isinstance(elem, dict):
            for k, v in elem.items():
                if (keys is None or k in keys) and v:
                    return True
            return False
        else:
            return bool(elem)
    return _inner


#
# Forms
#
class AuthorInlineForm(WebDepositForm):
    """
    Author inline form
    """
    name = fields.TextField(
        placeholder=_("Family name, First name"),
        widget_classes='form-control',
        #autocomplete=map_result(
        #    dummy_autocomplete,
        #    authorform_mapper
        #),
        widget=ColumnInput(class_="col-xs-6"),
        validators=[
            required_if(
                'affiliation',
                [lambda x: bool(x.strip()), ],  # non-empty
                message=_("Creator name is required if you specify affiliation.")
            ),
        ],
    )
    affiliation = fields.TextField(
        placeholder=_("Affiliation"),
        widget_classes='form-control',
        widget=ColumnInput(class_="col-xs-4 col-pad-0"),
    )


class ArticleForm(WebDepositForm):
    #
    # Fields
    #
    doi = fields.TextField(
        label=_("Digital Object Identifier"),
        placeholder=_("e.g. 10.1234/foo.bar..."),
        widget_classes="form-control",
        icon='fa fa-barcode fa-fw',
        validators=[
            doi_syntax_validator,
        ],
        filters=[
            strip_string,
            strip_prefixes("doi:", "http://dx.doi.org/"),
        ],
        processors=[
            missing_doi_warning,
        ],
    )

    publication_date = fields.Date(
        label=_('Publication date'),
        icon='fa fa-calendar fa-fw',
        description=_('Required. Format: YYYY-MM-DD.'),
        default=date.today(),
        validators=[validators.required()],
        widget=date_widget,
        widget_classes='input-sm',
        export_key='imprint.date',
    )

    title = fields.TextField(
        label=_('Title'),
        export_key='title.title',
        icon='fa fa-book fa-fw',
        widget_classes="form-control",
        validators=[validators.Required()],
    )

    authors = fields.DynamicFieldList(
        fields.FormField(
            AuthorInlineForm,
            widget=ExtendedListWidget(
                item_widget=ItemWidget(),
                html_tag='div',
            ),
        ),
        label=_('Authors'),
        add_label=_('Add another author'),
        icon='fa fa-user fa-fw',
        min_entries=1,
        widget_classes='',
        export_key='authors',
        validators=[validators.Required(), list_length(
            min_num=1, element_filter=filter_empty_helper(),
        )],
    )

    abstract = fields.TextAreaField(
        label=_("Description"),
        description=_('Required.'),
        default='',
        icon='fa fa-pencil fa-fw',
        validators=[validators.required(), ],
        widget=CKEditorWidget(
            toolbar=[
                ['PasteText', 'PasteFromWord'],
                ['Bold', 'Italic', 'Strike', '-',
                    'Subscript', 'Superscript', ],
                ['NumberedList', 'BulletedList'],
                ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'RemoveFormat'],
                ['SpecialChar', 'ScientificChar'], ['Source'], ['Maximize'],
            ],
            disableNativeSpellChecker=False,
            extraPlugins='scientificchar',
            removePlugins='elementspath',
        ),
        filters=[
            sanitize_html(),
            strip_string,
        ],
        export_key='abstract.summary',
    )

    journal_title = fields.TextField(
        label=_("Journal title"),
        description=_("Optional."),
        validators=[
            required_if(
                'journal_volume', [lambda x: bool(x.strip()), ],  # non-empty
                message=_("Journal title is required if you specify either "
                          "volume, issue or pages.")
            ),
            required_if(
                'journal_issue', [lambda x: bool(x.strip()), ],  # non-empty
                message=_("Journal title is required if you specify either "
                          "volume, issue or pages.")
            ),
            required_if(
                'journal_pages', [lambda x: bool(x.strip()), ],  # non-empty
                message=_("Journal title is required if you specify either "
                          "volume, issue or pages.")
            ),
        ],
        export_key='journal_info.title',
        widget_classes='form-control',
    )

    journal_volume = fields.TextField(
        label=_("Volume"),
        description=_("Optional."),
        export_key='journal_info.volume',
        widget_classes='form-control',
    )

    journal_issue = fields.TextField(
        label=_("Issue"),
        description=_("Optional."),
        export_key='journal_info.issue',
        widget_classes='form-control',
    )

    journal_pages = fields.TextField(
        label=_("Pages"),
        description=_("Optional."),
        export_key='journal_info.pagination',
        widget_classes='form-control',
    )

    language = fields.SelectField(
        choices=LocalProxy(lambda: language_list_long(
            enabled_langs_only=False)),
        default='english',
        icon='fa fa-globe fa-fw',
        widget_classes='form-control',
    )

    keywords = fields.DynamicFieldList(
        fields.TextField(
            widget_classes='form-control',
            autocomplete=keywords_autocomplete,
            widget=ColumnInput(class_="col-xs-10"),
        ),
        label=_('Keywords'),
        add_label=_('Add another keyword'),
        icon='fa fa-tags fa-fw',
        widget_classes='',
        min_entries=1,
    )

    notes = fields.TextAreaField(
        label=_("Notes"),
        description=_('Optional.'),
        default='',
        validators=[validators.optional()],
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
        icon='fa fa-pencil fa-fw',
        export_key='comment',
    )

    plupload_file = fields.FileUploadField(
        label="",
        widget=plupload_widget,
        export_key=False
    )

    #
    # Form configuration
    #
    _title = _('New article')
    _subtitle = _('Instructions: (i) Press "Save" to save your upload for '
                  'editing later, as many times you like. (ii) Upload or '
                  'remove  extra files in the bottom of the form. (iii) When '
                  'ready, press "Submit" to finalize your upload.')

    groups = [
        ('Basic Information',
            ['doi', 'publication_date', 'title', 'authors', 'abstract', ],
            {
                'indication': 'required',
            }),
        ('Journal',
            ['journal_title', 'journal_volume', 'journal_issue',
             'journal_pages'],
            {
                'indication': 'required'
            }),
        ('Additional information',
            ['language', 'keywords', 'notes'],
            {
                'indication': 'optional',
            })
    ]

    field_sizes = {
        'plupload_file': 'col-md-12',
    }


#
# Workflow
#
class article(SimpleRecordDeposition):
    name = _("Article")
    name_plural = _("Articles")
    group = _("Articles & Preprints")
    draft_definitions = {
        'default': ArticleForm,
    }

    @classmethod
    def process_sip_metadata(cls, deposition, metadata):
        # Map keywords to match jsonalchemy configuration
        metadata['keywords'] = map(
            lambda x: {'term': x},
            metadata['keywords']
        )
