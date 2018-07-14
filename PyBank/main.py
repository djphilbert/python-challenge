import os

# Module for reading CSV's
import csv

csvpath = os.path.join( 'Resources', 'election_data.csv')

# # Method 1: Plain Reading of CSVs
cand_votes = {} 
counter = 0
percent_each = 0

with open(csvpath, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   header = next(csvreader)

   for vote in csvreader:
       counter += 1
       if (vote[2]) in cand_votes.keys():
           cand_votes[vote[2]] += 1
       else:
           cand_votes[vote[2]] = 1

percent = []
for key in cand_votes:
   percent_each = cand_votes[key]/counter *100
   percent.append(f"{key}:{percent_each}%")
winner = max(cand_votes, key=cand_votes.get)
print(cand_votes)
print(counter)
print(percent)
print(winner)

text_file = open("PypollOutput.txt", "w")
text_file.write("Total votes " + str(cand_votes))
text_file.write("Total Counter" + str(counter))
text_file.write("Percentage " + str(percent))
text_file.write("Winner is " + str(winner))
text_file.close()