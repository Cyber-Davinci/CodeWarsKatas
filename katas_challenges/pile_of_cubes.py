
def find_nb(m):
	total,n = 0,0
	# increment n and total as long as total is less than m
	while total < m:
		n+=1
		total+=n**3

	# return number of cubes if m = total else return -1
	return n if m==total else -1
print(find_nb(3154))