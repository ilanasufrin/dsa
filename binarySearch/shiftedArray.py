"""
A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don't have a pre-shifted copy of it. 
For instance, the sequence 1,  2, 3, 4, 5 becomes 3, 4, 5, 1, 2 after shifting it twice to the left

Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr. 
If num isn't in shiftArr, return -1. 
Assume that the offset doesn't equal to 0 (i.e. assume the array is shifted at least once) or to arr.length - 1 (i.e. assume the shifted array isn't fully reversed).

# linear search => O(N)

# binary search to find shift point => O(logN) + O(logN)
# binary search TWICE to find num in two sub arrays (to the left and right of the shift point)
# = O(3logN)
# = O(logN)
"""

def shifted_arr_search(shiftArr, num):

  def driver(shiftArr, num):
    shiftPoint = find_shift_point(shiftArr, 0, len(shiftArr)-1)
    print('shift point ' + str(shiftPoint))

    if binary_search(shiftArr, num, 0, shiftPoint) != 0:
        return binary_search(shiftArr, num, 0, shiftPoint)
    if binary_search(shiftArr, num, shiftPoint, len(shiftArr)-1) != 0:
        return binary_search(shiftArr, num, shiftPoint, len(shiftArr)-1)
    else:
        return -1
    # return binary_search(shiftArr, num, shiftPoint, len(shiftArr)-1)
    # if num < shiftArr[0]:
    #     return binary_search(shiftArr, shiftPoint, shiftArr.length - 1, num)

    # return binary_search(shiftArr, 0, shiftPoint - 1, num)

  
  def binary_search(shiftArr, num, leftBound, rightBound):
    possibleIndex = leftBound + (rightBound - leftBound)/2
    # print(possibleIndex)
    if possibleIndex <= 0 or possibleIndex > len(shiftArr):
      return -1
    
    if shiftArr[possibleIndex] == num:
      return possibleIndex
    elif shiftArr[possibleIndex] > num:
      print('going left')
      return binary_search(shiftArr, num, leftBound, possibleIndex-1)
    else:
      print('going right')
      return binary_search(shiftArr, num, possibleIndex+1, rightBound)
    

  # def find_shift_point(shiftArray, leftBound, rightBound):
  #   possibleShiftPoint = leftBound + (rightBound - leftBound)/2
  #   print(possibleShiftPoint)

    
  #   if shiftArray[possibleShiftPoint-1] > shiftArray[possibleShiftPoint or possibleShiftPoint <= 0]:
  #     return possibleShiftPoint
  #   else:
  #     print('going left')
  #     return find_shift_point(shiftArray, 0, possibleShiftPoint-1)
  #     print('going right')
  #     return find_shift_point(shiftArray, possibleShiftPoint+1, len(shiftArray)-1)

  def find_shift_point(shiftArray, leftBound, rightBound):
    begin = 0
    end = len(shiftArray) - 1

    while (begin <= end):
        mid = begin + (end - begin)/2
        if (mid == 0 or shiftArray[mid] < shiftArray[mid-1]):
            return mid
        if (shiftArray[mid] > shiftArray[0]):
            begin = mid + 1
        else:
            end = mid - 1

    return 0


  # shiftPoint = find_shift_point(shiftArr, 0, len(shiftArr)-1)
  # bs = binary_search(shiftArr, num, 0, len(shiftArr)-1)
  # print(bs)
  a = driver(shiftArr, num)
  print(a)
  
  



shiftArr = [3, 4, 5, 1, 2]

shifted_arr_search(shiftArr, 2)