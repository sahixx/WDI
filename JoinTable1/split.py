with open("/Users/danielkhan/Downloads/offers_english.json","r") as f:
	lines=f.readlines()

n = len(lines)
partitions = [8225748, 16451499]
count=0
curr_partition = partitions[count]
arr=[]
for i,line in enumerate(lines):
	
	if i>curr_partition:
		f=open("partition"+str(count)+".json", "a")
		for i in range(len(arr)):
			f.write(arr[i])
		f.close()
		count=count+1
		curr_partition=partitions[count]
		arr=[]

	arr.append(line)

f=open("partition"+str(count)+".json", "a")
for i in range(len(arr)):
	f.write(arr[i])
f.close()
	
