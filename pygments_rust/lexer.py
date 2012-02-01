#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygments.lexer import RegexLexer, include
from pygments.token import *
from pygments.unistring import xid_start, xid_continue


class RustLexer(RegexLexer):
    "A Pygments lexer for rust."
    name = 'Rust'
    aliases = ['rust']
    filenames = ['*.rc', '*.rs']

    tokens = {
        'root': [
            # Literals
            include('literals'),
            # Comments
            include('comments'),
            # Operators
            include('operators'),
            # Keywords
            include('keywords'),
            # Types
            include('types'),
            # Symbols -- braces, parentheses, semicolons, etc.
            # http://doc.rust-lang.org/doc/rust.html#symbols
            (r'([](){};#,:.[]|::|-\>)', Punctuation),
            # Identifiers
            # http://doc.rust-lang.org/doc/rust.html#identifiers
            (r'[%s][%s]*' % (xid_start, xid_continue), Name),
            # Whitespace is insignificant.
            (r'[ \t\n\r]+', Whitespace),
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
            (r'\d(\d|_)*(\.(\d|_)+)((e|E)[+-]?(\d|_)+)?(f|f32|f64)?', Number.Float),
            (r'\d(\d|_)*(\.(\d|_)+)?((e|E)[+-]?(\d|_)+)(f|f32|f64)?', Number.Float),
            (r'\d(\d|_)*(\.(\d|_)+)?((e|E)[+-]?(\d|_)+)?(f|f32|f64)', Number.Float),
            # Decimal integer literals
            (r'\d(\d|_)*(i8|i16|i32|i64|u|u8|u16|u32|u64)?', Number.Integer),
        ],
        'string': [
            (r'\\(\n|[nrt"\\]|x[0-9a-fA-F_]{2}|u[0-9a-fA-F_]{4}|U[0-9a-fA-F_]{8})', String.Escape),
            (r'[^\\"\n]+', String),
            (r'"', String.Char, '#pop')
        ],
        'character': [
            (r"\\([nrt'\\]|x[0-9a-fA-F_]{2}|u[0-9a-fA-F_]{4}|U[0-9a-fA-F_]{8})'", String.Escape, '#pop'),
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
            (r'//.*', Comment),
            # Multi-line comments; e.g., /* this is a \n comment */
            (r'/\*(.|\n)*?\*/', Comment)
        ],
        'keywords': [
            # General keywords
            (r'(alt|as|assert|be|bind|break|chan|check|claim|cont|const|'
             r'copy|do|else|enum|export|fail|fn|for|if|iface|impl|import|in|'
             r'inline|let|log|mod|move|mutable|native|of|pure|resource|ret|'
             r'self|send|type|unchecked|unsafe|use|while|with)\b', Keyword),
            # Unimplemented keywords
            (r'(note|prove)\b', Keyword),
            # Reserved keywords
            (r'(class|trait)\b', Keyword),
            # Booleans
            (r'(true|false)\b', Keyword.Constant),
            # Nil
            # (r'\(\)', Keyword.Constant),
        ],
        'types': [
            # Types
            (r'(int|uint|float|char|bool|u8|u16|u32|u64|f32|f64|i8|i16|i32|'
             r'i64|str|task|vec)\b', Name.Builtin),
            # Unimplemented types
            (r'any\b', Name.Builtin),
            # Reserved types
            (r'(m32|m64|m128|f80|f16|f128)\b', Name.Builtin),
        ]
    }
