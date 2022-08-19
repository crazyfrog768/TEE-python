file_read = open('group_scores.txt')
file_write = open('test.txt', 'w')

for g_score in file_read:    # read each line
    g_score_list = g_score.split(' ')  # make it to list
    sum_score = 0
    for score in g_score_list:
        score_int = int(score)
        sum_score += score_int

    average_score = sum_score / len(g_score_list)
    file_write.write(str(average_score) + '\n')


file_read.close()
file_write.close()

