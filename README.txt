This is a simple web scraper for basketballreference.com that I made because I wanted to use the data
for a sklearn linear regression project (which I'm still working on).

The program allows the user to decide a span of years that they want to collect data for.
I also did some cleaning on the data to make it usable for tensorflow. 
The program will create a .csv file with the data in the same directory.

The stats for the selected year, and the win shares (an advanced statistic) of the following year are collected.
Both years are cross referenced and modified so that the data has a player's year as a row, and their win shares as
the last column. This was tricky, as of course the players in the league changed each year, and thus the order of
the lists would be different. Also, as a product of how the data on the website is structured, if a player is traded
their name appears twice on the list, so I had to account for this. I don't think I used the most efficient 
algorithms for this process, as I'm still learning about algorithms, so I plan on improving this once I learn more.
Additionally, before the year 2000, the program doesn't work sometimes, I don't know why yet but I think it has
something to do with a different structuring of the website on those years.



