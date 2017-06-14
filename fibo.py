def fibo2(N):
	if N == 0 or N == 1:
		return N
	if N > 1:
		return fibo(N-1) + fibo(N-2)
	if N < 0:
		return fibo(N+2) - fibo(N+1)

if __name__=="__main__":
	print("fibo(5)", fibo(5))

def fibo(N):
	a = 0
	b = 1
	for i in range(N):
		bnew = a + b
		a = b
		b = bnew
	return b
