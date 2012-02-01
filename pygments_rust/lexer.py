#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygments.lexer import RegexLexer, bygroups, combined, include
from pygments.token import Comment, Operator, Keyword, Name, String, Number, \
    Punctuation, Whitespace
from pygments.unistring import xid_start, xid_continue


class RustLexer(RegexLexer):
    "A Pygments lexer for rust."
    name = 'Rust'
    aliases = ['rust']
    filenames = ['*.rc', '*.rs']

    _identifier = r'[%s][%s]*' % (xid_start, xid_continue)
    _path = '(?:' + _identifier + r'::)*' + _identifier + '(?:::)?'

    tokens = {
        'root': [
            # Literals
            include('literals'),
            # Comments
            include('comments'),
            # Types
            include('types'),
            # Whitespace is insignificant.
            (r'[ \t\n\r]+', Whitespace),
            (r'(fn)([ \t\n\r]+)', bygroups(Keyword, Whitespace), 'funcname'),
            (r'(const)([ \t\n\r]+)', bygroups(Keyword, Whitespace),
                'constname'),
            (r'(enum|iface|type)([ \t\n\r]+)', bygroups(Keyword, Whitespace),
                'typename'),
            (r'(impl)([ \t\n\r]+)', bygroups(Keyword, Whitespace), 'impl'),
            (r'(import|use)([ \t\n\r]+)', bygroups(Keyword, Whitespace),
                'import'),
            # Keywords
            include('keywords'),
            # Identifiers
            # http://doc.rust-lang.org/doc/rust.html#identifiers
            (r'#' + _identifier, Comment.Preproc),
            (r'([](){};,:.[]|::|-\>)', Punctuation),
            # Operators
            include('operators'),
            (r'#\[', Name.Attribute, combined('attributes', 'root')),
            #(r'#\[(.|\n)*?\]', Name.Attribute),
            # Symbols -- braces, parentheses, semicolons, etc.
            # http://doc.rust-lang.org/doc/rust.html#symbols
            (r'#', Punctuation),
            (_identifier, Name),
        ],
        'attributes': [
            (r'\[', Name.Attribute, '#push'),
            (r'\];?', Name.Attribute, '#pop'),
            (r'[(=,)]', Name.Attribute),
            (_identifier, Name.Attribute),
        ],
        'literals': [
            # http://doc.rust-lang.org/doc/rust.html#literals
            # Character literals
            (r"'", String.Char, 'character'),
            # String literals
            (r'"', String, 'string'),
            # Hexadecimal integer literals
            (r'0x[0-9a-fA-F_]+(i8|i16|i32|i64|u|u8|u16|u32|u64)?', Number.Hex),
            # Binary integer literals
            (r'0b[01_]+(i8|i16|i32|i64|u|u8|u16|u32|u64)?', Number.Binary),
            # Float literals
            # TODO: there must be a better way to express this.
            (r'\d(\d|_)*(\.(\d|_)+)((e|E)[+-]?(\d|_)+)?(f|f32|f64)?',
                Number.Float),
            (r'\d(\d|_)*(\.(\d|_)+)?((e|E)[+-]?(\d|_)+)(f|f32|f64)?',
                Number.Float),
            (r'\d(\d|_)*(\.(\d|_)+)?((e|E)[+-]?(\d|_)+)?(f|f32|f64)',
                Number.Float),
            # Decimal integer literals
            (r'\d(\d|_)*(i8|i16|i32|i64|u|u8|u16|u32|u64)?', Number.Integer),
        ],
        'funcname': [
            (_identifier, Name.Function, '#pop')
        ],
        'constname': [
            (_identifier, Name.Constant, '#pop')
        ],
        'typename': [
            (_identifier, Name.Class, '#pop')
        ],
        'impl': [
            (_identifier, Name.Class, '#pop'),
            ('<', Operator, '#pop')
        ],
        'import': [
            (r'(' + _identifier + r')([ \t\n\r]*)(=)([ \t\n\r]*)(' + _path + r')',
             bygroups(Name, Whitespace, Punctuation, Whitespace, Name.Namespace), '#pop'),
            (_path, Name.Namespace, '#pop')
        ],
        'string': [
            (r'\\(\n|[nrt"\\]|x[0-9a-fA-F_]{2}|u[0-9a-fA-F_]{4}|U[0-9a-fA-F_]{8})',
                String.Escape),
            (r'[^\\"\n]+', String),
            (r'"', String.Char, '#pop')
        ],
        'character': [
            (r"\\([nrt'\\]|x[0-9a-fA-F_]{2}|u[0-9a-fA-F_]{4}|U[0-9a-fA-F_]{8})'",
                String.Escape, '#pop'),
            (r"[^'\\]'", String.Char, '#pop')
        ],
        'operators': [
            # Unary operators
            # http://doc.rust-lang.org/doc/rust.html#unary-operator-expressions
            (r'([-*!@~])', Operator),
            # Binary operators
            # http://doc.rust-lang.org/doc/rust.html#binary-operator-expressions
            (r'([+*/%-])', Operator),
            # Bitwise operators
            # http://doc.rust-lang.org/doc/rust.html#bitwise-operators
            (r'([&|^]|<<|>>|>>>)', Operator),
            # Lazy boolean operators
            # http://doc.rust-lang.org/doc/rust.html#lazy-boolean-operators
            (r'(\|\||&&)', Operator),
            # Comparison operators
            # http://doc.rust-lang.org/doc/rust.html#comparison-operators
            (r'(==|!=|>=|<=|<|>)', Operator),
            # Binary move operator
            (r'<-', Operator),
            # Swap operator
            (r'<->', Operator),
            # Assignment
            (r'([+*/%&-|^]|<<|>>|>>)?=', Operator),
        ],
        'comments': [
            # Single-line comments; e.g. //this is a comment
            (r'//.*', Comment.Single),
            # Multi-line comments; e.g., /* this is a \n comment */
            (r'/\*(.|\n)*?\*/', Comment.Multiline)
        ],
        'keywords': [
            # General keywords
            (r'(alt|as|assert|be|bind|break|chan|check|claim|cont|'
             r'copy|do|else|export|fail|fn|for|if|in|'
             r'inline|let|log|mod|move|mutable|native|of|pure|resource|ret|'
             r'self|send|to|unchecked|unsafe|while|with)\b', Keyword),
            (r'(class|trait)\b', Keyword.Reserved),
            # Unimplemented keywords
            (r'(note|prove)\b', Keyword.Reserved),
            # Booleans
            (r'(true|false)\b', Keyword.Constant),
            # Nil
            # (r'\(\)', Keyword.Constant),
        ],
        'types': [
            # Types
            (r'(int|uint|float|char|bool|u8|u16|u32|u64|f32|f64|i8|i16|i32|'
             r'i64|str|task|vec)\b', Keyword.Type),
            # Unimplemented types
            (r'any\b', Keyword.Reserved),
            # Reserved types
            (r'(m32|m64|m128|f80|f16|f128)\b', Keyword.Reserved),
        ]
    }
