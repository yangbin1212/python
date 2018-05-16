interviewer =['Nancy','lucy','Tony']
print(interviewer[0])
print(interviewer[1])
print(interviewer[2])
print(interviewer[0]+",can't arrive")
interviewer[0]='Fancy'
print(interviewer[0])
print(interviewer[1])
print(interviewer[2])
print('want more big')
interviewer.insert(0,'mike')
interviewer.insert(interviewer.__len__()//2,'Bob')
interviewer.append('Mary')
for x in interviewer:
	print('Welcome,'+x)

print("\njust two")
while interviewer.__len__()>2:
	print('sorry,'+interviewer.pop())
for x in interviewer:
	print('still in list,'+x)
del interviewer[1]
del interviewer[0]
if interviewer.__len__() ==0:
	print('totol empty')
