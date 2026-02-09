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