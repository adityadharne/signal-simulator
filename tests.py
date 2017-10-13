import unittest
from models import Signal


class SignalTestCase(unittest.TestCase):
    def test_if_green(self):
        signal = Signal()
        self.assertIsNotNone(signal.ascii_signals['green'])

    def test_if_red_transitions_green(self):
        signal = Signal()
        signal.signal_transition()
        self.assertEqual(signal.signal_now, 'green')


if __name__ == '__main__':
    unittest.main()