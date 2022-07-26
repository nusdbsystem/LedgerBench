import sys

start, end = -1.0, -1.0

duration = float(sys.argv[2])
warmup = duration/3.0

tLatency = []
sLatency = []
fLatency = []

rLatency = []
wLatency = []
hLatency = []
vLatency = []

nkey = 0
nkeys = []

for line in open(sys.argv[1]):
  if line.startswith('#') or line.strip() == "":
    continue
  if line.startswith("verifynkeys"):
    nkey = float(line[12:-1])
    continue

  line = line.strip().split()
  if not line[0].isdigit() or len(line) < 6:
    continue

  if start == -1:
    start = float(line[2]) + warmup
    end = start + warmup

  fts = float(line[2])
  
  if fts < start:
    continue

  if fts > end:
    break

  latency = int(line[3])
  status = int(line[4])
  op = int(line[5])

  if op == 0:
    rLatency.append(latency)
  elif op == 1:
    wLatency.append(latency)
  elif op == 2:
    hLatency.append(latency)
  elif int(line[0]) > 0:
    nkeys.append(nkey)
    vLatency.append(latency)

  tLatency.append(latency) 

  if status == 0:
    sLatency.append(latency)
  else:
    fLatency.append(latency)

if len(tLatency) == 0:
  print "Zero completed transactions.."
  sys.exit()

outfile = open(sys.argv[3], "w")
outfile.write(str(len(sLatency)) + "\n")                                        
outfile.write(str(sum(sLatency)) + "\n")                                        
outfile.write(str(len(tLatency)) + "\n")                                        
outfile.write(str(sum(tLatency)) + "\n")
outfile.write(str(end - start) + "\n")
outfile.write(str(len(rLatency)) + "\n")
outfile.write(str(sum(rLatency)) + "\n")
outfile.write(str(len(wLatency)) + "\n")
outfile.write(str(sum(wLatency)) + "\n")
outfile.write(str(len(hLatency)) + "\n")
outfile.write(str(sum(hLatency)) + "\n")
outfile.write(str(len(vLatency)) + "\n")
outfile.write(str(sum(vLatency)) + "\n")
outfile.write(str(sum(nkeys)) + "\n")
