Okay so I have to tried to classify entities with regular expression and entity recognition from spacy. 

If you see a tag that looks like <TAG> that means a regular expression made it 

If you see a tag that is in all caps it was done by spacy 

	On second thought we probably should rap those in <> those as well 
	(easier for network to recongine those are special tokens)

I also added start and stop tokens, that will allow us to put the location either at the end or beginning of the sequence 

Last thing is I used a lemmatizer from wordnet to try and stardardize the words a little. If you think we should use something else that is totally cool but I have had some success with lemmatizers over stemmers. 

There are alot of things that I am missing if you look at the data though, one thing in particular that I thought was unique is the * character. It almost means something different when people wrap text arround those. So i tried to separate them. 

Give the script and data a glance and let me know any updates that you have


