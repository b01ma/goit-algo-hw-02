from collections import deque

'''
    d.append(x) – додає праворуч
    d.appendleft(x) – додає ліворуч
    
    d.pop() – видаляє та повертає останній елемент
    d.popleft() – видаляє та повертає перший елемент
    
    len(d) – кількість елементів у черзі
    d.clear() – очищає чергу
    d[0] – перший елемент (як у списку)
    d[-1] – останній елемент    
'''



def is_palindrome(s: str) -> bool:
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    d = deque()
    
    for c in s:
        d.append(c)
    
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
        
    return True

print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("racecar"))                      # True
print(is_palindrome("palindrome"))                   # False


    

    