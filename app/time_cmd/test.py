import pytest
from scheme import scheme

s = scheme("test", 7, 0, 16, 0)
pytest.Class.warn
assert(s.check() == False)
