'''
Created on Mar 9, 2018

@author: ncarlson
'''
import pygame
import math

def pacman(center,start,stop):
    '''center, start and stop must be tuples with x and y'''
    radius = distance(start,center)
    results = []
    while start[0]!=stop[0] and start[1]!=stop[1]:        
        p = {}
        mults = getQuadrantMultiplier(center, start)
        p[1] = (start[0]+mults[0],start[1])
        p[2] = (start[0]+mults[0],start[1]+mults[1])
        p[3] = (start[0],start[1]+mults[1])
        d = []
        d.append((1,distance(p[1],center)))
        d.append((2,distance(p[2],center)))
        d.append((3,distance(p[3],center)))
        point = 1
        temp = 100.0
        for dist in d:
            if abs(dist[1]-radius)<temp:
                point = dist[0]
                temp = dist[1]
        results.append(p[point])
        start = p[point]
        print(start)
    return results
        

def getQuadrantMultiplier(center,point):
    if point[0]<=center[0]:
        #2 and 3
        if point[1]<=center[1]:
            #2
            return ((1,-1))
        else:
            #3
            return ((-1,-1))
    elif point[0]>center[0]:
        #1 or 4
        if point[1]<=center[1]:
            #1
            return ((1, 1))
        else:
            #4
            return ((-1,1))
        
    
def distance(loc1,loc2):
    d = math.sqrt(
        math.pow(loc1[0]-loc2[0],2) 
        + 
        math.pow(loc1[1]-loc2[1],2)
        )
    return d

if __name__=="__main__":
    center = (20,20)
    start = (23,20)
    stop = (20,23)
    print(pacman(center,start,stop))
    #print(getQuadrantMultiplier((20,20), (55,22)))
