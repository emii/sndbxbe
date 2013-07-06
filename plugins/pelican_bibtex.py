"""
Pelican BibTeX
==============

A Pelican plugin that populates the context with a list of formatted
citations, loaded from a BibTeX file at a configurable path.

The use case for now is to generate a ``Publications'' page for academic
websites.
"""
# Author: Vlad Niculae <vlad@vene.ro>
# Unlicense (see UNLICENSE for details)

import logging
logger = logging.getLogger(__name__)

from pelican import signals

import re

__version__ = '0.2'


def add_publications(generator):
    """
    Populates context with a list of BibTeX publications.

    Configuration
    -------------
    generator.settings['PUBLICATIONS_SRC']:
        local path to the BibTeX file to read.

    Output
    ------
    generator.context['publications']:
        List of tuples (key, year, text, bibtex, pdf, slides, poster).
        See Readme.md for more details.
    """
    if 'PUBLICATIONS_SRC' not in generator.settings:
        return
    from StringIO import StringIO
    try:
        from pybtex.database.input.bibtex import Parser
        from pybtex.database.output.bibtex import Writer
        from pybtex.database import BibliographyData, PybtexError
        from pybtex.backends import html
        from pybtex.style.formatting import plain
    except ImportError:
        logger.warn('`pelican_bibtex` failed to load dependency `pybtex`')
        return

    refs_file = generator.settings['PUBLICATIONS_SRC']
    try:
        bibdata_all = Parser().parse_file(refs_file)
    except PybtexError as e:
        logger.warn('`pelican_bibtex` failed to parse file %s: %s' % (
            refs_file,
            str(e)))
        return

    publications = []

    # format entries
    plain_style = plain.Style()
    formatted_entries = plain_style.format_entries(bibdata_all.entries.values())

    for formatted_entry in formatted_entries:
        key = formatted_entry.key
        entry = bibdata_all.entries[key]

        pattern = re.compile('([^\s\w]|_)+')
        publications.append({'key' : key,
                             'year' : entry.fields['year'],
                             'author' : entry.fields['author'],
                             'title' : pattern.sub('', entry.fields['title']),
                             'journal' : entry.fields['journal'],
                             'url' : entry.fields['url'],
                             'volume' : entry.fields['volume'],
                             'pages' : entry.fields['pages']})

    generator.context['publications'] = publications


def register():
    signals.generator_init.connect(add_publications)
