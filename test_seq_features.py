import seq_features
import bioinfo_dicts
import pytest
import string

def test_n_neg_for_single_E_or_D():
    """Perform unit tests on n_neg."""

    assert seq_features.n_neg('E') == 1
    assert seq_features.n_neg('D') == 1

def test_n_neg_for_empty_sequence():
    assert seq_features.n_neg('') == 0

def test_n_neg_for_longer_sequences():
    assert seq_features.n_neg('ACKLWTTAE') == 1
    assert seq_features.n_neg('DDDDEEEE') == 8

def test_n_neg_for_lower_case_sequences():
    assert seq_features.n_neg('acklwttae') == 1

def test_n_neg_for_invalid_amino_acid():

    #Generate a set of letters that are not amino acids
    alphabet = string.ascii_uppercase
    not_aa = []
    for x in not_aa:
        if x not in bioinfo_dicts.aa.keys():
            not_aa.append(x)

    for x in not_aa:
        with pytest.raises(RuntimeError) as excinfo:
            seq_features.n_neg(aa)
        excinfo.match(aa + " is not a valid amino acid")
