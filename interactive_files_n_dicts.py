f = open("scores.txt")
user_input = raw_input("Type a restaurant name or a rating:")

scores = {}
for line in f: 
    temp = line.split(":")
    key = temp[0]
    val = temp[1].strip()
    scores[key] = val

restaurants = sorted(scores.keys())

def get_rating(restaurant):
    if restaurant in restaurants:
        print "Restaurant %s is rated %s."  % (restaurant, scores[restaurant])

def same_rating(number):
    print "The following restaurants have a rating of %s:" % number
    for key,val in scores.iteritems():
        if val == number:
            print key



if user_input.isdigit():
    same_rating(user_input)
elif user_input in restaurants:
    get_rating(user_input)
else:
    print "I do not understand. Please, enter restaurant name or rating:"
    user_input = raw_input()


f.close()

