# Election_Analysis

## Project overview

Tom is a Colorado Election Bpard employee. He asked us to assist him in the electrion audit for the US Congress for Colorado. He had provided us with the counted votes in a csv file (election_results.csv). The purpose of our mission is to generate a vote count report to certify the US congressional race in the state of Colorado. 

In our report, we will have to retrieve the following data:
1. Total number of votes cast
2. Complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. Winner of the election based on popular vote

We will use Python and Visual Studio Code to run our analysis. 

## Election audit results

* The total votes of this Congressional election is 369,711.
* The Colorado state has 3 counties, Arapahoe, Denver, and Jefferson. The breakdown of the number of votes and the percentage of the total votes for each county is presented in the table below :

![Counties_votes](https://user-images.githubusercontent.com/85641189/124458362-7c748580-dd52-11eb-9fed-acced07d65cd.png)

* The Denver county has recorded the largest number of votes with 82.78% of the total votes.
* Three candidates have run the US congressional race for the Colorado's state: 
  * Charles Casper Stockham
  * Diana DeGette
  * Raymon Anthony Doane
The breakdown of the number of votes and the percentage of the total votes for each candidate is presented in the table below :

![Candidate_votes](https://user-images.githubusercontent.com/85641189/124459297-a1b5c380-dd53-11eb-9351-64f118c888ff.png)

* Diana DeGette won the US Congressional election for the Colorado state with 73.8% of the total votes. She has recorded 272,892 votes.

## Election audit summary

In this project and for this Congressional election, the analysis focuses on two categories of results:
* the result of the votes for each county
* the result of the votes for each candidate.
However, we are able to add other variables and use this script for any election. 

### Code modifications in case of a two-round system
For some elections, we may use a two-round system. In this case, if no candidate receives a required number of votes then there is a runoff between the two candidates with the most votes. 
The code we used in this project determines the winning vote count, the winning percentage, and the winning candidate as follow

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

In case we use a two-round system, we will add a "elif" function to the if statement. The elif statement will be:

        elif (votes == winning_count) and (vote_percentage == winning_percentage):
          print(f'Second round required.')
          
### Code modifications for counting absentee ballots
Depending on state law, voters unable or unwilling to vote at polling stations on Election Day may vote via absentee ballots. Absentee ballots can be sent and returned by mail, or requested and submitted in person, or dropped off in locked boxes. We can add this data to our code in order for the State to be able to highlight this variable. 

I take the hypothesis that the absentee ballots are registered in the same column than the candidate's name. In this case, the absentee ballots will be added to the candidate_option list thanks to the if statement below:

    if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] += 1

The output of the for loop statement below will be the candidate results including the number of votes and the percentage of the total votes for the absentee ballots.            
```
    for candidate_name in candidate_votes:
            votes = candidate_votes.get(candidate_name)
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')"
```
        
We will discuss with the election commission any other modification they need in order to run this script for any election.
