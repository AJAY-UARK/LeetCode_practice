'''
NOTES:

1.  Ask clarifying questions, don't just assume, especially definitions.

2.  If you have to store values from a list/array in a stack, and if values have duplicates, 
    you can just store their indices instead of the values, and reference the index when needed, only works in some cases.

3.  It's ok to do multiple O(n) passes over iterables, if it makes the code simpler and easier to understand, 
    you don't always have to do everything in a single pass, look at 143 (Duplicate) for inspiration.

4.  For LinkedList problems, using a dummy node simplifies the edge cases, 
    such as when the head node needs to be removed, inspiration from 19.

5.  If you're in a Google style interview, where you dry run your code, 
    think of edge cases, like empty inputs, single element inputs, odd/even length inputs, etc.

6.  Definition of a balanced tree is, for all nodes, the difference between depth of left subtree and right subtree 
    is less than or equal to 1 level. It's NOT height of the tree is equal to least possible height for given number of nodes, 
    IT'S NOT the same, inspiration from 543!!

7. When using heapq with custom classes/objects, use a tuple of the form to be stored (key, unique_id, object),
    - heapq does not support a custom comparator or key function.
    - It compares tuple elements in order.
    - First, it compares `key`.
    - If keys are equal, it compares `unique_id`.
    - Without a unique_id, Python would attempt to compare the objects
    themselves, which raises a TypeError since class instances cannot be compared by default.
    - Inspiration from 23

8.  In some problems, a pointer-based solution is optimal (O(1) space), but it can be
    time-consuming to implement, explain, and dry-run during interviews.
    If an alternative approach exists using extra space (e.g., stack or list) that is simpler and faster to implement, 
    it's often reasonable to choose it and explicitly tell the interviewer:

    - The problem can be solved in O(1) space using pointers.
    - However, the pointer approach is harder to implement and review under time constraints.
    - For clarity and speed, I'm choosing a solution that uses extra space.

    This is especially important in interviews where:
    - Pointer manipulation is hard to visualize
    - You must dry-run your code, and explain pointer transitions, which consumes significant time

    That said, if the pointer logic is simple or strictly required, it may be worth taking the risk.
    Inspiration from 25

9.  Some problems are only possible to be solved using BFS, keep that in mind and don't always jump to DFS, 
    analyze and visualize before you write code, don't take too much time though. Inspiration from 994
'''
from typing import List
import math

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashTable = []
        val = False
        for i in nums:
            if i in hashTable:
                val = True
            else:
                hashTable.append(i)
        return val
    
    def isAnagram(self, s: str, t: str) -> bool:
        l = {}
        r = {}
        result = False
        for i in range(len(s)):
            if len(s) != len(t):
                result = False
                break
            if s[i] in l:
                val = l[s[i]]
                l[s[i]] = val + 1
            else:
                l[s[i]] = 1
            if t[i] in r:
                val = r[t[i]]
                r[t[i]] = val + 1
            else:
                r[t[i]]= 1
        if l == r and len(s) == len(t):
            result = True
        return result
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hashTable:
                return [hashTable[val], i]
                break
            hashTable[nums[i]] = i
        return []
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = {}
        for string in strs:
            h1 = {}
            for i in range(len(string)):
                if string[i] in h1:
                    val = h1[string[i]]
                    h1[string[i]] = val + 1
                else:
                    h1[string[i]] = 1

            key = tuple(sorted(h1.items()))
            if key in hashTable:
                hashTable[key].append(string)
            else:
                hashTable[key] = [string]
        
        ans = list(hashTable.values())

        return ans
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h1 = {}
        for i in range(len(nums)):
            if nums[i] in h1:
                h1[nums[i]] += 1
            else:
                h1[nums[i]] = 1
        
        freq = [[] for _ in range(len(nums)+1)]

        for n, c in h1.items():
            freq[c].append(n)
        
        ans = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
                
    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            count = len(s)
            string += f"{count}#{s}"
        return string

    def decode(self, s: str) -> List[str]:
        ans = []
        count = 0
        while count < len(s):
            count2 = count
            while s[count2] != "#":
                count2 += 1
            length = int(s[count:count2])
            string = s[count2 + 1 : count2 + 1 + length]
            ans.append(string)
            count = count2 + 1 + length
        return ans
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left2right = []
        right2left = []
        product = 1

        for i in range(len(nums)):
            if i > 0:
                product *= nums[i-1]
            left2right.append(product)
        
        product = 1
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums)-1:
                product *= nums[i+1]
            right2left.append(product)
        
        right2left = right2left[::-1]
        res = [a*b for a,b in zip(left2right, right2left)]
        
        return res

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        square = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in column[j] or
                    board[i][j] in rows[i] or 
                    board[i][j] in square[((i//3)*3+j//3)]):
                    return False
                column[j].add(board[i][j])
                rows[i].add(board[i][j])
                square[((i//3)*3+j//3)].add(board[i][j])
        return True
    
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(numbers)):
            difference = target - numbers[i]

            if numbers[i] in hashTable:
                return [hashTable[numbers[i]]+1, i+1]
            
            hashTable[difference] = i
        return []
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-1):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) -1
            while j < k:
                # target = -nums[i]
                if -nums[i] < (nums[j] + nums[k]):
                    k -= 1
                elif -nums[i] > (nums[j] + nums[k]):
                    j += 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                    k -= 1

        return ans
    
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2:
            return 0
        l, r = 0, len(heights)-1
        max_area = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            if max_area < area:
                max_area = area
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_area
    
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right  = len(nums)-1
        
        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target: return middle
            if nums[middle] < target: left = middle + 1
            if nums[middle] > target: right = middle -1
            
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        top = 0
        bottom = rows - 1
        while top <= bottom:
            middle = (top + bottom)//2
            if matrix[middle][0] > target:
                bottom = middle - 1
            elif matrix[middle][columns-1] < target:
                top = middle + 1
            else: 
                break
        if top > bottom: return False
        left = 0
        right = columns - 1
        while left <= right:
            half = (left + right) // 2
            if target == matrix[middle][half]:
                return True
            elif target > matrix[middle][half]:
                left = half + 1
            else:
                right = half - 1
            
        return False
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            k = (left + right) // 2
            hours = 0
            for pile in piles:
                ceil = math.ceil(pile / k)
                hours += ceil
            if hours <= h:
                ans = min(ans, k)
                right = k - 1
            else:
                left = k + 1
        return ans

    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        ans = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break
            mid = (l + r) // 2
            ans = min(ans, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:# elif nums[mid] < nums[r]:
                r = mid - 1
        return ans
    
    def isValid(self, s: str) -> bool:
        l = []
        closed = {'}': '{', ']':'[', ')':'('}
        for i in range(len(s)):
            if s[i] in closed:
                if len(l) == 0:
                    return False
                if closed[s[i]] != l.pop():                   
                    return False
            else:
                l.append(s[i])
        return True if not l else False
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            try:
                stack.append(int(i))
            except ValueError:
                v2 = stack.pop()
                v1 = stack.pop()
                if i == '+':
                    stack.append(v1 + v2)
                elif i == '-':
                    stack.append(v1 - v2)
                elif i == '*':
                    stack.append(v1 * v2)
                elif i == '/':
                    stack.append(int(v1 / v2))
        return stack[0]
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # stack = []
        # warmer = 0
        # for i in range(len(temperatures)):
        #     if len(stack) == 0:
        #         warmer = temperatures.pop()
        #         stack.append(0)
        #     else:
        #         curr = temperatures.pop()
        #         if warmer > curr:
        #             stack.append(stack[-1] + 1)
        #         else:
        #             stack.append(0)
        #             warmer = curr
        # ans = stack[::-1]
        # return ans
        n = len(temperatures)
        answer = [0] * n
        stack = []  # will store indices

        for i in range(n):
            # while current temp is warmer than stack top
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            
            stack.append(i)

        return answer
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair = [[p,s] for p, s in zip(position, speed)]

        # stack = []
        # for p, s in sorted(pair)[::-1]:
        #     stack.append((target-p)/s)
        #     if len(stack) >= 2 and stack[-1] <= stack[-2]:
        #         stack.pop()
        # return len(stack)
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        count = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                count = max(profit, count)
            else:
                l = r
            r += 1
        return count
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        chars = set()
        ans = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            ans = max(ans, r-l+1)
        return ans
    
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            middle  = (l + r)//2

            if target == nums[middle]: return middle

            if nums[l] <= nums[middle]:
                if target > nums[middle]:
                    l = middle + 1
                elif target < nums[l]:
                    l = middle + 1
                else:
                    r = middle - 1 
            else:                  
                if target < nums[middle]:
                    r = middle - 1
                elif target > nums[r]:
                    r = middle - 1
                else:
                    l = middle + 1
        return -1  

class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        
    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.minstack[-1]

class TimeMap:

    def __init__(self):
        self.store = {} # key: list of [val, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key,[])
        
        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
                
        return res