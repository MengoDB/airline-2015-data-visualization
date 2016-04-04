airline-2015-data-visualization

This project is to display on-time percentage of top 5 airline in 2015 by creating a dimple.js visualization. It is a project for Udacity Data Analyst Nanodegree.


# Data Visualization: U.S. Airline Performance, 2015

By Mengyao Gao, Udacity’s Data Analyst Nanodegree, Project 5

## Summary

This data visualization displays 5 biggest U.S. airlines’ performance in 2015 (Nov. 2014 – Oct. 2015). It shows each airline’s on time percentage for each month. 

## Design

-Exploratory Data Analysis and Cleaning (Python and R)

The dataset, downloaded from RITA, includes all domestic flights from all carriers from Nov. 2014 to Oct. 2015. Python script and Rstudio are used to do exploratory data analysis. In the exploratory process, all the flights are grouped by carriers and month in the year; on-time percentage is calculated in each group. 

Before studying the dataset, I expect that multiple carriers might share similar trends of on-time performance which is impacted by external facts like weather and season. However, under similar trends, different airlines might still have different performance. In our common sense, some airlines have good fame for their on-time arrivals while some airlines have bad fame for their delayed arrivals. I decided to use line chart to represent the similarity and difference of each airline’s on-time performance.

Below is the first plot.
 
![alt tag](https://github.com/MengoDB/airline-2015-data-visualization/blob/master/Rplot.png)

This plot includes 15 carriers. Too many carriers would make this chart too crowded. To display the trends more distinguishable, I truncated the dataset to feature only 5 biggest airlines with 5 highest gross numbers of flights in 2015. The selected airlines are American Airlines Inc., Delta Airlines Inc., ExpressJet Airlines Inc., SkyWest Airlines Inc. and Southwest Airlines Co..

The new line chart with top 5 airlines is shown below.

![alt tag](https://github.com/MengoDB/airline-2015-data-visualization/blob/master/Rplot02_top5.png)
 
My initial evaluation of this chart was that it could clearly show the trends of on-time performance over year. It could answer the audience two questions. The first question: which airline is likely to be on-time and which one not. This helps customers better choose airline when purchasing flight tickets. The second question: which month flights is likely to be delayed on even though he or she chooses the airline with best performance. Weather, travel season or other issues account for delays instead of airline services. The chart would help travellers better plan the trip in different months.

## Data Visualization (dimple.js)

I used D3.js and dimple.js to create the initial data visualization. Specific choices in this sketch is explained as follows:

•	Chart type: Line chart is suitable to display trends and reveal some unusual stories when necessary. In this use case, it shows the common trends of on-time performance for each airline as well as the comparison of performance between them over time.
•	Scatter points is added on the line chart to emphasize the airlines’ individual data points at each month.
•	Y-axis uses percentage as the unit for measure values.
•	Y-axis scale is set from (minimum y - 0.05) to 1 to avoid crowded lines and points.
•	Coloring each line series distinguish airlines from each other.
•	Legend is placed at top right for better organization.

The initial visualization can be viewed at index-initial.html. Screenshot is placed below:

![alt tag](https://github.com/MengoDB/airline-2015-data-visualization/blob/master/initial.png)

## Feedback

I interviewed 3 individuals in person, and asked for their feedback on the initial visualization. Comments are listed below:

Interview #1

I saw in this chart, y axis which represents airlines’ the on-time percentage over months ranges from 74%. I observe similar trends of on-time performance among the five airlines. On August to November, all the airlines perform better than other months while on Feb and June airline is likely to be delayed. Despite of similar trends, Delta performs best on every single month. I also notice an exception that on December, Delta has higher on-time percentage than January while other airlines have lower percentage.

For the layout and encoding of this chart, I think color could be more differentiate. The point could be smaller to make this dashboard cleaner.


Interview #2

This chart is trying to display the on-time performance of the top U.S. domestic flights. In this chart, Delta has the best performance while ExpressJet worst. All the airlines’ on-time percentages are more than 74%. If I was the person to buy flight tickets,  it provided a hint to choose the airline on the aspect of on-time performance.

For the visual code and layout, I think if you add some texts with this chart like the conclusion of distribution over time, it will help me better understand to find the trends.

Interview #3

This chart is a dashboard to show on-time performance among top five domestic airlines over the last year. It is clearly from the board that the airlines have similar trends of on-time performance. On December, February and June, airlines have relatively bad on-time performance. Delta has the better on-time percentages over months compared to other airlines.

For the visual code and layout, you could emphasize on the best value every month.

### Feedback from first submission to Udacity

Summary: The dashboard should focus on one finding and display it to audience. For example, the story that Delta performs best ontime rate over 2015. The other story about seasonality of on-time performance cannot be proved by a single year's data. The selection of the top 5 carriers are not explained.

## Post-feedback Design

With the feedback from the 3 interviewers, I made the following changes to the initial chart:


1.	I changed the radium of all the scatter circles to make the chart cleaner.
2.	I changed the title to 'Delta airlines consistently the top performer of 2015 in on time arrival percentage' which explain my findings more clearly.
3.	I made the line for Delta airline thicker, which could emphasize on its best performance.
4.	I added notes at the end which explained how the airlines were selected to the dashboard.

![alt tag](https://github.com/MengoDB/airline-2015-data-visualization/blob/master/final.png)

## Resources

http://stackoverflow.com/questions/22836594/dimple-js-change-radius-of-circles
https://github.com/PMSI-AlignAlytics/dimple/wiki/dimple.chart

## Data
airline_data.csv: original downloaded dataset.
top5_carriers.csv: cleaned data with top 5 carriers.
