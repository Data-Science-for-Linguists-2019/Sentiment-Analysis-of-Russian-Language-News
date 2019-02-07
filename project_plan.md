Project Ideas
=============
<hr>
Comparative analysis of sentiment of Russian language news sources

- Summary
	- I would scrape text from a variety of Russian language news sources, both Russia-based and Western (e.g. Radio Cvoboda and/or BBC Novosti, vs Pravda, RT, and/or Izvestia (I may wanna look up what sources people consider "news" in Russia, Izvestia seems kind of tabloid-y)). I would take articles from the same time period and on the same general topic (either Russia, the US, or World news). Then I would do some sort of analysis on this data. I could probably do something based on just what people/topics appear most common in each source, as well as a sentiment analysis. 
- Data
	- The data would be a bunch of txt files which correspond to articles from each site. I could probably use Python's NLTK corpusreader method but I would have to read up on that. I'm also not sure if that works well with Russian. To scrape the data set I would use BS4 and urllib. I would go on the page that links to all the news articles for the topic I pick, find all the links with beautiful soup, then read through those pages source code and scrape the body of their article. I've done this before with Amnesty International, so I think I can handle it. 
	- In terms of size, I would probably pick a short-ish period of time, maybe 3 days to a week, since each website usually has (depending on the day) a bunch of articles daily (Izvestiya for example has like 40 articles today). I could also pick a certain start/end date, and then take the first X number of articles from that day on. I'll probably start with 2 sources but if I find the time I could do like 4 or 5 maybe.
- Analysis
	- *What is my end goal?* <br> My end goal is to find how different news sources discuss the same topics, and whether they tend to discuss different topics to different degrees.
	- *What linguistic analysis do I have in mind?* <br> The main linguistic analysis method I would use would be sentiment analysis. I would need to probably create some sort of training set and a test set to figure out it's accuracy, which would probably require me to go through and mark a certain number of articles for sentiment. (How many would I need to mark? I obviously can't mark every article, since it would take forever and also nullify the point of using computational methods.) Alternatively, I could try to find a classifier that was already created to do this analysis.
	- *Hypothesis?* <br> I would think that Western based news sources would speak about Russia more negatively than Russian based sources and vice versa.
- Presentation
	- I can't think of anything special re the presentation.
- Potential difficulties
	- Many of the websites load the page more as you scroll down. I'm not really sure how this would affect webscraping. Are only the pages that are loaded first available when you request the source code ? Would there be some kind of error ?
	- Would my manual analysis of sentiment be less valid since I am not at a native level of Russian ? Also, would the number of articles I have to tag in order to make a good classifier be too large for me to read through in a realistic amount of time? Like, if I used 2000 articles, would I need to go through 200 articles or something? Or do I just need to tag enough that my test set has a reasonable error margin?
    
