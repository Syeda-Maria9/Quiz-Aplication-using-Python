print ('''\t\t\t\t===================
               WELCOME TO THE QUIZ
               ===================''')
select=input('''\t Do you want to login as ADMIN(A) OR as PLAYER(P):
                ⇨''').upper()
if select=="A":
        def login():
            username=input("Enter username: ")
            password=input("Enter password: ")
            if password=="batch2021" and username=="cis":
                print("YOU ARE SUCCESSFULLY LOGGED IN")
            else:
                print("INVALID USERNAME OR PASSWORD")
                login()
        login()


        def add(b):
            with open(b, "a+") as f:
                f.write('\n{}\\na{}\\nb){}\\nc{}\\nd{}-{}-'.format(input('Enter Question: '),
                                                                   input('Enter Option A: '),
                                                                   input('Enter Option B: '),
                                                                   input('Enter Option C: '),
                                                                   input('Enter Option D: '),
                                                                   input('Enter Ans: ')))
        def view(a):
            with open(a, "r") as f:
                contents = f.readlines()
                print(contents)
                for question in contents:
                    questions = question.split("-")
                    q = questions[0].replace('\\n', '\n')
                    print(q)
                    a = questions[1]
                    print('ANSWER: ', a + '\n')
        view_add_admin=input('''\t Enter (A) to add question OR Enter (V) to view question
                            ⇨''').upper()
        if view_add_admin=="V":
            domain=input("Please write (AI) for AI domain OR CS for CS domain ⇨ ").upper()
            if domain=='AI':
                level=input("For Easy level (E) and for Hard level (H): ").upper()
                if level=="E":
                    view("AI_easy.txt")
                elif level=="H":
                    view("AI_hard.txt")
            elif domain=="CS":
                level=input("For Easy level (E) and for Hard level (H): ").upper()
                if level=="E":
                    view("CS_easy.txt")
                elif level=="H":
                    view("CS_hard.txt")
        elif view_add_admin=="A":
            domain=input("Please write (AI) for AI domain OR CS for CS domain ⇨").upper()
            if domain=='AI':
                level=input("For Easy level (E) and for Hard level (H): ").upper()

                if level=="E":
                     add("AI_easy.txt")

                elif level=="H":
                        add("AI_hard.txt")
                        
            elif domain=="CS":
                level=input("For Easy level (E) and for Hard level (H): ").upper()

                if level=="E":
                    add("CS_easy.txt")

                elif level=="H":
                    add("CS_hard.txt")

elif select=="P":
    def player_quiz(level):
        with open (level) as f:
            score=0
            contents=f.readlines()
            for question in contents:
                question=question.split("-")
                q=question[0].replace('\\n','\n')
                print(q)
                ans=input("Enter your ans: ")
                if ans==question[1]:
                    score+=1
            print("your score is",score,"out of 10")
    
    Player_name:input("\nEnter player's name:")
    quiz_domain=input("Enter *AI* for AI quiz OR Enter *CS* for CS quiz:\n ⇨ ").upper()
    
    if quiz_domain=="AI":
        level=input("\t Enter *E* for easy level OR *H* for hard level: \n⇨ ").upper()
        if level=="E":
            print("\t---------AI EASY QUIZ---------\t")
            player_quiz ("AI_easy.txt")
        elif level=="H":
            print("\t---------AI HARD QUIZ---------\t")
            player_quiz("AI_hard.txt")
               

    elif quiz_domain=="CS":
        level=input("\t Enter *E* for easy level OR *H* for hard level: \n⇨ ").upper()
        if level=="E":
            print("\t---------CS EASY QUIZ---------\t")
            player_quiz ("CS_easy.txt")
        elif level=="H":
            print("\t---------CS HARD QUIZ---------\t")
            player_quiz ("CS_hard.txt")



            

