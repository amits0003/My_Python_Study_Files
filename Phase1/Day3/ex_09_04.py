counts = {'a':1,'b':2,'c':2}
for key in counts:
# counts[key] =  (key in counts) + 1
#   counts[key] = (counts[key] * 1) + 1
    
    counts[key] = counts.get(key,0) + 1

print(counts)
