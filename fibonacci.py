def fibbonacci_series(start,end):
    fib_series=[]
    a,b = 0,1
    while a<=end:
        if a>=start:
            fib_series.append(a)
        a,b = b ,a+b
    return fib_series        


start_range = 10
end_range = 100
print(fibbonacci_series(start_range,end_range))