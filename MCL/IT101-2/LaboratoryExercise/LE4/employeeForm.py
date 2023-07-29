def displayEmployee(empRecord):
    for k, v in empRecord.items():
        print("="*65)
        print('Employee NO:', k)
        for dk, dv in empRecord[k].items():
            print(dk + ': ' + dv)
        print("="*65)
        print()
        
def retrieveData(myFile):
    try:
        f = open(myFile, 'r')
        x = f.read()
        f.close
        return x
    except:
        print('File does not exist')
        
def addEmployee(empRecord, empId, fname, lname, dep, rph):
    empRecord[empId] = {
        'First name': fname,
        'Last name': lname,
        'Department': dep,
        'Rate per hour': rph
    }
    e = ";\n" + empId + ',' + fname + ',' + lname + ',' + dep + ',' + rph
    f = open('empList.txt', 'a')
    f.write(e)
    f.close()
    return empRecord

def getList():
    f = open('empList.txt','r')
    g = f.readlines()
    f.close()
    
    formattedData = []
    for i in g:
        splitUser = i.split(',')
        newUserDictionary = {}
        newUserDictionary['NO'] = splitUser[0]
        newUserDictionary['lastname'] = splitUser[1]
        newUserDictionary['firstname'] = splitUser[2]
        newUserDictionary['department'] = splitUser[3]
        newUserDictionary['rate'] = splitUser[4]
        formattedData.append(newUserDictionary['department'])
    return formattedData
