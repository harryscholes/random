a = 1
a *3

b = a*3+5

using PyPlot

plot([1:10;], [31:40;])

using Plots
pyplot() # Choose a backend
plotlyjs()
plot(rand(4,4)) # This will plot to the plot pane
plot(randn(10^3,4))
histogram(randn(10^3,4))
scatter(Normal(3,5))

using BenchmarkTools

function f(n)
       nheads = @parallel (+) for i=1:n
                rand(Bool)
              end
       end


@benchmark f(100000000)

@benchmark f(100000000)


nprocs()

@benchmark nheads = @parallel (+) for i=1:100000000
  rand(Bool)
end


function g(n)
    nheads = @parallel (+) for i=1:n
        Int(rand(Bool))
    end
end


@benchmark g(100000000)

@benchmark g(100000000)

@benchmark g(100000000)


a::Int64 = 1
b = 1.1
typeof(a)
typeof(b)

a + b ::Int

a+b::Any
a+b::Float64


function newf(x)::Int
    x
end


newf(1.1)
newf(1)


function newf(x)::Number
    x::Int
    #x
end

x = newf(1)


using Gadfly

plot(rand(10,10))


z = 1

function f{x<:Number}(x::Int64, y::Float64)
        x + y + z
end

f(1, 1.1)



f(x::Number, y::Number) = "Num"
f(1,2)
f(x::Int, y::Number) = "Int"
f(1,2)
f(x::Int, y::Float64) = "Int + Float"
f(1.1,1.1)
f(1,1.1)
f{z<:Float64}(x::Int, y::z) = "Static Int + Float"
f(1,1.1::z)
f{z<:Int64}(x::Int, y::z) = "Static Int + Float"
f(1,1.1::z)
