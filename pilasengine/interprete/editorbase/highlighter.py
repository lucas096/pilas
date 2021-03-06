#-*-coding:utf-8-*-
# pilas engine: un motor para hacer videojuegos
#
# Copyright 2010-2014 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar
from __future__ import absolute_import
# based on Python Syntax highlighting from:
# http://diotavelli.net/PyQtWiki/Python%20syntax%20highlighting

import os
try:
    import json
except ImportError:
    import simplejson as json

from PyQt4.QtGui import QColor
from PyQt4.QtGui import QTextCharFormat
from PyQt4.QtGui import QFont
from PyQt4.QtGui import QSyntaxHighlighter
from PyQt4.QtCore import QRegExp


COLOR_SCHEME = {
    "keyword": "darkMagenta",
    "operator": "darkRed",
    "brace": "#858585",
    "definition": "blue",
    "string": "green",
    "string2": "darkGreen",
    "comment": "gray",
    "properObject": "darkBlue",
    "numbers": "brown",
    "spaces": "#BFBFBF",
    "extras": "orange",
    "editor-background": "white",
    "editor-selection-color": "white",
    "editor-selection-background": "#437DCD",
    "editor-text": "black",
    "current-line": "darkCyan",
    "selected-word": "yellow",
    "brace-background": "#5BC85B",
    "brace-foreground": "red"}
SYNTAX = {}


def load_syntax():
    structure = None
    structure = {'comment': ['#'],
                 'definition': ['def', 'class'],
                 'string': ["'", '"'],
                 'extension': ['py'],
                 'properObject': ['self'],
                 'operators': ['=', '==', '!=', '<', '<=', '>', '>=', '\\+', '-', '\\*', '/', '//', '\\%', '\\*\\*', '\\+=', '-=', '\\*=', '/=', '\\%=', '\\^', '\\|',
                               '\\&', '\\~', '>>', '<<'],
                 'keywords': ['and', 'assert', 'break', 'c lass', 'continue', 'def', 'class', 'del', 'elif', 'else', 'except', 'exec', 'finally',
                              'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise',
                              'return', 'super', 'try', 'while', 'yield', 'None', 'True', 'False']
                 }

    SYNTAX['python'] = structure


def format(color, style=''):
    """Return a QTextCharFormat with the given attributes."""
    _color = QColor()
    _color.setNamedColor(color)

    _format = QTextCharFormat()
    _format.setForeground(_color)

    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)

    return _format


# Syntax styles that can be shared by all languages
STYLES = {
    'keyword': format(COLOR_SCHEME['keyword']),
    'operator': format(COLOR_SCHEME['operator']),
    'brace': format(COLOR_SCHEME['brace']),
    'definition': format(COLOR_SCHEME['definition']),
    'string': format(COLOR_SCHEME['string']),
    'string2': format(COLOR_SCHEME['string2']),
    'comment': format(COLOR_SCHEME['comment']),
    'properObject': format(COLOR_SCHEME['properObject']),
    'numbers': format(COLOR_SCHEME['numbers']),
    'spaces': format(COLOR_SCHEME['spaces']),
    'extras': format(COLOR_SCHEME['extras'])}


def restyle(scheme):
    STYLES['keyword'] = format(scheme.get('keyword', COLOR_SCHEME['keyword']))
    STYLES['operator'] = format(scheme.get('operator', COLOR_SCHEME['operator']))
    STYLES['brace'] = format(scheme.get('brace', COLOR_SCHEME['brace']))
    STYLES['definition'] = format(scheme.get('definition', COLOR_SCHEME['definition']))
    STYLES['string'] = format(scheme.get('string', COLOR_SCHEME['string']))
    STYLES['string2'] = format(scheme.get('string2', COLOR_SCHEME['string2']))
    STYLES['comment'] = format(scheme.get('comment', COLOR_SCHEME['comment']))
    STYLES['properObject'] = format(scheme.get('properObject', COLOR_SCHEME['properObject']))
    STYLES['numbers'] = format(scheme.get('numbers', COLOR_SCHEME['numbers']))
    STYLES['spaces'] = format(scheme.get('spaces', COLOR_SCHEME['spaces']))
    STYLES['extras'] = format(scheme.get('extras', COLOR_SCHEME['extras']))


class Highlighter(QSyntaxHighlighter):

    # braces
    braces = ['\\(', '\\)', '\\{', '\\}', '\\[', '\\]']

    def __init__(self, document, lang, scheme=None):
        QSyntaxHighlighter.__init__(self, document)
        self.apply_highlight(lang, scheme)

    def apply_highlight(self, lang, scheme=None):
        load_syntax()
        langSyntax = SYNTAX.get(lang, {})
        if scheme:
            restyle(scheme)

        keywords = langSyntax.get('keywords', [])
        operators = langSyntax.get('operators', [])
        extras = langSyntax.get('extras', [])

        rules = []

        # Keyword, operator, brace and extras rules
        rules += [(r'\b%s\b' % w, 0, STYLES['keyword']) for w in keywords]
        rules += [(r'%s' % o, 0, STYLES['operator']) for o in operators]
        rules += [(r'%s' % b, 0, STYLES['brace']) for b in Highlighter.braces]
        rules += [(r'\b%s\b' % e, 0, STYLES['extras']) for e in extras]

        # All other rules
        proper = langSyntax.get('properObject', None)
        if proper is not None:
            proper = '\\b' + str(proper[0]) + '\\b'
            rules += [(proper, 0, STYLES['properObject'])]

        rules.append((r'__\w+__', 0, STYLES['properObject']))

        definition = langSyntax.get('definition', [])
        for de in definition:
            expr = '\\b' + de + '\\b\\s*(\\w+)'
            rules.append((expr, 1, STYLES['definition']))

        # Numeric literals
        rules += [
            (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0,
            STYLES['numbers']),
        ]

        regex = langSyntax.get('regex', [])
        for reg in regex:
            expr = reg[0]
            color = COLOR_SCHEME['extras']
            style = ''
            if len(reg) > 1:
                color = COLOR_SCHEME[reg[1]]
            if len(reg) > 2:
                style = reg[2]
            rules.append((expr, 0, format(color, style)))

        comments = langSyntax.get('comment', [])
        for co in comments:
            expr = co + '[^\\n]*'
            rules.append((expr, 0, STYLES['comment']))

        stringChar = langSyntax.get('string', [])
        for sc in stringChar:
            expr = r'"[^"\\]*(\\.[^"\\]*)*"' if sc == '"' \
                else r"'[^'\\]*(\\.[^'\\]*)*'"
            rules.append((expr, 0, STYLES['string']))

        # Multi-line strings (expression, flag, style)
        # FIXME: The triple-quotes in these two lines will mess up the
        # syntax highlighting from this point onward
        self.tri_single = (QRegExp("'''"), 1, STYLES['string2'])    # '''
        self.tri_double = (QRegExp('"""'), 2, STYLES['string2'])    # """

        multi = langSyntax.get('multiline_comment', [])
        if multi:
            self.multi_start = (QRegExp(multi['open']), STYLES['comment'])
            self.multi_end = (QRegExp(multi['close']), STYLES['comment'])
        else:
            self.multi_start = None

        # Build a QRegExp for each pattern
        self.rules = [(QRegExp(pat), index, fmt)
            for (pat, index, fmt) in rules]
        #Apply Highlight to the document... (when colors change)
        self.rehighlight()

    def highlightBlock(self, text):
        """Apply syntax highlighting to the given block of text."""
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)

            while index >= 0:
                # We actually want the index of the nth match
                index = expression.pos(nth)
                length = expression.cap(nth).length()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)
        if not self.multi_start:
            # Do multi-line strings
            in_multiline = self.match_multiline(text, *self.tri_single)
            if not in_multiline:
                in_multiline = self.match_multiline(text, *self.tri_double)
        else:
            # Do multi-line comment
            self.comment_multiline(text, self.multi_end[0], *self.multi_start)

        #Spaces
        expression = QRegExp('\s+')
        index = expression.indexIn(text, 0)
        while index >= 0:
            index = expression.pos(0)
            length = expression.cap(0).length()
            self.setFormat(index, length, STYLES['spaces'])
            index = expression.indexIn(text, index + length)

    def match_multiline(self, text, delimiter, in_state, style):
        """Do highlighting of multi-line strings. ``delimiter`` should be a
        ``QRegExp`` for triple-single-quotes or triple-double-quotes, and
        ``in_state`` should be a unique integer to represent the corresponding
        state changes when inside those strings. Returns True if we're still
        inside a multi-line string when this function is finished.
        """
        # If inside triple-single quotes, start at 0
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        # Otherwise, look for the delimiter on this line
        else:
            start = delimiter.indexIn(text)
            # Move past this match
            add = delimiter.matchedLength()

        # As long as there's a delimiter match on this line...
        while start >= 0:
            # Look for the ending delimiter
            end = delimiter.indexIn(text, start + add)
            # Ending delimiter on this line?
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            # No; multi-line string
            else:
                self.setCurrentBlockState(in_state)
                length = text.length() - start + add
            # Apply formatting
            self.setFormat(start, length, style)
            # Look for the next match
            start = delimiter.indexIn(text, start + length)

        # Return True if still inside a multi-line string, False otherwise
        if self.currentBlockState() == in_state:
            return True
        else:
            return False

    def comment_multiline(self, text, delimiter_end, delimiter_start, style):
        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = delimiter_start.indexIn(text)
        while startIndex >= 0:
            endIndex = delimiter_end.indexIn(text, startIndex)
            commentLength = 0
            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = text.length() - startIndex
            else:
                commentLength = endIndex - startIndex + delimiter_end.matchedLength()

            self.setFormat(startIndex, commentLength, style)
            startIndex = delimiter_start.indexIn(text, startIndex + commentLength)


class EmptyHighlighter(QSyntaxHighlighter):

    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)

    def highlightBlock(self, text):
        pass
