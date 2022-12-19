APP User Stories

As a fan of live music, I want to know what people have thought about concerts from particular artists so I know which ones to buy tickets for when the artist is playing in my area.
I want to be able to search tweets about a certain artist that I am interested and get back information about whether people liked or disliked a concert from that artist that they attended.

As a music venue owner, I want to see how popular a particular artist has been at their concerts so I can decide whether I should host them when the are touring in my city.
I want to be able to compare tweets about multiple artists that are about to go on tour so I can know which ones are more popular and decide which artists I will host at my venue.

APP MVP
My App should be able to retrieve tweets based on hashtags surrounding the artists and their performances (i.e. #"artist name", #"tour and tour year", #tickets, #live, etc).  The retrieved tweets should then be analyzed for their general sentiment (positive or negative sentiment) and the output should be the result of this sentiment.   
Modular Design:

Interface module: App user is given ability to choose which artist(s) to recieve information on by assigning the artist to a variable.
Tweet Retrieval module:  App uses the recent search endpoint to gather recently posted tweets based on the relevant hashtags.
Sentiment Analysis module:  Google NLP sentiment analysis tool reviews text in retrieved tweets.
Sentiment Comparison module:  If comparing responses to multiple artists, app compares sentiment scores to determine which of the scores is higher, aka more positive.  Returns result of the comparison as part of string: "The artist with a better reputation is ____________".
Artist Review module:  If user is only looking for information on one artist, the app takes the sentiment analysis score and associates a negative score (less than zero) with an artist that the user should avoid.  If the score is positive (higher than zero), the app recommends this artist.  
