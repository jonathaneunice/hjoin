#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for `hjoin` module.
"""

import pytest
from hjoin import *


def test_string_shape():
    assert string_shape('') == (0, 0)
    assert string_shape('this') == (1, 4)
    assert string_shape('this\nis') == (2, 4)
    assert string_shape('this\nis\n') == (2, 4)
    assert string_shape('this\nis\n\n') == (3, 4)


def test_hjoin_null():
    assert hjoin([]) == ''
    assert hjoin(None) == ''


def test_hjoin_1d():
    assert hjoin(['this']) == 'this'
    assert hjoin(['this', 'that']) == 'this that'
    assert hjoin(['this', 'that', 'and']) == 'this that and'


def test_hjoin_2d():
    assert hjoin(['this\nthing', 'is']) == 'this  is\nthing   '
    assert hjoin(['this\nthing', 'is\ngood']) == 'this  is  \nthing good'
    assert hjoin(['this', 'is\ngood\nenough']) == \
                  'this is    \n     good  \n     enough'
    assert hjoin(['this\nthing', 'is'], sep=' | ') == \
                  'this  | is\nthing |   '


