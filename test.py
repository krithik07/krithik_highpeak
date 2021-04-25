sample_input = open('sample_input.txt','r')



sample_output = open('sample_output.txt','a')

goodies={}
output_list=[]



for f in sample_input:
    index_toRead_price=f.index(":")
    print(f[index_toRead_price+1:].strip())
    print(f[:index_toRead_price])
    goodies[f[:index_toRead_price]]=f[index_toRead_price+1:].strip()
print(goodies)




prices=[int(i) for i in list(goodies.values())]



prices.sort(reverse=True)
print(prices)



employees=int(input("Number of the employees: "))
print("employees",employees)

length_considered=(len(prices)- employees)

print(length_considered)

for i in range(length_considered):
    maxprice=prices[i]
    minprice=prices[employees+i]
    if i == 0:
        difference=maxprice-minprice
        choosen_index=i
    elif (maxprice-minprice)<difference:
        difference=maxprice-minprice
        choosen_index=i


c_price=prices[choosen_index:employees+choosen_index]

difference=max(c_price)-min(c_price)
print("difference",difference)



count=0

for key,value in goodies.items():
    prices[count]
    print(value)
    if int(value) in c_price and count < employees:
        str1=key+": "+value


        output_list.append(str1)
        count+=1
        print(str1)

sample_output.write("Number of employees: "+str(employees))
sample_output.write("\n\n")


sample_output.write("Here the goodies that are selected for distribution are: ")

sample_output.write("\n")

for i in output_list:
    sample_output.write(i)
    sample_output.write("\n")
sample_output.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(difference))
sample_output.write("\n\n\n")


sample_input.close()
sample_output.close()
