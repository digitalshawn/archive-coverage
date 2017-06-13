for i in /mnt/intersect/tweets/*.json.gz; do
  python getURIsInTweets.py $i >> "$i.out"
#  exit
done

sleep infinity
