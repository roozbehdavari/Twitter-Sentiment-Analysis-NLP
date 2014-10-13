import sys
import json
import re

def frequency(sentiment_file,tweets_file):
	
	afinnfile = open(sentiment_file,'r')   # Opening the file that contains the sentiments
	modefile = afinnfile.readlines()
	afinnfile.close()

	scores = {}                            # initialize an empty dictionary

	for line in modefile: 
		term, score  = line.split("\t")    # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)          # Convert the score to an integer. 	
	
	state_sentiment = {}

	alltweets = open(tweets_file,'r')      # Opening the file that contains the tweets
	tweetsJson = alltweets.readlines()
	alltweets.close()


	for tweet in tweetsJson:
		if 'text' in json.loads(tweet).keys():
			if  type(json.loads(tweet)[u'place']) != type(None):					# Picking only tweets with location info
				if json.loads(tweet)[u'place'][u'country'] == 'United States':		# Picking tweets in USA
					state_or_country =  json.loads(tweet)[u'place'][u'full_name']	
					if re.search(r',\s.*',state_or_country).group()[2:] != 'USA':	# Picking tweets that have state abbreviation
						state = re.search(r',\s.*',state_or_country).group()[2:]
						if len(state) == 2:
	
							tweet = json.loads(tweet)[u'text'].encode('ascii','ignore')    # Measuring the tweet score
							splitted_tweet = tweet.split()
							splitted_tweet_lower = [x.lower() for x in splitted_tweet]
		
							total_score = 0
					
							for word in splitted_tweet_lower:
								if word in scores.keys():
									total_score += scores[word]
					
							if state in state_sentiment.keys():
								state_sentiment[state] += total_score						
							else:
								state_sentiment[state] = total_score						
	
	state_rank = []
	for states in state_sentiment:
		state_rank.append(state_sentiment[states])
	
	for states in state_sentiment:
		if state_sentiment[states] == max(state_rank):
			print states
				
				

def main():
	sentiment_file = sys.argv[1]
	tweet_file = sys.argv[2]
	frequency(sentiment_file,tweet_file)


if __name__ == '__main__':
    main()
