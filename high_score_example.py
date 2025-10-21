filename = 'high_scores.txt'


# open it up and store some scores as csv
with open(filename, 'w') as f:
    # write our high scores
    f.write('Natasha, 1020\n')
    f.write('Charles, 1010\n')
    f.write('Max, 1050\n')


# no open the scores and save them to a high score list of dictionaries
high_score_list = []
with open(filename, 'r') as f:
    read_list = f.readlines()

print(read_list)

# loop over the read_list and store in a dictionary
for line in read_list:
    new_list = line.split(',')
    name = new_list[0]
    score = int(new_list[1])
    print(name,score)
    # append a dict to our high score list
    high_score_list.append({"name":name, "score":score})


print('*'*20)
print(high_score_list)

sorted_high_scores = sorted(high_score_list, key= lambda x: x['score'], reverse=1)
print('*'*40)

print(sorted_high_scores)


