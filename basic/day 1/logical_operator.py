#logical operator

# and = jodi ekti condition mittha hoy, tahole pura condition mittha
# or = jkono ekti condition sotto holei, puro condition sotto

name = "Mikasa"
age = 23

name_matched = name == "Mikasa"
age_matched = age == age>23

print(name_matched and age_matched)
print(name_matched or age_matched)


#           condition1      condition2      AND     OR
#              true            true         true    true
#              true            false        false   true
#              false           true         false   true
#              false           false        false   false