import pytest

from src.results_counter import ResultsCounter


@pytest.fixture
def results_counter(questions):
    return ResultsCounter(questions)


@pytest.mark.parametrize('questions', [["Q1"]])
def test_can_count_answers_of_single_answer(results_counter):
    answers_count = results_counter.count_answers([
        ["A"]
    ])
    assert answers_count == {"Q1": {"A": 1}}


@pytest.mark.parametrize('questions', [["Q1"]])
def test_can_count_answers_of_two_answers(results_counter):
    answers_count = results_counter.count_answers([
        ["A"], ["A"]
    ])
    assert answers_count == {"Q1": {"A": 2}}


@pytest.mark.parametrize('questions', [["Q1", "Q2"]])
def test_can_count_single_answers_of_multiple_questions(results_counter):
    answers_count = results_counter.count_answers([
        ["A", "B"],
        ["A", "C"],
    ])
    assert answers_count == {
        "Q1": {"A": 2},
        "Q2": {"B": 1, "C": 1}
    }


@pytest.mark.parametrize('questions', [["Q1"]])
def test_can_count_similar_answers(results_counter):
    answers_count = results_counter.count_answers([
        ["A, B"],
        ["B, A"],
    ])
    assert answers_count == {
        "Q1": {"A, B": 2}
    }
