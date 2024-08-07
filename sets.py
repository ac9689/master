thisset={"ashwani","ankit","tanvik",1,2}
print(thisset)
set1=set(("amr","john"))
print(set1)
htp=["ashwani",45,76,34,34]
print(htp)
for x in thisset:
    print(x)
print("ankit" in thisset)
thisset.add("orange")
print(thisset)
docs={"mts","jns",2,4}
thisset.update(docs)
print(thisset)
thisset.update(htp)
print(thisset)
thisset.remove("orange")
print(thisset)