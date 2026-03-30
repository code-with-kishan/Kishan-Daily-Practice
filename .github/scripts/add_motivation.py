#!/usr/bin/env python3
import os
import random
import datetime
import subprocess
import sys
from pathlib import Path

# DSA problems and solutions
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
    """Calculate which day we're on based on when script started"""
    start_date_file = ".dsa_start_date"
    
    try:
        if os.path.exists(start_date_file):
            with open(start_date_file, 'r') as f:
                start_date = datetime.datetime.strptime(f.read().strip(), "%Y-%m-%d").date()
        else:
            start_date = datetime.datetime.now().date()
            with open(start_date_file, 'w') as f:
                f.write(start_date.strftime("%Y-%m-%d"))
        
        today = datetime.datetime.now().date()
        day_number = (today - start_date).days + 1
        return day_number
    except Exception as e:
        print(f"Error calculating day: {e}")
        return 1

def create_dsa_file(problem, day_num):
    """Create a DSA solution file"""
    try:
        dsa_dir = Path("solutions")
        dsa_dir.mkdir(exist_ok=True)
        
        filename = dsa_dir / f"day_{day_num}_solution.py"
        
        content = f"""# Day {day_num} - {problem['title']} Solution
# Solved on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

{problem['code']}

# Test cases
if __name__ == "__main__":
    # Add test cases here
    pass
"""
        
        with open(filename, 'w') as f:
            f.write(content)
        
        print(f"✅ Created: {filename}")
        return filename
    except Exception as e:
        print(f"❌ Error creating DSA file: {e}")
        return None

def update_readme(day_num, motivation):
    """Update README with daily motivation and streak"""
    try:
        readme_file = Path("README.md")
        
        if not readme_file.exists():
            with open(readme_file, 'w') as f:
                f.write("# DSA Journey\n\n")
                f.write("## Daily Motivation & Progress\n\n")
        
        with open(readme_file, 'r') as f:
            content = f.read()
        
        # Add new entry at the beginning
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        new_entry = f"**Day {day_num}** ({date}): {motivation}\n\n"
        
        # Insert after the header
        parts = content.split("## Daily Motivation & Progress\n\n", 1)
        updated_content = parts[0] + "## Daily Motivation & Progress\n\n" + new_entry + (parts[1] if len(parts) > 1 else "")
        
        with open(readme_file, 'w') as f:
            f.write(updated_content)
        
        print(f"✅ Updated: README.md")
        return True
    except Exception as e:
        print(f"❌ Error updating README: {e}")
        return False

def git_commit(filename, message, day_num):
    """Make a git commit"""
    try:
        subprocess.run(['git', 'add', str(filename)], check=True, capture_output=True)
        result = subprocess.run(['git', 'commit', '-m', message], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Committed: {message}")
            return True
        else:
            print(f"⚠️  Commit message: {result.stdout}")
            return False
    except subprocess.CalledProcessError as e:
        print(f"❌ Git commit failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error in git_commit: {e}")
        return False

def main():
    try:
        print("🚀 Starting DSA Automation Script...")
        
        # Get current day number
        day_num = get_day_number()
        print(f"📅 Day {day_num}")
        
        # Random number of commits (2-5)
        num_commits = random.randint(2, 5)
        print(f"📝 Will create {num_commits} commits today")
        
        commits_made = 0
        
        for commit_idx in range(num_commits):
            try:
                # Random DSA problem
                problem = random.choice(DSA_PROBLEMS)
                
                # Create solution file
                solution_file = create_dsa_file(problem, f"{day_num}_{commit_idx + 1}")
                
                if solution_file is None:
                    print(f"⚠️  Skipping commit {commit_idx + 1}")
                    continue
                
                # Commit message with natural feel
                commit_messages = [
                    f"Solved {problem['title']} - DSA practice #{commit_idx + 1}",
                    f"Day {day_num}: Working on {problem['title']} solution",
                    f"Added {problem['title']} algorithm - Day {day_num}",
                    f"DSA Challenge: Implementing {problem['title']}",
                    f"Day {day_num} progress: {problem['title']} complete",
                ]
                
                commit_msg = random.choice(commit_messages)
                
                # Make commit
                if git_commit(solution_file, commit_msg, day_num):
                    commits_made += 1
                
                # Random delay between commits (to look natural)
                if commit_idx < num_commits - 1:
                    import time
                    time.sleep(random.randint(2, 5))
            
            except Exception as e:
                print(f"❌ Error in commit {commit_idx + 1}: {e}")
                continue
        
        # Update README with motivation
        try:
            motivation = random.choice(MOTIVATIONS)
            update_readme(day_num, motivation)
            git_commit("README.md", f"Day {day_num}: {motivation}", day_num)
            commits_made += 1
        except Exception as e:
            print(f"❌ Error updating motivation: {e}")
        
        print(f"\n✅ Script completed! Made {commits_made} commits on Day {day_num}")
        return 0
    
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
