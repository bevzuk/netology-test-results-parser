import pytest

from src.results_report import ResultsReport


@pytest.fixture
def results_report(questions, correct_answers, answers):
    return ResultsReport(questions, correct_answers, answers)


@pytest.mark.parametrize('questions', [["Q1", "Q2", "Q3"]])
@pytest.mark.parametrize('correct_answers', [["Correct1", "Correct2", "Correct3"]])
@pytest.mark.parametrize('answers', [[
    ["Correct1", "Correct2", "Correct3"],
    ["Correct1", "Correct2", "Wrong"],
    ["Correct1", "Wrong", "Wrong"]
]])
def test_report_for_multiple_responses(results_report):
    report_data = results_report.summary()
    assert report_data == [["Q1", 3], ["Q2", 2], ["Q3", 1]]


@pytest.mark.parametrize('questions', [["Q1", "Q2", "Q3"]])
@pytest.mark.parametrize('correct_answers', [["Correct1", "Correct2", "Correct3"]])
@pytest.mark.parametrize('answers', [[
    ["Correct1", "Correct2", "Correct3"],
    ["Correct1", "Correct2", "Wrong"],
    ["Correct1", "Wrong", "Wrong"]
]])
def test_report_for_multiple_responses_ordered_by_count(results_report):
    report_data = results_report.summary_sorted_by_count()
    assert report_data == [["Q3", 1], ["Q2", 2], ["Q1", 3]]


@pytest.mark.parametrize('questions', [["Q1", "Q2"]])
@pytest.mark.parametrize('correct_answers', [["Correct 1.1, Correct 1.2", "Correct 2"]])
@pytest.mark.parametrize('answers', [[
    ["Correct 1.1, Correct 1.2", "Correct 2"],
    ["Correct 1.2, Correct 1.1", "Correct 2"],
    ["Correct 1.1, Wrong", "Wrong"]
]])
def test_answers_for_multiple_responses(results_report):
    report_data = results_report.answers()
    assert report_data == [
        ["", ""],
        ["Q1", ""],
        ["Correct 1.1, Correct 1.2", 2],
        ["Correct 1.1, Wrong", 1],
        ["", ""],
        ["Q2", ""],
        ["Correct 2", 2],
        ["Wrong", 1]
    ]

