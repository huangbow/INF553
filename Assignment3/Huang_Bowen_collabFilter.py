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
    item = str(sys.argv[4])
    k = int(sys.argv[5])


    ratings = readRatings(ratings_file)
    print "readRatings output", ratings
    sim = similarity(ratings[user1], ratings[user2])
    print "sim = ", sim
    nearest = nearestNeighbors(user1, ratings, k)
    print "nearestNeighbors: ", nearest
    prediction = predict(item, nearest, ratings)
    print "prediction for item", item, ": ", prediction


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
    sim_count=0
    delta=[]
    a_delta2=[]
    b_delta2=[]
    num_up=0
    num_down=0
    avg_user_1=avg(user_ratings_1)
    avg_user_2=avg(user_ratings_2)
    #get the delta in the same items these two users rated
    for key in user_ratings_1:
        for k in user_ratings_2:
            if key==k:
                sim_count+=1
                temp1=user_ratings_1.get(key)-avg_user_1
                temp2=user_ratings_2.get(key)-avg_user_2
                delta.append((temp1,temp2))
                a_delta2.append(temp1**2)
                b_delta2.append(temp2**2)
    #if no co-items
    if sim_count==0:
        return 0.0


    for v in delta:
        num_up+=v[0]*v[1]
    a_down=0
    b_down=0
    for v in a_delta2:
        a_down+=v
    for v in b_delta2:
        b_down+=v
    num_down=a_down*b_down

    similarity=num_up/(math.sqrt(num_down))
    return similarity


def nearestNeighbors(user_id, all_user_ratings, k):

    # Write code to determine the k nearest neighbors for user_id
    nearest=[]
    for key in all_user_ratings:
        if key!=user_id:
            nearest.append((key,similarity(ratings[user_id],ratings[key])))
    nearest=sorted(nearest,key=lambda x:(x[1],x[0]),reverse=True)

    return nearest[0:k]


def predict(item, k_nearest_neighbors, all_user_ratings):
    
    # Write code to predict the rating for the item given the k nearest neighbors of the user
    total_sim=0
    total_up=0
    k_nearest_neighbors_temp=k_nearest_neighbors
    for u in k_nearest_neighbors:
        if all_user_ratings[u[0]].get(item+'\n')!=None:
            total_sim+=u[1]
            total_up+=u[1]*all_user_ratings[u[0]].get(item+'\n')

    prediction=total_up/total_sim
    

    return prediction



if __name__ == '__main__':
    main()
