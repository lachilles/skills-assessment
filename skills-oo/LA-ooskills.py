# # Part 1: Discussion
# # What are the three main design advantages that object orientation can provide?
# Polymorphism: flexibility of types without condictionals
# Encapsulation: hiding complexity. Don't need to know info a method uses internally.
# Abstraction: when you design base classes that are non-functioning themselves, but are meant to be useful only when subclasses and when additional attributes or methods are defined.

# # Explain each concept.

# # 1. What is a class?
# A class is a "type" of thing, like String(str) or File(file)

# # 2. What is an instance attribute?
# An attribute (or characteristic) unique to the instance (an individual instance of a class). Instance attribute overrides class attributes.

# # 3. What is a method?
# Function defined on a class

# # 4. What is an instance in object orientation?
# An individual instance of a class.

# # 5. How is a class attribute different than an instance attribute? Give an example of when you might use each.
# Class attributes are characteristics unique to the class and consistant across instances of it.
# An instance attribute overrides the class attribute.
# For example, Melon Order class may have an attribute price = 5. The price per melon is consistant regardless of qty or which state it is shipped to. However, tax may vary depending on the state. Therefore, tax would be an instance attribute of Melon Order class, (for example tax = .075 if state = CA)

# Parts 2 through 5:
# Create your classes and class methods

#
"""Part 2-5"""


class Student(object):
    """Student class attributes sets first_name, last_name, address at initialization"""
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    """Question class attributes sets question and answer"""
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        print self.question
        player_answer = raw_input("True or False: ")
        #Player inputs True or False
        if player_answer == self.answer:
            return True
        else:
            return False

class Exam(object):
    """Exam class attribute sets exam name"""

    def __init__(self, name):
        # super(Question, self).__init__(name)
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        question = Question(question, correct_answer)
        self.questions.append(question)
        # exam = Exam('midterm')
        # exam.add_question.add()
        # question.ask_and_evaluate()

    def administer(self):
        score = 0
        for current_question in self.questions:
            is_correct = current_question.ask_and_evaluate()
            if is_correct is True:
                score += 1
        return score


        # def __init__(self, score):
            # score = 0
            # super(Question, self).__init__()
            # for question in question.ask_and_evaluate():
            #     if player_answer is True:
            #         score += 1
            #     elif player_answer is False:
            #         pass
            #     else:
            #         pass

volleyball_exam = Exam('Luke Skyblocker exam')
volleyball_exam.add_question(
    'Who is the newest player on the team? ', 'Vish')
volleyball_exam.add_question(
    'Who is the tallest player on the team? ', 'Christian')


music_exam = Exam('Music exam')
music_exam.add_question(
    'What is #? ', 'sharpe')
music_exam.add_question(
    'What is my favorite queen song?', 'Christian')

volleyball_exam.administer()




