from surt import surt
import moment
from dateutil.parser import parse

# http://bit.ly/tONigD	http://t.co/sthUkX13	Sun Jan 01 00:00:03 +0000 2012	153264184535158784

with open('/mnt/intersect/tweets/combined.out','r') as f:
  for line in f:
    fields = line.strip().split('\t')
    if len(fields) != 4: continue

    expandedURI = fields[0]
    uri = fields[1]
    datetime = fields[2]
    tweetId = fields[3]
 
    date14 =  parse(datetime).strftime('%Y%m%d%H%M%S')
    print '{0}\t{1}\t{2}'.format(expandedURI, date14, tweetId)
