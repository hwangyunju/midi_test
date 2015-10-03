#!/usr/bin/python
import unittest
from midi_comparator import MIDIComparator


class TestPitch(unittest.TestCase):

    def test_identical_pitch_sequences(self):
        mc = MIDIComparator('tests/data/score1.mid', 'tests/data/score1.mid')
        # comparing two identical sequences shall give a ratio of 1.0
        assert mc.get_pitch_similarity_ratio() == 1.0

    def test_identical_rhythm_sequences(self):
        mc = MIDIComparator('tests/data/score2.mid', 'tests/data/score2.mid')
        # comparing two identical sequences shall give a ratio of 1.0
        assert mc.get_rhythm_similarity_ratio() == 1.0

    def test_identical_velocity_sequences(self):
        mc = MIDIComparator('tests/data/score3.mid', 'tests/data/score3.mid')
        # comparing two identical sequences shall give a ratio of 1.0
        ratio = mc.get_velocity_similarity_ratio()
        assert ratio == 1.0
        
    def test_identical_sequences(self):
        mc = MIDIComparator('tests/data/score4.mid', 'tests/data/score4.mid')
        # comparing two identical sequences shall give a ratio of 1.0
        ratio = mc.get_similarity_ratio()
        assert ratio == 1.0

    def test_forte_piano_velocity_sequences(self):
        # tests/data/score5 - forte
        # tests/data/score6 - piano
        mc = MIDIComparator('tests/data/score5.mid', 'tests/data/score6.mid')
        ratio = mc.get_velocity_similarity_ratio()
        assert 0.9 < ratio < 0.92

    def test_rhythm_1_bar_rhythm_shift(self):
        mc = MIDIComparator('tests/data/score7.mid', 'tests/data/score7_1_bar_shift.mid')
        # comparing two sequences, where the second is shifted 1 bar from the first one
        ratio = mc.get_rhythm_similarity_ratio()
        assert ratio == 1.0
                
    def test_one_note_diff_sequences(self):
        mc = MIDIComparator('tests/data/score2.mid', 'tests/data/score3.mid')
        # score3 is missing one note present in score 2
        ratio = mc.get_similarity_ratio()
        assert 0.87 < ratio < 0.92
                
if __name__ == "__main__":
    unittest.main()
