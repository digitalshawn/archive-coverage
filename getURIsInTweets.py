import json
import gzip
import sys

# Reads all files, supplied by args, breaks into py objs

def main():
  tweetGZs = sys.argv[1:]  
  tweets = []
  for gzs in tweetGZs:
    with gzip.open(gzs, 'r') as gz:
      rawJSON = gz.read()
      tweets = rawJSON.split('\n')

# [{u'indices': [42, 62], u'url': u'http://t.co/uogjb7YJ', u'expanded_url': u'http://bibliosol.wordpress.com', u'display_url': u'bibliosol.wordpress.com'}, {u'indices': [63, 83], u'url': u'http://t.co/uogjb7YJ', u'expanded_url': u'http://bibliosol.wordpress.com', u'display_url': u'bibliosol.wordpress.com'}]

  print "expandeduri,uri,createdAt"
  for tweetRaw in tweets:
    tweet = json.loads(tweetRaw)
    if 'entities' in tweet and 'urls' in tweet['entities']:
      for url in tweet['entities']['urls']:
        print "{0},{1},{2}".format(url['expanded_url'],url['url'],tweet['created_at'])


if __name__ == "__main__":
  main()


