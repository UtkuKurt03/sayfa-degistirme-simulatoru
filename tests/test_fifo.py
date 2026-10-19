import unittest
from algorithms.fifo import simulate
from inputs import parse_pages, validate_capacity

class FifoTests(unittest.TestCase):
    def test_reference_trace(self):
        r = simulate([7,0,1,2,0,3,0,4,2,3,0,3,2],3)
        self.assertEqual(r.faults,10)
        self.assertEqual([s.frames for s in r.steps],[(7,),(7,0),(7,0,1),(2,0,1),(2,0,1),(2,3,1),(2,3,0),(4,3,0),(4,2,0),(4,2,3),(0,2,3),(0,2,3),(0,2,3)])
    def test_hit_does_not_change_fifo_order(self):
        r=simulate([1,2,1,3],2)
        self.assertEqual(r.steps[-1].frames,(3,2))
        self.assertEqual(r.faults,3)
    def test_one_frame(self):
        self.assertEqual(simulate([1,1,2,2,1],1).faults,3)
    def test_enough_frames(self):
        self.assertEqual(simulate([1,2,1,3],5).faults,3)
    def test_invalid_input(self):
        for value in ['', '-1 2', 'x 2']:
            with self.assertRaises(ValueError): parse_pages(value)
        with self.assertRaises(ValueError): validate_capacity(0)
    def test_commas_and_spaces(self):
        self.assertEqual(parse_pages('1, 2 3'),[1,2,3])

if __name__ == '__main__': unittest.main()
