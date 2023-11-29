# copyright ############################### #
# This file is part of the Xdeps Package.   #
# Copyright (c) CERN, 2023.                 #
# ######################################### #

from types import SimpleNamespace

import xdeps as xd
from xdeps.operators import *
import itertools


def test_eq_neq():
    manager = xd.Manager()
    container = SimpleNamespace(a=1, b=2, c=3)
    ref = manager.ref(container, 'ref')

    assert eq(ref.a + ref.b, ref.c)._value
    assert not neq(ref.a + ref.b, ref.c)._value
    assert not eq(ref.a, ref.b)._value
    assert neq(ref.a, ref.b)._value


def test_logical_ops():
    manager = xd.Manager()
    container = SimpleNamespace(t=True, f=False)
    ref = manager.ref(container, 'ref')

    for lhs, rhs in itertools.combinations(['t', 'f'], 2):
        ref_lhs, ref_rhs = getattr(ref, lhs), getattr(ref, rhs)
        val_lhs, val_rhs = getattr(container, lhs), getattr(container, rhs)
        assert land(ref_lhs, ref_rhs)._value == (val_rhs and val_lhs)
        assert lor(ref_lhs, ref_rhs)._value == (val_rhs or val_lhs)


def test_conditionals():
    manager = xd.Manager()
    container = SimpleNamespace(one=1, two=2, three=3, string='hello')
    ref = manager.ref(container, 'ref')

    assert if_then_else(ref.one < ref.two, ref.three, ref.string)._value == 3
    assert if_then_else(ref.one > ref.two, ref.three, ref.string)._value == 'hello'
    assert if_then(ref.one < ref.two, ref.three)._value == 3
    assert if_then(ref.one > ref.two, ref.three)._value is False
