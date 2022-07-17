#Magic 8-ball program
import random

responses = ["Yes", "No", "Maybe So", "Ask Again", "Of Course", "Definitely", "Negative", "Of Course Not", "Don't Know"]
random.shuffle(responses)
print(random.choice(responses))