#dic
dict={"avi":100 ,"lior":200 ,"idan":350 ,"ori":450 ,"david":900}
print(dict)
a=(dict["avi"])
b=(dict["david"])
print("the sumery of avi and david: " + str(a+b))
dict.update({"avi and david":a+b})
print(dict)
print( "dffregfre: " + str(len(dict)))