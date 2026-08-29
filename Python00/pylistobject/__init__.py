# -*- coding: utf-8 -*-
"""
pylistobject -- A modular OOP tutorial package demonstrating Python's
memory model, object identity, reference counting, and list behavior.

This package contains 7 demo classes, each in its own module:

  1. ObjectIdentityDemo       -- id(), immutable rebinding, string identity
  2. ReferenceCountingDemo    -- sys.getrefcount(), nested list refcounts
  3. ListReferenceDemo        -- slicing, shallow copy via [:]
  4. StringImmutabilityDemo   -- string immutability vs list mutability
  5. ListAliasingDemo         -- alias vs copy, concat vs append, list()
  6. ShallowVsDeepCopyDemo    -- list*N, explicit shared refs, literals
  7. NestedListMutationDemo   -- 2D slice mutation, mixed-type iteration

Usage:
    from pylistobject import ObjectIdentityDemo
    demo = ObjectIdentityDemo()
    demo.run_all()

NO DECORATORS are used anywhere in this package.
"""

from pylistobject.object_identity import ObjectIdentityDemo
from pylistobject.reference_counting import ReferenceCountingDemo
from pylistobject.list_references import ListReferenceDemo
from pylistobject.string_immutability import StringImmutabilityDemo
from pylistobject.list_aliasing import ListAliasingDemo
from pylistobject.shallow_vs_deep_copy import ShallowVsDeepCopyDemo
from pylistobject.nested_list_mutation import NestedListMutationDemo

# Explicit public API -- importable via "from pylistobject import *"
__all__ = [
    "ObjectIdentityDemo",
    "ReferenceCountingDemo",
    "ListReferenceDemo",
    "StringImmutabilityDemo",
    "ListAliasingDemo",
    "ShallowVsDeepCopyDemo",
    "NestedListMutationDemo",
]
