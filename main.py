import unittest

from itertools import zip_longest


class Frame:
    def __init__(self, first_roll, second_roll):
        self.first_roll = first_roll
        self.second_roll = second_roll

    def score(self):
        return self.first_roll + self.second_roll

    def is_spare(self):
        return self.score() == 10


class StrikeFrame(Frame):
    def __init__(self):
        pass

    def score(self):
        return 10


class NullFrame:
    def is_spare(self):
        return False


def calculate_score(frames):
    result = 0
    for previous_frame, frame in get_previous_frames_paired_with_current_frames(frames):
        if previous_frame.is_spare():
            result += frame.first_roll
        result += frame.score()
    return result


def get_previous_frames_paired_with_current_frames(frames):
    return zip([NullFrame()] + frames[:-1], frames)


class TestBowling(unittest.TestCase):

    def test_score_zero_for_every_roll(self):
        frames = [
            Frame(0, 0),
            Frame(0, 0),
            Frame(0, 0),
            Frame(0, 0),
            Frame(0, 0),
            Frame(0, 0),
            Frame(0, 0),
            Frame(0, 0),
            Frame(0, 0),
            Frame(0, 0)
        ]
        score = calculate_score(frames)
        self.assertEqual(0, score)

    def test_score_one_for_one_roll(self):
        frames = [
            Frame(1, 0),
            Frame(0, 0),
            Frame(0, 0),
            Frame(0, 0),
            Frame(0, 0),
            Frame(0, 0),
            Frame(0, 0),
            Frame(0, 0),
            Frame(0, 0),
            Frame(0, 0)
        ]
        score = calculate_score(frames)
        self.assertEqual(1, score)

    def test_rolling_a_spare_doubles_next_roll(self):
        frames = [
            Frame(1, 9),
            Frame(1, 1),
            Frame(1, 1),
            Frame(1, 1),
            Frame(1, 1),
            Frame(1, 1),
            Frame(1, 1),
            Frame(1, 1),
            Frame(1, 1),
            Frame(1, 1)
        ]
        score = calculate_score(frames)
        self.assertEqual(29, score)

    # def test_rolling_a_strike_on_first_frame(self):
    #     frames = [
    #         StrikeFrame(),
    #         Frame(0, 0),
    #         Frame(0, 0),
    #         Frame(0, 0),
    #         Frame(0, 0),
    #         Frame(0, 0),
    #         Frame(0, 0),
    #         Frame(0, 0),
    #         Frame(0, 0),
    #         Frame(0, 0)
    #     ]
    #     score = calculate_score(frames)
    #     self.assertEqual(10, score)
