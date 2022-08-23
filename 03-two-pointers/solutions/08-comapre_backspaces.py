# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.


def backspaceCompare(s: str, t: str) -> bool:
    arr1 , arr2 = [] , []
    
    for i in s:
        if i == "#" and arr1:
            arr1.pop()
        elif i == "#":
            continue
        else:
            arr1.append(i)
            
    for i in t:
        if i == "#" and arr2:
            arr2.pop()
        elif i == "#":
            continue
        else:
            arr2.append(i)
    if arr1 == arr2: return True

    return False