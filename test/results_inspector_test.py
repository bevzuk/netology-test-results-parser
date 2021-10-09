import pytest

from src.results_inspector import ResultsInspector


@pytest.fixture
def results_inspector(correct_answers):
    return ResultsInspector(correct_answers)


@pytest.mark.parametrize('correct_answers', ["A"])
def test_single_correct_result(results_inspector):
    correct = results_inspector.test("A")
    assert correct


@pytest.mark.parametrize('correct_answers', ["A"])
def test_single_incorrect_result(results_inspector):
    correct = results_inspector.test("B")
    assert not correct


@pytest.mark.parametrize('correct_answers', ["A, B"])
def test_multiple_correct_result(results_inspector):
    correct = results_inspector.test("B, A")
    assert correct


