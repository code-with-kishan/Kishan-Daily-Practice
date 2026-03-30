#!/usr/bin/env python3
"""
DSA Daily Commit Script
Creates random DSA solution files and commits them
"""
import os
import random
import datetime
import subprocess
from pathlib import Path

# ==================== CONFIGURATION ====================
# Change these to your actual values
GIT_USER_NAME = "code-with-kishan"
GIT_USER_EMAIL = "kishan@example.com"
# ========================================================

DSA_PROBLEMS = [
    {
        "title": "Two Sum",
        "code": """def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []"""
    },
    {
        "title": "Reverse String",
        "code": """def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s"""
    },
    {
        "title": "Binary Search",
        "code": """def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1"""
    },
    {
        "title": "Merge Sorted Arrays",
        "code": """def mergeSorted(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result"""
    },
    {
        "title": "Palindrome Check",
        "code": """def isPalindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]"""
    },
    {
        "title": "Fibonacci",
        "code": """def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b"""
    },
    {
        "title": "Valid Parentheses",
        "code": """def isValidParentheses(s):
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return False
    return len(stack) == 0"""
    },
    {
        "title": "Longest Substring Without Repeating",
        "code": """def lengthOfLongestSubstring(s):
    char_index = {}
    max_length = 0
    start = 0
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_length = max(max_length, i - start + 1)
    return max_length"""
    },
]

MOTIVATIONS = [
    "Every DSA problem solved is a step closer to mastery! 💪",
    "Consistency beats perfection. Keep grinding! 🚀",
    "Today's code is tomorrow's solution. Keep learning! 📚",
    "Algorithms are the language of problem solving! 🧠",
    "One step at a time. You're building something great! ✨",
    "The best time to learn DSA was yesterday. The second best is today! ⏰",
    "Practice makes perfect. Keep pushing! 🎯",
    "Every commit is a victory. Celebrate your progress! 🏆",
    "Data structures are the foundation of great code! 🏗️",
    "Keep iterating, keep improving! 🔄",
]

def get_day_number():
    """Get day number"""
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

def create_solution_file(problem, day_num):
    """Create a solution file"""
    Path("solutions").mkdir(exist_ok=True)
    filename = Path("solutions") / f"day_{day_num}_solution.py"
    
    content = f"""# {problem['title']}
# Day {day_num} - {datetime.datetime.now().strftime('%Y-%m-%d')}

{problem['code']}

if __name__ == "__main__":
    pass
"""
    
    with open(filename, 'w') as f:
        f.write(content)
    return filename

def update_readme(day_num, motivation):
    """Update README with motivation"""
    readme = Path("README.md")
    if not readme.exists():
        with open(readme, 'w') as f:
            f.write("# DSA Daily Practice\n\n## Progress\n\n")
    
    with open(readme, 'r') as f:
        content = f.read()
    
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    entry = f"**Day {day_num}** ({date}): {motivation}\n\n"
    
    parts = content.split("## Progress\n\n", 1)
    new_content = parts[0] + "## Progress\n\n" + entry + (parts[1] if len(parts) > 1 else "")
    
    with open(readme, 'w') as f:
        f.write(new_content)

def main():
    print("🚀 Starting DSA Automation")
    
    # Get day
    day = get_day_number()
    print(f"📅 Day {day}")
    
    # Random commits (2-5)
    num_commits = random.randint(2, 5)
    print(f"📝 Creating {num_commits} commits")
    
    # Create commits
    for i in range(num_commits):
        problem = random.choice(DSA_PROBLEMS)
        file = create_solution_file(problem, f"{day}_{i+1}")
        print(f"✅ Created: {file}")
    
    # Update README
    motivation = random.choice(MOTIVATIONS)
    update_readme(day, motivation)
    print(f"📌 Added: {motivation}")
    
    print("✅ Script complete!")

if __name__ == "__main__":
    main()
