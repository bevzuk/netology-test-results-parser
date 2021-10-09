from src.results_inspector import ResultsInspector


class CorrectResultsCounter:
    def __init__(self, correct_results):
        self.correct_results = correct_results

    def count_correct_answers(self, test_results):
        counts = []
        for index, correct_result in enumerate(self.correct_results):
            inspector = ResultsInspector(correct_result)
            count = 0
            for response in test_results:
                response_to_question = response[index]
                if inspector.test(response_to_question):
                    count = count + 1
            counts.append(count)
        return counts


