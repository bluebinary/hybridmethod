import sys, os
import pytest

path = os.path.join(os.path.dirname(__file__), "..", "source")

sys.path.insert(0, path)  # add 'classicist' library path for importing into the tests

import classicist
