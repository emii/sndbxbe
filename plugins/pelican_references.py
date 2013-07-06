# -*- coding: utf-8 -*-
"""
Copyright (c) Emiliano Izquierdo <eizquierd@gmail.com>\

"""
from pelican import signals
import re

try:
    from pybtex.database.input.bibtex import Parser
    from pybtex.database.output.bibtex import Writer
    from pybtex.database import BibliographyData, PybtexError
    from pybtex.backends import html
    from pybtex.style.formatting import plain

except ImportError:
    logger.warn('`pelican_bibtex` failed to load dependency `pybtex`')

def generate_references(generator):
    pattern = re.compile('([^\s\w]|_)+')
    pattern2 = re.compile(r'[\\\"\'\`\{\}]')
    for article in generator.articles: 
        if 'references' in article.metadata:
            refs_file = article.metadata['references']
            try:
                bibdata_all = Parser().parse_file(refs_file)
            except PybtexError as e:
                logger.warn('`pelican_bibtex` failed to parse file %s: %s' % (
                    refs_file,
                    str(e)))

            references = []

            # format entries
            plain_style = plain.Style()
            formatted_entries = plain_style.format_entries(bibdata_all.entries.values())

            for formatted_entry in formatted_entries:
                key = formatted_entry.key
                entry = bibdata_all.entries[key]
                try:
                    year = entry.fields['year']
                except:
                    year = '&nbsp;'
                try:
                    author = entry.fields['author']
                    author = pattern2.sub('',author)
                    author = author.replace(',','')
                    author = author.replace(' and ',', ')

                except:
                    author = '&nbsp;'
                try:
                    title = entry.fields['title']
                except:
                    title = '&nbsp;'
                try:
                    journal = entry.fields['journal']
                except:
                    journal = '&nbsp;'
                try:
                    url = entry.fields['url']
                except:
                    url = '&nbsp;'
                try:
                    volume = entry.fields['volume']
                except:
                    volume = '&nbsp;'
                try:
                    pages = entry.fields['pages']
                except:
                    pages = '&nbsp;'

                
                references.append({'key' : key,
                                     'year' : year,
                                     'author' : author,
                                     'title' : pattern.sub('', title),
                                     'journal' : journal,
                                     'url' : url,
                                     'volume' : volume,
                                     'pages' : pages
                                     })

            article.references= references

def register():
    signals.article_generator_finalized.connect(generate_references)