import sys,os,subprocess as v,json
s=sys.stdout
def p(l):
 s.write(l);s.flush()
t=sys.argv[1]
while 1:
 p("\n> ");c=raw_input().split();r=[];a=[]
 for q in c:
	r+=v.check_output("sed -n 's/\\(.\\{22\\}\\).*"+q+".*/\\1/p' "+t,shell=True).split(" \n")
 for m in r:
	if m not in a and r.count(m)==len(c):a+=m,
 p(json.dumps(a))
