"""
Collatz conjecture function
.
.
.
The Collatz conjecture is an example of a simple
computational process whose behavior is so unpredictable
that the world's best mathematicians still don't understand it.

Consider the simple function f(n)f(n) (as defined in the
Wikipedia page above) that takes an integer nn and divides

it by two if nn is even and multiplies nn by 33 and then adds
one to the result if nn is odd. The conjecture involves studying
the value of expressions of the form f(f(f(...f(f(n)))))f(f(f(...f(f(n)))))
as the number of calls to the function ff increases. The conjecture is that,
for any non-negative integer nn, repeated application of ff to nn yields
a sequence of integers that always includes 11.

"""



def f(n):
    if n%2 == 0:
        number = n/2
        return(int(number))
    else:
        number = (n*3)+1
        return(int(number))
    
    
print(f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071)))))))))))))))
print(f(f(f(f(f(f(f(674))))))))     
