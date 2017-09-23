#title
print("Driving Simulation")
print(" ")

# this is the formula for the calculated speed
def v(u,a,t):
    v = u + (a * t)
    return v

#this is the formula for the total distance travelled
def s(u,a,t):
    s = ((u * t) + ((a * t * t) /2))
    return s


u = 0   # u is the initial velocity
t = int(input("Time spent on the road = "))
a = int(input("Acceleration = "))
d = int(input("Distance = "))
sl = 60     # sl stand for Speed Limit
print(" ")

for i in range(0 , t+1):
    print ("Duration:", i, end="")  # the time is printed in range of 0 to time input + 1
    print (" Distance: " , "*" * int(s(u,a,i)/10))

speed = v(u,a,t)
distance_travelled = s(u,a,t)

print (" ")

if (speed>60):
    print("The person went over the speed limit. Safety first! (Maximum speed was" , v(u,a,t) , "m/s)")
else:
    print("The person went within the speed limit. (Maximum speed was" , v(u,a,t) , "m/s)")

if (distance_travelled >= d):
    print("The person arrived at the destination successfully. (Reached a total of", s(u,a,t), "m)")
else:
    print("The person wasn't able to reach the destination... (Reached a total of" , s(u,a,t) , "m)")
