# Personal-Brand-Development

Earlier this year, I was selected as Fall 2020 Fellow with [bespoken](https://www.letsbespoken.org), a mentorship program for womxn in music. 
My work as part of this mentorship program includes developing my own artistic personal brand as it related to my music, data science, and everything I do. This brand development project will culminate in the coming months in the form of a new website that integrates my multi-faceted work, and will holistically represent who I am.

An important first step to this is understanding where I am today in my personal branding and finding words to describe my current persona as I'm seen by those around me, and then using that to inform the artistic direction I want to move in. Data-driven decision making is at the core of what I do- both as a data scientist and as a person! So, naturally, I chose to approach this personal branding project in the same way, and created an anonymous survey sent to a pool of friends, family, and colleagues in order to gain a better understanding of how people see me and my work today. This repository contains the results and analysis from that survey.


## The Survey

The survey I created was quite simple, distributed using Google Forms, and contained 3 main required questions.

>1) How would you describe my personality in 3 words?
>2) When is the last time you heard me play music?
>3) How would you describe my music, after hearing me perform in a concert or recital? What 3 words might you walk away with?
  
The survey was sent to 14 people consisting of family, friends, and people who I have worked with musically in the past, and had a 100% response rate.

While the words were the most important piece of feedback for me, the question on how long it has been since each survey-taker has heard me play was important, and could serve as a form of "weighting" the responses for added depth to the analysis.


## The Data

I obtained the data from the survey as responses were coming in, using the Google Sheets API. Because I designed the survey with the analysis in mind, the data was clean and minimal additional cleaning was needed. Mostly, I transformed the data from wide to long, ensured each word was consistent (capitalized, no trailing or leading spaces), and confirmed that words were spelled correctly, etc. There was one word I had to manually correct, as it was written two different ways by two different people ("Hard-working" v.s. "Hardworking").


## The Analysis

Two considerations were taken into account when looking at this data.

>1) Frequency: Are there certain common words that are being used by more people?
>2) Relevance: What are people who have heard me more recently saying in comparison to people who haven't heard me play for a few years? Are there any patterns           there?

This 2nd consideration was especially important, as I know that my personal branding two years ago isn't the same as it is now, and won't be the same in two more years! My personal brand is a reflection of who I am, and it continues to change and evolve as I do. I also noticed that some of the more general words to describe my music (ex: "Beautiful") come from peopple who haven't heard me play recently (or at all!), while some of the more descriptive words come from people who have heard me play more recently.

To visualize the most frequent words in both the personality and music categories, I created the following word cloud, respectively:


![personality](personality_wordcloud.png)


![music](music_wordcloud.png)

## Conclusions & Next Steps

This project is still ongoing, and every day I am continuing to explore who I want to be, the persona I want to exude, and the directions in which I want my personal and artistic projects to go. 

From this analysis, I learned that my friends, family, and colleagues see me in quite a positive, "happy" light. I also realized that my artistic projects may not always 100% reflect my personality and how I interact with those around me. For example, just because those close to me describe me as "thoughtful", "sweet", and "bubbly" doesn't mean that every project I work on will also have these qualities! I may want certain projects to explore other parts of my personality and who I am that friends and family may not see all of the time.

This realization was incredibly eye-opening for me, and I may not have realized it as explicitly if I had not conducted this survey and analyzed the data in this way. If I were to do this survey again in the future (as I am sure I will!) I may also want to get the perspective of people who don't know me very well, to see the impressions my music and I make on people who haven't had the chance to get to know me closely. 

This analysis will be used as another "data point" to see how people percieve me and my music at this early stage of my development as an artist, and ultimately to shape my artistic vision and process going forward! Specifically for this brand development project, I will use the words that are here (and those that aren't!) to inform the visual style/vibe I want reflected on my new website.
