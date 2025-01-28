# add()	 	Adds an element to the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns whether another set contains this set or not

# issubset()	<=	Returns whether another set contains this set or not
# Верните True, если все элементы набора yприсутствуют в наборе x:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# remove()	 	Removes the specified element
# remove()	 	Removes the specified element
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others