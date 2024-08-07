import math

points = [(23, 45), (12, 78), (56, 89), (34, 23), (67, 12), (89, 67), (45, 34), (78, 90), (90, 56), (12, 34), (67, 89), (34, 56), (56, 78), (78, 12), (23, 67)]
distances = list()
def euclideanDistance(point1,point2):

    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

for i in range(len(points)):
    for j in range(i+1,len(points)):
        distances.append(euclideanDistance(points[i],points[j]))

print("Minimum Mesafe:", min(distances))
