"""
How to check if an array contains numbers
Problem is to search ( binary or sequential )
Search is O(Log N): Binary Search 
Sort and SEarch: Sequential search is O(n)
"""

def check_num():
    arry = ["X", "Y", 99, "P", 201, "Z"]
    val = None
    for n in arry:
        if type(n) is int:
            val = n
            break
    return val

number = check_num()
print(number)

"""
Q4. How to find the largest and smallest number in an unsorted array
solution: Sequenctial search is O(N)
solution: sort and then find min and max. O(N Log N), getting element from index is O(1)
"""

arr = [90,10002, 1,34,12, 908, 45,678,34,2, -1000]
def find_min_max(arr):
    min_bucket = arr[0]
    max_bucket = arr[0]
    for n in arr:
        if n < min_bucket:
            #replace with smaller number
            min_bucket = n 
        if n > max_bucket:
            #replace with larger number
            max_bucket = n 

    return (min_bucket, max_bucket)


def find_by_sorting(arr):
    arr.sort()
    end = len(arr) - 1
    min = arr[0]
    max = arr[end]
    return (min,max)


if __name__ == '__main__':
    res = find_min_max(arr)
    print(res)
    res = find_by_sorting(arr)
    print(res)
