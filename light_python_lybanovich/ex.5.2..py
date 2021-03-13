# """Выведите.на.экран.все.вопросы.из.списка,.а.также.правильные.ответы.в.таком. виде:
# Q:.вопрос A:.ответ"""

questions = [
"We don't serve strings around here. Are you a string?",
"What is said on Father's Day in the forest?",
"What makes the sound 'Sis! Boom! Bah!'?"
   ]
answers = [
"An exploding sheep.",
"No, I'm a frayed knot.",
"'Pop!' goes the weasel."
]

dict_map= ((0,1),(1,2), (2,0))

for q,a in dict_map:
    print(questions[q])
    print(answers[a])