# Timeseries-prediction

Each paper is associated with abstract, authors, year, venue, and title.

#* --- paperTitle
#@ --- Authors
#t ---- Year
#c  --- publication venue
#index 00---- index id of this paper
#% ---- the id of references of this paper (there are multiple lines, with each indicating a reference)
#! --- Abstract

1) Convert the .txt file to .csv with all the information given.

a. We created a DataFrame through which we removed the title, authors, publication
venue, abstract.
b. We deleted records that were not dated.
c. We converted the dataset into a table for better and faster processing.

2) Format of the new table: [Ids] lines and columns [years] up to 600,000 entries.

3) Each position is increased by 1 each time a paper refers to another paper in a particular
year.

4) With this amendment we will use our data on the neural network.

5) Looking at the data, we see a rather sparse table so we do extra filtering to reduce it even
further.
a. We deleted the first 50 years since they had little or no references at all.
b. We deleted the rows that were referenced less than 90 times.

Ending up with 1865 records to train in our neural network.
