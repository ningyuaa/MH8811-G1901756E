#----------------------------------------------------------------------------------
def my_min(fname):
    smallest_so_far = None
    for the_num in fname:
        if smallest_so_far is None:
            smallest_so_far = the_num
        elif the_num < smallest_so_far:
            smallest_so_far = the_num
    return smallest_so_far
#---------------------------------------------------------------------------------
def my_max(fname):
    largest_so_far = None
    for the_num in fname:
        if largest_so_far is None:
            largest_so_far = the_num
        elif the_num > largest_so_far:
            largest_so_far = the_num
    return largest_so_far
#----------------------------------------------------------------------------------
def my_average(fname):
    total_num = 0
    for the_num in fname:
        total_num = total_num + the_num
        aver_num = total_num/len(fname)
    return aver_num
#----------------------------------------------------------------------------------
def my_median(fname):
    fname.sort()
    order = int(len(fname)/2)
    if len(fname)%2 == 1:
        med_num = fname[order]
    elif len(fname)%2 == 0:
        med_num = (fname[order-1]+fname[order])/2
    return med_num
#----------------------------------------------------------------------------------
def my_range(fname):
    range = my_max(fname)-my_min(fname)
    return range
#Read the file---------------------------------------------------------------------
def getfilelines (fname):
    fh=open(fname)
    lines=[]
    for line in fh:
        line = line.rstrip()
        if line:
            line= float(line)
            lines.append(line)
    fh.close()
    return lines
data = getfilelines('forpy.csv')
#------------------------------------------------------------------------------------
def Sample_Var (data):
    n = sum1 = sum2 = 0
    
    for x in data:
        n += 1
        sum1 += x
    mean = sum1/n

    for x in data:
        sum2 += (x-mean)*(x-mean)

    var = sum2/ (n-1)
    return var
    
print ('Min number is',my_min(data))
print ('Max number is',my_max(data))
print ('Median is',my_median(data))
print ('Range is', my_range(data))
print ('Sample variance is', Sample_Var(data))