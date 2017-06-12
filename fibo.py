def fibo(N):
	if N == 0 or N == 1:
		return N
	if N > 1:
		return fibo(N-1) + fibo(N-2)
	if N < 0:
		return fibo(N+2) - fibo(N+1)

if __name__=="__main__":
	print("fibo(5)", fibo(5))