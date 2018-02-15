class Average:
	def __init__(self, ittearable):
		#validation

		# Get stats
		self.mean = Average.mean(ittearable)
		self.median = Average.median(ittearable)
		self.mode = Average.mode(ittearable)

	def __str__(self):
		return 'An object was created as an instance of the average class.\n\
		Now it can be used to calculate avarages.'

	def mean(ittearable):
		return sum(ittearable)/len(ittearable)

	def median(ittearable):
	    ittearable = sorted(ittearable)
	    length = len(ittearable)
	    midpoint = length//2
	    if length % 2 != 0:
	        return ittearable[midpoint]
	    if length % 2 == 0:
	        return (ittearable[midpoint] + ittearable[midpoint+1])/2
	    
	def mode(ittearable):
	    # make counter dictionary
	    counter = dict()
	    for key in ittearable:
	        counter[key] = counter.get(key,0) + 1
	    
	    # make a list of tuples with items and counter
	    commons = list()
	    for key, val in counter.items():
	        commons.append( (val, key) )
	    #Sort the list of tupules in desending order of values
	    commons.sort(reverse=True)
	    
	    # use the sorted list of key-count to find all modes
	    # returns a list of mode(s)
	    mod = []
	    for index, touple in enumerate(commons):
	        if len(mod) < 1:
	            mod.append(touple[1])
	        else:
	            if touple[0] == commons[index-1][0]:
	                mod.append(touple[1])
	            else:
	                break
	            
	    return mod

itr = [2,4,5,6,2,9,2,3,5,7,1,2,3,3]
new_ittr = Average(itr)
print(new_ittr)
print(new_ittr.mean)
print(new_ittr.median)
print(new_ittr.mode)

# Ways to improve
# How to use this class outside of this document
# validation
# __str__ method