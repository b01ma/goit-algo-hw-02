def check_brackets(s: str) -> str:
    stack = []
    
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for c in s:
        if c in "({[":
            stack.append(c)
        
        if c in ")}]":
            if not stack:
                return 'Not_symmetry' 
            if stack.pop() != pairs[c]:
                return 'Not_symmetry'
                    
    if stack:
        return 'Not_symmetry'
    
    return 'Symmetry'


print(check_brackets("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Симетрично
print(check_brackets("( 23 ( 2 - 3);"))             # Несиметрично
print(check_brackets("( 11 }"))                     # Несиметрично