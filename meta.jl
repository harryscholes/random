n = 20
ex = :( x - 1 )

for i in 2:20
    ex = :( $ex * (x-$i))
end

ex

x = 100
eval(ex)

x = 10^5
eval(ex)
@elapsed




function f(n)
    x = 1
    for i in 1:n
        x += i
    end
    x
end

function g(n)
    x = 1.0
    for i in 1:n
        x += i
    end
    x
end

@code_warntype f()

@time f(10000)

@code_warntype f(10)


function f(n)
    s = 0
    for i = 1:n
        s *= (i/2)
    end
    s
end

@time f(1)

@time f(10^6)

@code_warntype f(1)

function f_improved(n)
    s = 0.0
    for i = 1:n
        s *= i/2
    end
    s
end

@time f_improved(1)

@time f_improved(10^6)

@code_warntype f_improved(1)
