import sys,os,subprocess as v,json
s=sys.stdout
def p(l):s.write(l);s.flush()
t=sys.argv[1]
while 1:
 p("\n> ");c=raw_input().split();r=[];a=[]
 for q in c:
	r+=v.check_output("grep '.\\{22\\}.*"+q+".*' "+t,shell=True).split("\n")[:-1]
 for m in r:
	d=m[:21]
	if d not in a and r.count(m)==len(c):a+=d,
 p(json.dumps(a))
