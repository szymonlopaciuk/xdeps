# copyright ############################### #
# This file is part of the Xdeps Package.   #
# Copyright (c) CERN, 2023.                 #
# ######################################### #
"""Convenience functions for use in expressions.

This file defines convenience functions that can be used in expressions
(instances of refs.BaseRef). Including such a function in this file ensures
that it will be properly handled when serializing/deserializing expressions
that use it.
"""

from typing import Union
from xdeps import refs


def _any_is_ref(*args):
    return any(refs.is_ref(arg) for arg in args)


def value_if_ref(ref_or_scalar):
    if refs.is_ref(ref_or_scalar):
        return ref_or_scalar._get_value()
    return ref_or_scalar


def eq(lhs, rhs) -> Union[refs.EqExpr, bool]:
    """Return an xdeps expression equating the two inputs."""
    if _any_is_ref(lhs, rhs):
        return refs.EqExpr(lhs, rhs)
    return lhs == rhs


def neq(lhs, rhs) -> Union[refs.NeExpr, bool]:
    """Return an xdeps expression of inequality between the two inputs."""
    if _any_is_ref(lhs, rhs):
        return refs.NeExpr(lhs, rhs)
    return lhs != rhs


def land(lhs, rhs):
    """Return an xdeps expression of logical conjunction between the inputs."""
    if _any_is_ref(lhs, rhs):
        return refs.BuiltinRef(land, lhs, rhs)
    return lhs and rhs


def lor(lhs, rhs):
    """Return an xdeps expression of logical disjunction between the inputs."""
    if _any_is_ref(lhs, rhs):
        return refs.BuiltinRef(lor, lhs, rhs)
    return lhs or rhs


def lnot(arg):
    """Return an xdeps expression of logical negation of the input."""
    if refs.is_ref(arg):
        return refs.BuiltinRef(lnot, arg)
    return not arg


def if_then(cond, if_true):
    """Return an xdeps expression evaluating to `if_true` if `cond` evaluates to
    true, and False otherwise."""
    if refs.is_ref(cond):
        return land(cond, if_true)

    if cond:
        return if_true

    return False


def if_then_else(cond, if_true, if_false):
    """Return an xdeps expression that returns `if_true` if `cond` evaluates to
    true, and optionally `if_false` otherwise.
    """
    if refs.is_ref(cond):
        return lor(land(cond, if_true), if_false)

    if cond:
        return if_true

    return if_false
