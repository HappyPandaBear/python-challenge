import csv

votes = {}

with open('PyPoll_Resources_election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        candidate = row[2]
        if candidate not in votes:
            votes[candidate] = 1
        else:
            votes[candidate] += 1

values = votes.values()
total_votes = sum(values)

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
for key, value in votes.items():
    print(f'{key}: {value / total_votes:.3%} ({value})')
print(f'-------------------------')
print(f'Winner: {max(votes, key=votes.get)}')
print(f'-------------------------')

file = open('PyPoll.txt','a')
file.write(f'Election Results\n',)
file.write(f'-------------------------\n')
file.write(f'Total Votes: {total_votes}\n')
file.write(f'-------------------------\n')
for key, value in votes.items():
    file.write(f'{key}: {value / total_votes:.3%} ({value})\n')
file.write(f'-------------------------\n')
file.write(f'Winner: {max(votes, key=votes.get)}\n')
file.write(f'-------------------------\n')
file.close()