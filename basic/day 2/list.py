# list hocche python er ekti object jkhane chaile onkgulo item store kore rakha jay.
# index no: 0,1,2,3,4,5,..........

sub = ["c","c++","python","java"]

# how to access:
print(sub)

# list er jkono value print:
print(sub[2])

# jkono index theke shuru kore baki sob value print:
print(sub[1:])

# last value theke print:
print(sub[-1: :-1])

# new item add (last e add hobe)
sub.append("toc")
print(sub)

# new item add (jkono value r por)
sub.insert(1,"tv")
print(sub)

# item remove:
sub.remove("c")
print(sub)

# length ber kora:
print(len(sub))

# list e item sajano:
sub.sort() #choto theke boro
print(sub)

sub.reverse()
print(sub)

# sobgulo item remove:
sub.clear()
print(sub)

# list copy:
sub1= ["a","b"]
sub2= sub1.copy()
print(sub2)

# kono ekta item kotobar asey:
varrible = sub2.count("c")
print(varrible)