# using the numbers 1-9 inclusive, make:
# _ _ _ _ * 3 = _ _ _ _ _

# n = map(str, range(1,10))
#
# for i in range(1234,9877):
#     j = i * 3
#     i, j = str(i), str(j)
#     if set(i+j) == set(n): print i, j


#n=map(str,range(1,10))



# for i in range(9877):
#  j=i*3;i,j=`i`,`j`
#  if set(i+j)==n:print i,j


# for i in range(9877):
#  j=i*3
#  if set(`i`+`j`)==n:print i,j

# n=set('123456789');x=[i for i in range(9877)if set(`i`+str(i*3))==n];print[(i,i*3)for i in x]

#n=set('123456789');print[(j,j*3)for j in[i for i in range(9877)if set(`i`+`i*3`))==n]]

#print [(i,i*3)for i in range(9877)if set(`i`+`i*3`)==set('123456789')]

print [(i,i*3)for i in range(9877)if set(`i`+`i*3`)==set(`5**18`)]


[(i,i*3)for i in range(9877)if set(`i`+`i*3`)==set(`5**18`)]


for i in range(9877):
 if set(`i`+`i*3`)==set(`5**18`):print i,i*3


i=1
while len(`i`)<5:
 if set(`i`+`i*3`)==set(`5**18`):print i,i*3
 i+=1


i=1
while i<9877:
 set(`i`+`i*3`)==set(`5**18`):print i,i*3
 i+=1




function f(x)
    #return [a for a in x if Set(vcat(digits(a[1]),digits(a[2])))==y]
    x = [(i, i*3) for i in 1:9876]
    y = Set([j for j in 1:10])
    filter(a-> Set(union(digits(a[1]),digits(a[2])))==y, x)
    #[i for i in x if union(digits(i[1]),digits(i[2]))==y]
    #l = Set(vcat(digits(i[1]),digits(i[2])))
end


x = collect(1:9876)
y = collect(1:9)
z = filter(i -> Set(vcat(digits(i),digits(i*3))) == Set(y), x)

[(i,i*3)for i in filter(i->Set(vcat(digits(i),digits(i*3)))==Set(collect(1:9)),collect(1:9876))]

[(i,i*3)for i in filter(i->Set(∪(digits(i),digits(i*3)))==Set(collect(1:9)),collect(1:9876))]

[(i,i*3)for i in filter(i->Set(∪(digits(i),digits(i*3)))==Set([1:9;]),[1:9876;])]

[[i,i*3]for i in filter(i->Set(mapreduce(digits,∪,[i,i*3]))==Set([1:9;]),[1:9876;])]
