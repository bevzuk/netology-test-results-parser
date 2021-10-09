class ResultsInspector:
    def __init__(self, correct_responses):
        self.correct_responses = correct_responses.split(", ")
        self.correct_responses.sort()

    def test(self, responses):
        responses_list = responses.split(", ")
        responses_list.sort()
        return responses_list == self.correct_responses
