s1={1,2,3,4,5}
s2={4,5,6,7,8}

# union method
union=s1.union(s2)
print(union)
# output:- {1, 2, 3, 4, 5, 6, 7, 8} union method se dono set ke unique elements ka set milega

intersection=s1.intersection(s2)
print(intersection)
# output:- {4, 5} intersection method se dono set ke common elements ka set milega

# difference method
difference=s1.difference(s2)
print(difference)
# output:- {1, 2, 3} difference method se s1 ke s2 se alag elements ka set milega

difference2=s2.difference(s1)
print(difference2)
# output:- {6, 7, 8} difference method se s2 ke s1 se alag elements ka set milega

symmetric_difference=s1.symmetric_difference(s2)
print(symmetric_difference)
# output:- {1, 2, 3, 6, 7, 8} symmetric_difference method se dono set ke unique elements ka set milega jo common nhi hai

# shortcuts

a={1,2,3,4,5}
b={4,5,6,7,8}

union1=a|b
print(union1)
# output:- {1, 2, 3, 4, 5, 6, 7, 8} union method ka shortcut

intersection1=a&b
print(intersection1)
# output:- {4, 5} intersection method ka shortcut

difference1=a-b
print(difference1)
# output:- {1, 2, 3} difference method ka shortcut

symmetric_difference1=a^b
print(symmetric_difference1)
# output:- {1, 2, 3, 6, 7, 8} symmetric_difference method ka shortcut