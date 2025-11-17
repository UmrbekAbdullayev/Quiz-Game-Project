import random
# using ast module, reads the data from txt file
import ast                                           
with open('question_bank.txt', 'r', encoding='utf-8') as file:
    text = file.read()
questions = ast.literal_eval(text.split('=', 1)[1].strip())    

# intro to the quiz
print('''Welcome to our quiz game! 
This quiz is about Python programming language
If you want to finish your quiz, press <<< exit/quit >>>
ARE YOU READY?
       ''')

# creating a list of possible wrong answers to use it inside the code
wrong_answers = ['a', 'b', 'c', 'd']

# the quiz starts
game_is_on = True
ques_range = int(input('How many questions do you want your section to be?   '))       # number of questions per section 

while game_is_on:           # the main loop
    nth_question = 1        # the first question 
    score = 0  
    section_questions = random.sample(questions, ques_range)
    for random_question in section_questions:
        print(nth_question, end= '. ') 
        options = '\n'.join(random_question['options'])                  # storing the options list so that later we can print 
        question = (input(f'{random_question['question']}\n'             # printing the questions with 4 variants to the console
                        f'{options}\n')).lower()
        wrong_answers.remove(random_question["answer"])                  # removes the correct answer from the list
        
        if question == 'exit' or question == 'quit':                     # checking for quits or exits
            print(f'Thank you! Your score from this section: {score}')
            game_is_on = False
            break
        
        while True:
            if question == random_question['answer']:                    # checking for correct answer
                print('Correct answer! ✅ \n')
                score += 1
                wrong_answers.append(random_question['answer'])          
                break
            
            elif question in wrong_answers:                              # checking for wrong answers
                print('Wrong answer! ❌ ')
                print(f'The correct answer is: {random_question["answer"]}\n ')
                wrong_answers.append(random_question['answer'])
                break
            
            else:
                question= input('You typed something else. Please choose again: ').lower() # checking for anything else from a, b, c, d
                wrong_answers.append(random_question['answer'])  
        nth_question += 1                                                                  # the order of questions
    
    print(f'Your score out of {ques_range}:   {score} 👏') 
    while True:
        want_to_continue = (input('Do you want to continue? Yes/No:    \n')).lower()
        if want_to_continue == 'no':
            game_is_on = False
            break
        elif want_to_continue != 'yes' and want_to_continue != 'no':
            want_to_continue = (input('Do you want to continue? Yes/No:    \n')).lower()
        else:
            break    