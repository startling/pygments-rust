#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygments.lexer import RegexLexer
from pygments.token import *


class RustLexer(RegexLexer):
    name = 'Rust'
    aliases = ['rust']
    filenames = ['*.rs']

    tokens = {
        'root': []        
    }
