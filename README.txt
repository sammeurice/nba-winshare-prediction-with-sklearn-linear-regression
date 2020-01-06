    WEB SCRAPER

This is a web scraper for basketballreference.com that I made because I wanted to use the data
for a sklearn linear regression project.

The program allows the user to decide a span of years that they want to collect data for.
I also did some cleaning on the data to make it usable for sklearn. 
The program will create a .csv file with the data in the same directory.

The stats for the selected year, and the win shares (an advanced statistic) of the following year are collected.
Both years are cross referenced and modified so that the data has a player's year as a row, and their win shares as
the last column. This was tricky, as of course the players in the league changed each year, and thus the order of
the lists would be different. Also, as a product of how the data on the website is structured, if a player is traded
their name appears twice on the list, so I had to account for this. I don't think I used the most efficient 
algorithms for this process, as I'm still learning about algorithms, so I plan on improving this once I learn more.
Additionally, before the year 2000, the program doesn't work sometimes, I don't know why yet but I think it has
something to do with a different structuring of the website on those years.


    MODEL TRAINING
    
A lot of the work was already done in the web scraper script, which is probably not the best way to have gone about this in retrospect
But at allowed for less work in this portion of the project
I did a little more data cleaning, then simply plugged my data into the sklearn linearregression package
the result of this test yield an average error of 2, which is not terrible but also could be a lot better


  POSSIBLE IMPROVEMENTS - Things that I would like to do if I can find the time
  
1. Clean up the code - I'm still getting used to clean coding practices

2. For some reason the built in standardizer causes some of the data to overflow,  the error says that it is because the standardizer takes 64 bit floats and that the data is too small, but even after i convert the data to 64 bit float it still gives the same error, the only solution i found was to use the numpy.nan_to_num function, which may have some part in the innacuracy of the model

3. Just generally try to find ways to improve the model, maybe test out different algorithms such as knn, which i think would be good, but perhaps time consuming due to the amount of features and data. Try using k folds when splitting training and testing data, etc.

4. I would like to build a web app that allows the user to select a player and have my model predict their win shares for the following season. I'm currently learning some html and how to use the django framework for python, so this would be a fun way to intersect these two projects. I would have to make another web scraper to collect this years player stats, then relay that vector to my model, and output the result. 
