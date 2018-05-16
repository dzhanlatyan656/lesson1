
def get_answer(question, answers):
	return answers.get(question)


myanswers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
#input(question)
# r = get_answer("привет", myanswers)
# print(r)

# r = get_answer("как дела", myanswers)
# print(r)

q = input("Что скажешь?\n")
r = get_answer(q, myanswers)
print(r)
