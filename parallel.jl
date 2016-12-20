using(Plots)

addprocs(Sys.CPU_CORES-1)

function f(n)
    gen = @spawn randn(n)
    ret::AbstractArray = fetch(gen)
    ret
end

f(1)
a = ones((10^3,10^3))
@time a = f((10^3,10^3))
@time f((10^3,10^3))


function g(n)
    ret = randn(n)
    ret
end

g(1)
@time g((10^3,10^3))


function j(n)
    av::Int = @parallel (+) for i=1:n
        nheads = @parallel (+) for i=1:n
            Int(rand(Bool))
        end
        #println(nheads)
    end
    av
    d = av / n
end

j(1)
@time j(10^4)


function k(n)
    av = 0
    for i in 1:n
