#Program C2: Basic Descriptive Statistics
N=[9,41,12,3,74,15]
#---------------------------------------------------------------------------------
def my_min(N):
    smallest_so_far = None
    for the_num in N:
        if smallest_so_far is None:
            smallest_so_far = the_num
        elif the_num < smallest_so_far:
            smallest_so_far = the_num
    return smallest_so_far
#---------------------------------------------------------------------------------
def my_max(N):
    largest_so_far = None
    for the_num in N:
        if largest_so_far is None:
            largest_so_far = the_num
        elif the_num > largest_so_far:
            largest_so_far = the_num
    return largest_so_far
#----------------------------------------------------------------------------------
def my_average(N):
    total_num = 0
    for the_num in N:
        total_num = total_num + the_num
        aver_num = total_num/len(N)
    return aver_num
#----------------------------------------------------------------------------------
def my_median(N):
    N.sort()
    order = int(len(N)/2)
    if len(N)%2 == 1:
        med_num = N[order]
    elif len(N)%2 == 0:
        med_num = (N[order-1]+N[order])/2
    return med_num
#----------------------------------------------------------------------------------
def my_range(N):
    range = my_max(N)-my_min(N)
    return range

print (N)
print (my_min(N))
print (my_max(N))
print (my_median(N))
print (my_range(N))