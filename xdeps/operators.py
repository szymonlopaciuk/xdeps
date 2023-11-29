# copyright ############################### #
# This file is part of the Xdeps Package.   #
# Copyright (c) CERN, 2023.                 #
# ######################################### #

from xdeps import refs


def eq(lhs, rhs) -> refs.EqExpr:
    """Return an xdeps expression equating the two inputs."""
    return refs.EqExpr(lhs, rhs)


def neq(lhs, rhs):
    """Return an xdeps expression of inequality between the two inputs."""
    return refs.NeExpr(lhs, rhs)


def land(lhs, rhs):
    """Return an xdeps expression of logical conjunction between the inputs."""
    return refs.LogicalAndExpr(lhs, rhs)


def lor(lhs, rhs):
    """Return an xdeps expression of logical disjunction between the inputs."""
    return refs.LogicalOrExpr(lhs, rhs)


def lnot(arg):
    """Return an xdeps expression of logical negation of the input."""
    return refs.NotExpr(arg)


def if_then(cond, if_true):
    """Return an xdeps expression evaluating to `if_true` if `cond` evaluates to
    true, and False otherwise."""
    return land(cond, if_true)


def if_then_else(cond, if_true, if_false):
    """Return an xdeps expression that returns `if_true` if `cond` evaluates to
    true, and optionally `if_false` otherwise.
    """
    if if_false is False:
        return land(cond, if_true)
    return lor(land(cond, if_true), if_false)
