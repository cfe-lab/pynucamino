import unittest
from unittest import mock

import pynucamino.functions as functions


class TestAlign(unittest.TestCase):

    mock_seq = "> Mock Sequence\ngattaca"
    mock_profile = "pun"
    mock_genes = ("ralphlauren", "hollister")

    mock_alignment = mock.Mock()
    mock_result = {"mock": "result"}
    mock_alignment.result = mock_result

    @mock.patch("pynucamino.functions.Nucamino", return_value=mock_alignment)
    def test_align(self, nuc_mock):
        result = functions.align(
            seqs=self.mock_seq,
            profile=self.mock_profile,
            genes=self.mock_genes,
        )
        self.assertEqual(result, self.mock_result)
        nuc_mock.assert_called_with(
            seqs=self.mock_seq,
            profile=self.mock_profile,
            genes=self.mock_genes,
            check=True,
        )
