#!/usr/bin/python3
"""a script markdown2html.py"""

import sys
import os
import markdown

def heading_parse(index, lines_read_list):
    """heading tags"""
    count_heading = 0
    list_heading = []
    min_level = 1
    max_level = 6