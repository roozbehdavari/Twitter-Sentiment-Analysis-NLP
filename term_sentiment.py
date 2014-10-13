import sys
import json

def new_term_sentiment(sentiment_file,tweets_file):

	term_sentiment = {}
	
	afinnfile = open(sentiment_file,'r')   # Opening the file that contains the sentiments
	modefile = afinnfile.readlines()
	afinnfile.close()

	scores = {}                            # initialize an empty dictionary

	for line in modefile: 
		term, score  = line.split("\t")    # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)          # Convert the score to an integer.


	alltweets = open(tweets_file,'r')      # Opening the file that contains the tweets
	tweetsJson = alltweets.readlines()
	alltweets.close()


	for tweet in tweetsJson:
		if 'text' in json.loads(tweet).keys():		
			tweet = json.loads(tweet)[u'text'].encode('ascii','ignore')
			splitted_tweet = tweet.split()
			splitted_tweet_lower = [x.lower() for x in splitted_tweet]
		
			total_score = 0
					
			for word in splitted_tweet_lower:
				if word in scores.keys():
					total_score += scores[word]
			for word in splitted_tweet_lower:
				if word not in scores.keys():
					if word in term_sentiment.keys():
						term_sentiment[word] += int(total_score)
					else:
						term_sentiment[word] = int(total_score)
	
	for term in term_sentiment:
		print term, term_sentiment[term]		
				

def main():
	sent_file = sys.argv[1]
	tweet_file = sys.argv[2]
	new_term_sentiment(sent_file,tweet_file)


if __name__ == '__main__':
    main()
