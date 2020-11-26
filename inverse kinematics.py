import math;
#print("enter the  values of a,d")
import serial;
#ser=serial.Serial('COM3',baudrate=9600,timeout=1)
#file=ser.readlines()
a=[]
d=[]
theta=[]
file=open(r"C:\Users\siddu\Desktop\something.txt",'r')
for i in range(6):
    k1=file.readline().strip("\n").strip().split(" ")
    #print(k1)
    k=list(map(int,k1))
    a.append(k[0])
    d.append(k[1])
    theta.append(0)
#print("enter the co-ordinates of end effector...")
#px=float(input("enter the x co-ordinate of end-effector  "))
#py=float(input("enter the y co-ordinate of end-effector  "))
#pz=float(input("enter the z co-ordinate of end-effector  "))
k=list(map(float,file.readline().split(" ")))
px=k[0]
py=k[1]
pz=k[2]
file.close()
d2=d[1]
d3=d[2]
d4=d[3]
a1=a[0]
a2=a[1]
a3=a[2]
theta[1]=math.asin(pz/a2)
c2=math.cos(theta[1])
s2=math.sin(theta[1])
theta[0]=math.acos((px*(a2*c2+a1)-py*d3)/(px**2+py**2))
c1=math.cos(theta[0])
s1=math.sin(theta[0])
theta23=math.acos(((pz**2-a2**2+(px*c1+py*s1-a1)**2)/(2*pz**2))**0.5)
theta[2]=theta23-theta[1]
c3=math.cos(theta[2])
s3=math.sin(theta[2])
c23=math.cos(theta23)
s23=math.sin(theta23)
nx=math.sin(math.pi/2)
ny=math.cos(math.pi/2)
nz=math.cos(math.pi/2)
ox=math.cos(math.pi/2)
oy=math.sin(math.pi/2)
oz=math.cos(math.pi/2)
ax=math.cos(math.pi/2)
ay=math.cos(math.pi/2)
az=math.sin(math.pi/2)
theta[3]=math.atan((ax*s1-ay*c1)/(ax*c1*c23+ay*s1*s23+az*s23))
c4=math.cos(theta[3])
s4=math.sin(theta[3])
theta[4]=math.atan((ax*c1*c23*c4+ay*s1*s23*c4+a2*s23*c4+a2*s1*s4-ay*c1*s4)/(-az*s23-ay*s1*s23+az*c23))
c5=math.cos(theta[4])
s5=math.sin(theta[4])
theta[5]=math.atan((oz*c23-ox*c1*s23-oy*s1*s23)/(nx*c1*s23+ny*s1*s23-nz*c23))
print(theta)
