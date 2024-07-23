from random import shuffle


def question(q, correct, wrong, *sols):
    a = -1
    cor_sol = sols[0]
    sols = list(sols)
    shuffle(sols)
    while a not in range(1, len(sols)+1):
        print(q)
        for z in range(len(sols)):
            print(str(z + 1) + ")", sols[z])
        try:
            a = int(input("Your choice?\n"))
        except ValueError:
            print("Incorrect. Type of the nums above\n")
    if a == sols.index(cor_sol) + 1:
        print("\n" + correct)
        return 1
    else:
        print(wrong)
        return 0


res_score = 0

res_score += question("What did the Hermione`s cat to help friends to pass the Iva?",
                      "yeap, the lever. No random throwing of the tree",
                      "go reread the third book. it is really amazing part of story",
                      "pulled the lever", "he cried to disarrange it",
                      "he scrapped it", "he sang a song to sleep it")


print("your score is:", res_score)
