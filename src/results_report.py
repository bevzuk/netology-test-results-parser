from src.correct_results_counter import CorrectResultsCounter
from src.results_counter import ResultsCounter


class ResultsReport:
    def __init__(self, questions, correct_answers, answers):
        self._questions = questions
        self._correct_answers = correct_answers
        self._answers = answers

    def summary(self):
        data = []
        counters = CorrectResultsCounter(self._correct_answers).count_correct_answers(self._answers)
        for index, question in enumerate(self._questions):
            data.append([question, counters[index]])
        return data

    def summary_sorted_by_count(self):
        return sorted(self.summary(), key=lambda item: item[1])

    def answers(self):
        report = []
        answers_counters = ResultsCounter(self._questions).count_answers(self._answers)
        for question in self._questions:
            report.append(['', ''])
            report.append([question, ''])
            answers = answers_counters[question]
            sorted_answers = list(answers.keys())
            sorted_answers.sort()
            for answer in sorted_answers:
                report.append([answer, answers[answer]])
        return report
