# Stubs for collections_extended.bags (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ._compat import handle_rich_comp_not_implemented
from ._util import deprecated
from collections import Hashable, MutableSet, Set
from typing import Any, Optional

class UniqueElementsView:
    bag: Any = ...
    def __init__(self, bag: Any) -> None: ...
    def __len__(self): ...
    def __iter__(self) -> None: ...
    def __contains__(self, elem: Any): ...

class CountsView:
    bag: Any = ...
    def __init__(self, bag: Any) -> None: ...
    def __len__(self): ...
    def __iter__(self) -> None: ...
    def __contains__(self, item: Any): ...

class _basebag(Set):
    def __init__(self, iterable: Optional[Any] = ...) -> None: ...
    def copy(self): ...
    def num_unique_elements(self): ...
    def unique_elements(self): ...
    def count(self, value: Any): ...
    def nlargest(self, n: Optional[Any] = ...): ...
    def counts(self): ...
    @classmethod
    def from_mapping(cls, mapping: Any): ...
    def __len__(self): ...
    def __contains__(self, value: Any): ...
    def __iter__(self) -> None: ...
    def is_subset(self, other: Any): ...
    def is_superset(self, other: Any): ...
    def __le__(self, other: Any): ...
    def __lt__(self, other: Any): ...
    def __gt__(self, other: Any): ...
    def __ge__(self, other: Any): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __and__(self, other: Any): ...
    def isdisjoint(self, other: Any): ...
    def __or__(self, other: Any): ...
    def __add__(self, other: Any): ...
    def __sub__(self, other: Any): ...
    def __mul__(self, other: Any): ...
    def __xor__(self, other: Any): ...

class bag(_basebag, MutableSet):
    def pop(self): ...
    def add(self, elem: Any) -> None: ...
    def discard(self, elem: Any) -> None: ...
    def remove(self, elem: Any) -> None: ...
    def discard_all(self, other: Any) -> None: ...
    def remove_all(self, other: Any) -> None: ...
    def clear(self) -> None: ...
    __ior__: Any = ...
    __iand__: Any = ...
    __ixor__: Any = ...
    __isub__: Any = ...
    __iadd__: Any = ...

class frozenbag(_basebag, Hashable):
    def __hash__(self): ...