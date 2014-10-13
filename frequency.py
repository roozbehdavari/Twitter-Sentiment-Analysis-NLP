import sys
import json

def frequency(tweets_file):
	
	term_count = {}

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
				if word in term_count.keys():
					term_count[word] += 1
				else:
					term_count[word] = 1
	
	for term in term_count:
		print term, term_count[term]		
				

def main():
	tweet_file = sys.argv[1]
	frequency(tweet_file)


if __name__ == '__main__':
    main()
