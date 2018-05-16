
motor=['bieke','aodi','dazhong','benci','baoma']
print(motor)
motor[0]='jili'
print(motor)
motor.append('tesila')
print(motor)
motors=[]
motors.append('yiqdazhong')
motors.append('guangqifengtian')
motors.append('dongfengrichan')
print(motors)
motors.insert(0,'zhejiangjili')
print(motors)
del motors[0]
print(motors)
del motors[0]  #delete
print(motors)
del motors[0]
print(motors)


motors1=['a','b','c','d','e']
popped_motors1=motors1.pop()
print(motors1)
print(popped_motors1)
print(motors1.pop(0))
print(motors1.pop(0))
print(motors1.pop(0))

motors2=['a','b','c','d','e']
motors2.remove('a')
motors2.remove(motors2[-1])
print(motors2)
