# /****************************************************************
#  *             CODERBYTE FIND INTERSECTION CHALLENGE            *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function FindIntersection(strArr) read the array of *
#  * strings stored in strArr which will contain 2 elements: the  *
#  * first element will represent a list of comma-separated       *
#  * numbers sorted in ascending order, the second element will   *
#  * represent a second list of comma-separated numbers           *
#  * (also sorted).                                               *
#  *                                                              *
#  * Your goal is to return a comma-separated string containing   *
#  * the numbers that occur in elements of strArr in sorted order.*
#  * If there is no intersection, return the string false.        *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: new string[] {"1, 3, 4, 7, 13", "1, 2, 4, 13, 15"}  *
#  * Output 1: 1,4,13                                             *
#  *                                                              *
#  * Input 2: new string[] {"1, 3, 9, 10, 17, 18", "1, 4, 9, 10"} *
#  * Output 2: 1,9,10                                             *
#  *                                                              *
#  ***************************************************************/

def findIntersection(arr):
    a1= set(arr[0])
    a2=set(arr[1])

    re=[]

    for i in a1:
        if i in a2:
            re.append(i)

    return ','.join(map(str,re))

arr=[ [1, 3, 4, 7, 13],[1, 2, 4, 13, 15]]
print(findIntersection(arr))

    