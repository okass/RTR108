# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
avg = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    avg = avg + float(line[line.find(".") - 1:])
    count += 1

avg = avg / count
print("Average spam confidence:", avg)