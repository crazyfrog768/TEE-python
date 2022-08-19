print('---------------------------------------')

file = open('group_scores.txt')    # reset to first line
pass_count = 0

for g_scores in file:
    g_scores_list = g_scores.split(' ')  # read the whole line at a time
    print(g_scores_list)    # make a series of number in ONE line to list
    for score in g_scores_list:   # now loop the list
        score_int = int(score)
        print(score_int, end ="-")
        if score_int > 50:
            pass_count += 1
    print()
print('pass 50 : ', pass_count)

file.close()