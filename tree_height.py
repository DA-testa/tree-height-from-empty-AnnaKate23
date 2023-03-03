# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    list = [0]*n
    # k = [(i,1) for i in range(n) if parents[i] == -1]
    #masivs = numpy.zeros(n)
    #root = numpy.where(parents==-1)
    # arr = numpy.array(range(-1, n))

    for i in range(n):
        height = get_height(i, parents, list)
        if height>max_height:
            max_height = height
    return max_height


def get_height(node, parents, list):
    if list[node] !=0:
        return list[node]
    if parents[node] == -1:
        list[node] = 1
    else:
        return get_height(parents[node], parents, list) + 1
    
    

        
    # return max_height


def main():
    text = input()
    if "I" in text:
        n = int(input())
        parents = numpy.asarray(list(map(int, input().split())))
    elif "F" in text:
        file = input()
        if "a" in file:
            print("can't use 'a'")
            return
        with open(f"./test/{file}", "r") as filee:
            n = int(filee.readline())
            parents = numpy.asarray(list(map(int,filee.readline().split())))

    else:
        print("Invalid input")
        return
    
    max_height = compute_height(n, parents)

    
    print(max_height)
            
            



    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
