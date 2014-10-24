import sys
import json
import string
import math

ratings = {} # initialize an empty ratings dictionary

def avg(value_dic):
    num=len(value_dic)
    total=0
    for k in value_dic:
        total+=value_dic.get(k)
    return total/num


def main():

    ratings_file = open(sys.argv[1])
    user1 = str(sys.argv[2])
    user2 = str(sys.argv[3])
    # item = str(sys.argv[4])
    # k = int(sys.argv[5])


    ratings = readRatings(ratings_file)
    print "readRatings output", ratings
    sim = similarity(ratings[user1], ratings[user2])
    print "sim = ", sim
    # nearest = nearestNeighbors(user1, ratings, k)
    # print "nearestNeighbors: ", nearest
    # prediction = predict(item, nearest, ratings)
    # print "prediction for item", item, ": ", prediction


def readRatings(ratings_file):
    
    # Write code to read ratings file and construct dictionary of dictionaries
    for line in ratings_file:
        v=line.split("\t")
        #initiate sub-dictionary
        ratings.setdefault(str(v[0]),{})
        ratings[str(v[0])][str(v[2])]=float(v[1])

    return ratings

    
def similarity(user_ratings_1, user_ratings_2):

    # Write code to implement the Pearson correlation equation
    # Return the similarity of user 1 and user 2 based on tehir ratings
    delta=[]
    a_delta2=[]
    b_delta2=[]
    num_up=0
    num_down=0
    avg_user_1=avg(user_ratings_1)
    avg_user_2=avg(user_ratings_2)
    print avg_user_1
    print avg_user_2
    #get the delta in the same items these two users rated
    for key in user_ratings_1:
        for k in user_ratings_2:
            if key==k:
                print key
                temp1=user_ratings_1.get(key)-avg_user_1
                temp2=user_ratings_2.get(key)-avg_user_2
                delta.append((temp1,temp2))
                a_delta2.append(temp1**2)
                b_delta2.append(temp2**2)
    print delta,"d"
    for v in delta:
        num_up+=v[0]*v[1]
    a_down=0
    b_down=0
    for v in a_delta2:
        a_down+=v
    for v in b_delta2:
        b_down+=v
    num_down=a_down*b_down
    print num_up,num_down

    similarity=num_up/(math.sqrt(num_down))
    return similarity


def nearestNeighbors(user_id, all_user_ratings, k):

    # Write code to determine the k nearest neighbors for user_id

    return nearest[0:k]


def predict(item, k_nearest_neighbors, all_user_ratings):
    
    # Write code to predict the rating for the item given the k nearest neighbors of the user

    return prediction



if __name__ == '__main__':
    main()
