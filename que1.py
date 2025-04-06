def interleaved(filename):
    with open (filename,'r') as inputfile:
        file_name=inputfile.read().split()
        
        s1, s2=file_name[0],file_name[1]
        interleaved=''.join(a+b for a,b in zip(s1,s2))
        interleaved+=s1[len(s2):]
        interleaved+=s2[len(s1):]
        return interleaved

result=interleaved('file.txt')
print(result)