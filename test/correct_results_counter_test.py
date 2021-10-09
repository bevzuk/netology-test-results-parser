import pytest

from src.correct_results_counter import CorrectResultsCounter


@pytest.fixture
def correct_results_counter(correct_answers):
    return CorrectResultsCounter(correct_answers)


@pytest.mark.parametrize('correct_answers', [["A"]])
def test_can_count_correct_answers_of_single_response(correct_results_counter):
    correct_answers_count = correct_results_counter.count_correct_answers([["A"]])
    assert correct_answers_count == [1]


@pytest.mark.parametrize('correct_answers', [["A"]])
def test_can_count_incorrect_answers_of_single_response(correct_results_counter):
    correct_answers_count = correct_results_counter.count_correct_answers([["B"]])
    assert correct_answers_count == [0]


@pytest.mark.parametrize('correct_answers', [["A, B", "A, B"]])
def test_can_count_correct_answers_of_multiple_responses_ignore_order(correct_results_counter):
    correct_answers_count = correct_results_counter.count_correct_answers([["B, A", "C, A"]])
    assert correct_answers_count == [1, 0]


@pytest.mark.parametrize('correct_answers', [["A, B", "A, B"]])
def test_can_count_correct_answers_of_single_responses_ignore_order(correct_results_counter):
    correct_answers_count = correct_results_counter.count_correct_answers([["B, A", "B, A"]])
    assert correct_answers_count == [1, 1]


@pytest.mark.parametrize('correct_answers', [["A, B", "C, D"]])
def test_can_count_correct_answers_of_multiple_responses_ignore_order(correct_results_counter):
    correct_answers_count = correct_results_counter.count_correct_answers([
        ["B, A", "D, C"],
        ["A, B", "C, D"]])
    assert correct_answers_count == [2, 2]
