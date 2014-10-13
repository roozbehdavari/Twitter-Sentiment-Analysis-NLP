import sys
import json

def top_ten(tweets_file):

	hashtag_count = {}

	alltweets = open(tweets_file,'r')      # Opening the file that contains the tweets
	tweetsJson = alltweets.readlines()
	alltweets.close()

	for tweet in tweetsJson:
		if 'text' in json.loads(tweet).keys():	
			hashtags = json.loads(tweet)[u'entities'][u'hashtags']
			for hashtag in 	hashtags:
				hashtag_text = hashtag[u'text']			
				if hashtag_text in hashtag_count.keys():
					hashtag_count[hashtag_text] += 1
				else:
					hashtag_count[hashtag_text] = 1
	
	
	top_ten_raw = sorted(hashtag_count, key=hashtag_count.get, reverse=True)[:10]
	for each in top_ten_raw:
		print each, hashtag_count[each]
			

def main():
	tweet_file = sys.argv[1]
	top_ten(tweet_file)


if __name__ == '__main__':
    main()
