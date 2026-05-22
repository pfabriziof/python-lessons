from . import t
import pytest
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(name=__name__)
logger.setLevel(logging.INFO)

@pytest.mark.parametrize(
        ('input_n', 'expected'),
        (
            (5,25),
            (3.,9.),
            )
        )
def test_square(input_n, expected):
    logger.info(f'{input_n=}') # you can show this log by using the --log-cli-level=INFO flag
    print(f'{input_n=}') # you can show this log by using the -s flag
    assert t.square(input_n) == expected

def test_square_float(): # you can show the name of the functions tests by using the -v flag
    assert t.square(3.) == pytest.approx(9.)

class TestSquare:
    def test_square(self):
        assert t.square(3) == 9

# pytest is compatible with legacy unittest tests.
# class TestLegacy(unittest.TestCase):
#     def test(self):
#         self.assertEqual(t.square(3), 9)
