f = open("scores.txt")

scores = {}
for line in f: 
    temp = line.split(":")
    key = temp[0]
    val = temp[1].strip()
    scores[key] = val

restaurants = sorted(scores)

for item in restaurants:
    print "Restaurant '%s' is rated at %s." % (item, scores[item]) 




f.close()
