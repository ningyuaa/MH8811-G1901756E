import json

#define the serialization function----------------------------------------
def ser(D):
    type_D = type(D)
    if type_D is list:
        res = "list|"
        for i in D:
            res = res + str(i)
            res = res + ','
            res = res + str(type(i))
            res = res + '|'
        return res[:-1]
    elif type_D is dict:
        res = "dict|"
        for i in D:
            res = res + str(i)
            res = res + ':'
            res = res + str(D[i])
            res = res + ','
            res = res + str(type(D[i]))
            res = res + '|'
        return res[:-1]
#define the deserialization function----------------------------------------
def des(s):
    lst_str = s.split('|')
    type_D = lst_str[0]
    lst_str = lst_str[1:]
    if type_D == 'list':
        res = list()
        for string in lst_str:
            item = string.split('',')
            V = item[0]
            V1 = item[1]

            if V1 == "<class 'int'>":
                res.append(int(V))
            elif V1 == "<class 'float'>":
                res.append(float(V))
            elif V1 == "<class 'str'>":
                res.append(V)
        return res
    elif type_D == 'dict':
        res = dict()
        for s in lst_str:
            ssplit = s.split(':')
            key = ssplit[0]
            item = ssplit[1]
            item = item.split(',')
            V = item[0]
            V1 = item[1]
            if V1 == "<class 'int'>":
                res[key] = int(V)
            elif V1 == "<class 'float'>":
                res[key] = float(V)
            elif V1 == "<class 'str'>":
                res[key] = V
        return res
#define dictionary comparison function------------------------------------
def com_d(d_1, d_2):
    if d_1 != {} and d_2 != {}: 
        for key in set(d_1) and set(d_2):
            if d_1[key] != d_2[key]:
                return False
            
            elif d_1 != d_2:
                return False

    elif d_1 == d_2:
            return True
    else:
            return False 
#def list comparison function---------------------------------------------
def com_l (d_1, d_2):
    if d_1 == d_2:
        return True
    else: 
        return False
#define comparison fuction------------------------------------------------
def com_c (d_1,d_2):
    if type (d_1) == type (d_2):
        if type (d_1) == type ([]):
            print (com_l(d_1, d_2))
        if type (d_1) == type ({}):
            print (com_d(d_1, d_2))
    else:
        print ('False')

file_1 = input('The path of file in json format:')
fn = file_1 +'.json'
data_1 = open(file_1)
data = json.load(data_1)
data_1.close()
print(data)
#Data structure to string to file------------------------------
s = ser(data)
fn1 = input ('The name of file in json format：')
ff = open (fn1, 'w')
ff.write(s)
ff.close()
#file to string------------------------------------------------
bb = open (fn)
str_file = bb.read()
bb.close()

der_data = des(str_file)

if com_c(data, der_data):
    print("Success")
else:
    print("Fail")
    