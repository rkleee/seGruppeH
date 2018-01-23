import argparse
import matplotlib.pyplot as plt


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--f', help='the filename where the CKJM results are stored', default='result.txt')
    
    return parser.parse_args()
    
args = parseArgs()
measures = ['WMC','DIT','NOC','CBO','RFC','LCOM','Ca','NPM']

#read results
results=[[] for m in measures]
classes = []
with open(args.f,'r') as rf:
    for line in rf:
        tokens = line.split()
        classes.append(tokens[0])        
        for i,tok in enumerate(tokens[1:]):
            results[i].append(int(tok))

print(results)

plots = []
cp = 0

#calculate classes with highest and lowest values
for i,m in enumerate(measures[5]):
    zipped = zip(classes,results[i])
    zipped = sorted(zipped,key=lambda x: x[1])
    print (m,zipped[0:3],zipped[-3:])
    #plot histogram and save as pdf
    p1 = plt
    p1 = plt.hist(results[i], normed=True, bins=100)
    plots.append(p1)
    (plots[cp]).xlabel(m)
    (plots[cp]).savefig(m+'.pdf')
    cp+1
    #plt.clf()
    

        

