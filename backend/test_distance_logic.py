import unittest

from backend.app import _sanitize_route_distance


class DistanceSanityTest(unittest.TestCase):
    def test_implausible_route_is_rejected_instead_of_replaced_by_estimate(self):
        # Do not convert an implausible router snap into a made-up road distance.
        distance = _sanitize_route_distance(17.0, 23.7)
        self.assertIsNone(distance)

    def test_normal_route_is_kept(self):
        distance = _sanitize_route_distance(17.0, 19.5)
        self.assertAlmostEqual(distance, 19.5, places=1)


if __name__ == "__main__":
    unittest.main()
