class ResultsCounter:
    def __init__(self, questions):
        self.questions = questions

    def count_answers(self, answers):
        counts = self._questions_as_dict()
        for person_answers in answers:
            for test_index, test_answer in enumerate(person_answers):
                test_answer = self._normalize(test_answer)
                question = self.questions[test_index]
                question_counts = counts[question]
                if test_answer not in question_counts:
                    question_counts[test_answer] = 0
                question_counts[test_answer] = question_counts[test_answer] + 1
        return counts

    def _questions_as_dict(self):
        dict = {}
        for question in self.questions:
            dict[question] = {}
        return dict

    def _normalize(self, answer):
        answers_list = answer.split(", ")
        answers_list.sort()
        return ", ".join(answers_list)