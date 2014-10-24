import sys
import json
import string
import math

ratings = {} # initialize an empty ratings dictionary

def main():

    ratings_file = open(sys.argv[1])
    # user1 = str(sys.argv[2])
    # user2 = str(sys.argv[3])
    # item = str(sys.argv[4])
    # k = int(sys.argv[5])


    ratings = readRatings(ratings_file)
    print "readRatings output", ratings
    # sim = similarity(ratings[user1], ratings[user2])
    # print "sim = ", sim
    # nearest = nearestNeighbors(user1, ratings, k)
    # print "nearestNeighbors: ", nearest
    # prediction = predict(item, nearest, ratings)
    # print "prediction for item", item, ": ", prediction


def readRatings(ratings_file):
    
    # Write code to read ratings file and construct dictionary of dictionaries
    b={}
    # b.setdefault(key, [])
    for line in ratings_file:
        v=line.split("\t")
        ratings.setdefault(v[0],{})
        # b[v[2]]=v[1]
        ratings[v[0]][v[2]]=v[1]

    # print b
    return ratings

    
def similarity(user_ratings_1, user_ratings_2):

    # Write code to implement the Pearson correlation equation
    # Return the similarity of user 1 and user 2 based on tehir ratings
    
    return similarity


def nearestNeighbors(user_id, all_user_ratings, k):

    # Write code to determine the k nearest neighbors for user_id

    return nearest[0:k]


def predict(item, k_nearest_neighbors, all_user_ratings):
    
    # Write code to predict the rating for the item given the k nearest neighbors of the user

    return prediction



if __name__ == '__main__':
    main()
