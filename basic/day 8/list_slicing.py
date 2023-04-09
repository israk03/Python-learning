"""                     [1,2,3,4,5]
                        [2,3,4]

                        [start_index_no : end_index_no : step]
"""

a =[12,13,4,"alu","peyaz",[2,"pizza"]]

print(a[::])            # same list print korbe

print(a[1: :])          # index 1 theke print korbe

print(a[1: :3])         # 2 ta kore value skip korbe, 3 er jaygay 4 dile 3 ta korto

print(a[ : :-1])        # reverse the list

print(a[0:4:1])         # list k slice korche
print(a[-1:-3:-1])      # list k slice korche
