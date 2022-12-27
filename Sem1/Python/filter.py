# filter method filters the given sequence with ht ehelp of function (user-defines,anonymous)
# --each element in the sequence which is true or not
l=[5,13,25,26,34,48,55,69,78,39,91]
# filter(function,sequence)
fl=filter(lambda x: x%13==0,l)
nl=list(fl)
print(nl)
