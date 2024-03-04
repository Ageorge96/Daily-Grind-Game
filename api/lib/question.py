class Question:
    def __init__(self, id, question, options, answer):
        self.id = id
        self.question = question
        self.options = options
        self.answer = answer

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "options": self.options,
            "answer": self.answer
        }