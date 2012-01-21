#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from pygments.lexer import RegexLexer, include, combined, bygroups
from pygments.token import *


class RustLexer(RegexLexer):
    name = 'Rust'
    aliases = ['rust']
    filenames = ['*.rs']

    tokens = {
        'root': [
            # use statements, e.g. `use std;`
            (r'(use)(\s(\w+)\;)', bygroups(Keyword.Namespace, Text)),
            # comments
            include('comments'),
            # operators
            include('operators'),
            # keywords
            include('keywords'),
            # types
            include('types'),
            # symbols -- braces, parentheses, semicolons, etc.
            # http://doc.rust-lang.org/doc/rust.html#symbols
            (r'(\[|\]|\{|\}|\(|\)|\;|\#|::|-\>|\,)', Punctuation),
            # whitespace is insignificant.
            (r'\s+', Whitespace),
        ],
        'operators':[
            # unary operators
            # http://doc.rust-lang.org/doc/rust.html#unary-operator-expressions
            (r'(-|\*|\!|@|~)', Operator),
            # binary operators
            # http://doc.rust-lang.org/doc/rust.html#binary-operator-expressions
            (r'(\+|\-|\*|/|\%)', Operator)
        ],
        'comments': [
            # single-line comments; e.g. //this is a comment
            (r'//.*', Comment),
            # multi-line comments; e.g., /* this is a \n comment */
            (r'/\*(.|\n)*?\*/', Comment)
        ],
        'keywords': [
            # general keywords
            (r'(alt|as|assert|auth|be|bind|block|break|chan|'
            r'check|claim|cont|const|copy|do|else|enum|export|fail|'
            r'fn|for|if|ifrace|impl|import|in|inline|lambda|let|log|'
            r'log_err|mod|mutable|native|note|of|prove|pure|'
            r'resource|ret|self|tag|type|unsafe|use|while|with)\b', Keyword),
            # booleans
            (r'(true|false)', Keyword),
        ],
        'types': [
            # types
            (r'(any|int|uint|float|char|bool|u8|u16|u32|u64|f32|'
             r'f64|i8|i16|i32|i64|str|task)', Name.Builtin),
        ]
    }
