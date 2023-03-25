import glob,random

curr = "/rdata/sifat/Unmask/ForPaper/DatatoFinetuneDetector/StyleCLIP/V1"
lines=[]

## real
paths1=glob.glob(curr + '/train/real/*.png')
for path in paths1:
  line=path+' 1\n'
  lines.append(line)

paths1_val = glob.glob(curr + '/val/real/*.png')
for path in paths1_val:
  line=path+' 1\n'
  lines.append(line)

## fake
paths2=glob.glob(curr + "/train/fake/*.png")
for path in paths2:
  line=path+' 0\n'
  lines.append(line)

paths2_val = glob.glob(curr + "/val/fake/*.png")
for path in paths2_val:
  line=path+' 0\n'
  lines.append(line)
  
f=open('list', 'w')
random.shuffle(lines)
for line in lines:
  f.write(line)
f.close()

## test
test_lines = []
paths3 = glob.glob(curr + "/test/real/*.png")
for path in paths3:
    line=path+' 1\n'
    test_lines.append(line)

paths3 = glob.glob(curr + "/test/fake/*.png")
for path in paths3:
    line=path+' 0\n'
    test_lines.append(line)

f=open('list_test', 'w')
random.shuffle(test_lines)
for line in test_lines:
  f.write(line)
f.close()

