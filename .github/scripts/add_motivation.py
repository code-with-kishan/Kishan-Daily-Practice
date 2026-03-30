#!/usr/bin/env python3
import os
import random
import datetime
from pathlib import Path

PROBLEMS = [
    ("Two Sum", "def twoSum(nums, target):\n    seen = {}\n    for i, num in enumerate(nums):\n        complement = target - num\n        if complement in seen:\n            return [seen[complement], i]\n        seen[num] = i\n    return []"),
    ("Binary Search", "def binarySearch(arr, target):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1"),
    ("Merge Sorted", "def mergeSorted(arr1, arr2):\n    result = []\n    i = j = 0\n    while i < len(arr1) and j < len(arr2):\n        if arr1[i] <= arr2[j]:\n            result.append(arr1[i])\n            i += 1\n        else:\n            result.append(arr2[j])\n            j += 1\n    result.extend(arr1[i:])\n    result.extend(arr2[j:])\n    return result"),
    ("Palindrome", "def isPalindrome(s):\n    s = ''.join(c.lower() for c in s if c.isalnum())\n    return s == s[::-1]"),
    ("Fibonacci", "def fibonacci(n):\n    if n <= 1:\n        return n\n    a, b = 0, 1\n    for _ in range(2, n + 1):\n        a, b = b, a + b\n    return b"),
    ("Valid Parentheses", "def isValidParentheses(s):\n    stack = []\n    pairs = {'(': ')', '{': '}', '[': ']'}\n    for char in s:\n        if char in pairs:\n            stack.append(char)\n        else:\n            if not stack or pairs[stack.pop()] != char:\n                return False\n    return len(stack) == 0"),
    ("Longest Substring", "def lengthOfLongestSubstring(s):\n    char_index = {}\n    max_length = 0\n    start = 0\n    for i, char in enumerate(s):\n        if char in char_index and char_index[char] >= start:\n            start = char_index[char] + 1\n        char_index[char] = i\n        max_length = max(max_length, i - start + 1)\n    return max_length"),
    ("Reverse String", "def reverseString(s):\n    left, right = 0, len(s) - 1\n    while left < right:\n        s[left], s[right] = s[right], s[left]\n        left += 1\n        right -= 1\n    return s"),
]

MOTIVATIONS = [
    "Every DSA problem solved is a step closer to mastery! 💪",
    "Consistency beats perfection. Keep grinding! 🚀",
    "Today's code is tomorrow's solution! 📚",
    "Algorithms are the language of problem solving! 🧠",
    "One step at a time. You're building something great! ✨",
    "Practice makes perfect. Keep pushing! 🎯",
    "Every commit is a victory. Celebrate your progress! 🏆",
    "Keep iterating, keep improving! 🔄",
]

def get_day():
    start_file = ".dsa_start_date"
    if os.path.exists(start_file):
        with open(start_file, 'r') as f:
            start = datetime.datetime.strptime(f.read().strip(), "%Y-%m-%d").date()
    else:
        start = datetime.datetime.now().date()
        with open(start_file, 'w') as f:
            f.write(start.strftime("%Y-%m-%d"))
    today = datetime.datetime.now().date()
    return (today - start).days + 1

def main():
    day = get_day()
    num_commits = random.randint(2, 5)
    
    print(f"Day {day}: Creating {num_commits} commits")
    
    Path("solutions").mkdir(exist_ok=True)
    
    for i in range(num_commits):
        title, code = random.choice(PROBLEMS)
        filename = Path("solutions") / f"day_{day}_{i+1}_solution.py"
        content = f"# {title}\n# Day {day}\n\n{code}\n"
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Created: {filename}")
    
    readme = Path("README.md")
    if not readme.exists():
        with open(readme, 'w') as f:
            f.write("# DSA Daily Practice\n\n## Progress\n\n")
    
    with open(readme, 'r') as f:
        content = f.read()
    
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    motivation = random.choice(MOTIVATIONS)
    entry = f"**Day {day}** ({date}): {motivation}\n\n"
    
    if "## Progress\n\n" in content:
        parts = content.split("## Progress\n\n", 1)
        new_content = parts[0] + "## Progress\n\n" + entry + parts[1]
    else:
        new_content = content + entry
    
    with open(readme, 'w') as f:
        f.write(new_content)
    
    print(f"Updated README with Day {day}")
    print("Done!")

if __name__ == "__main__":
    main()
