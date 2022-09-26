import random
#Part A
weeks = 16
classes = 5
tuition = 6000
classes_per_week = 2

cost_per_week = ((tuition / classes) / weeks)

cost_per_class = (cost_per_week / classes_per_week)

print("Cost per week:", str(cost_per_week))

print("Cost per class:", str(cost_per_class))

#Part B
list = [1,2,3,4,5]
print("random choice: " + str(random.choice(list)))