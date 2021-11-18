
def readfromfile(f):
    data = []
    try:
        file = open(f, 'r')
        text = file.readlines()
        for i in text:
            i = i.replace('\n','')
            data.append(i)
        file.close()
    except FileNotFoundError as fnfe:
        print(fnfe.args)
        print("File " + f + ' bestaat niet.')
    finally:
        return data
