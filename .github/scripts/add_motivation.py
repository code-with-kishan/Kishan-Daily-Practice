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

def log(msg, level="INFO"):
    """Print logs with timestamp and level"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {msg}")

def check_git_config():
    """Check git configuration"""
    log("=" * 60)
    log("CHECKING GIT CONFIGURATION", "CHECK")
    log("=" * 60)
    
    try:
        result = subprocess.run(['git', 'config', '--list'], capture_output=True, text=True)
        user_name = subprocess.run(['git', 'config', 'user.name'], capture_output=True, text=True)
        user_email = subprocess.run(['git', 'config', 'user.email'], capture_output=True, text=True)
        
        log(f"Git User Name: {user_name.stdout.strip()}")
        log(f"Git User Email: {user_email.stdout.strip()}")
        
        if user_name.stdout.strip() and user_email.stdout.strip():
            log("✅ Git config is set correctly", "SUCCESS")
            return True
        else:
            log("❌ Git config is NOT set correctly", "ERROR")
            return False
    except Exception as e:
        log(f"❌ Error checking git config: {e}", "ERROR")
        return False

def check_repo_status():
    """Check repository status"""
    log("=" * 60)
    log("CHECKING REPOSITORY STATUS", "CHECK")
    log("=" * 60)
    
    try:
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        log("Git Status Output:")
        for line in result.stdout.split('\n'):
            log(f"  {line}")
        
        result = subprocess.run(['git', 'log', '--oneline', '-n', '3'], capture_output=True, text=True)
        log("Last 3 Commits:")
        for line in result.stdout.split('\n'):
            if line:
                log(f"  {line}")
        
        return True
    except Exception as e:
        log(f"❌ Error checking repo status: {e}", "ERROR")
        return False

def get_day_number():
    """Calculate which day we're on based on when script started"""
    log("=" * 60)
    log("CALCULATING DAY NUMBER", "CHECK")
    log("=" * 60)
    
    start_date_file = ".dsa_start_date"
    
    try:
        if os.path.exists(start_date_file):
            with open(start_date_file, 'r') as f:
                start_date = datetime.datetime.strptime(f.read().strip(), "%Y-%m-%d").date()
            log(f"Found existing start date: {start_date}")
        else:
            start_date = datetime.datetime.now().date()
            with open(start_date_file, 'w') as f:
                f.write(start_date.strftime("%Y-%m-%d"))
            log(f"Created new start date: {start_date}")
        
        today = datetime.datetime.now().date()
        day_number = (today - start_date).days + 1
        log(f"Today's date: {today}")
        log(f"Day number: {day_number}", "SUCCESS")
        return day_number
    except Exception as e:
        log(f"❌ Error calculating day: {e}", "ERROR")
        return 1

def create_dsa_file(problem, day_num):
    """Create a DSA solution file"""
    try:
        dsa_dir = Path("solutions")
        dsa_dir.mkdir(exist_ok=True)
        log(f"Solutions directory: {dsa_dir.absolute()}")
        
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
        
        log(f"✅ Created file: {filename.absolute()}", "SUCCESS")
        return filename
    except Exception as e:
        log(f"❌ Error creating DSA file: {e}", "ERROR")
        return None

def update_readme(day_num, motivation):
    """Update README with daily motivation and streak"""
    try:
        readme_file = Path("README.md")
        
        if not readme_file.exists():
            log("README.md not found, creating new one")
            with open(readme_file, 'w') as f:
                f.write("# DSA Journey\n\n")
                f.write("## Daily Motivation & Progress\n\n")
        
        with open(readme_file, 'r') as f:
            content = f.read()
        
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        new_entry = f"**Day {day_num}** ({date}): {motivation}\n\n"
        
        parts = content.split("## Daily Motivation & Progress\n\n", 1)
        updated_content = parts[0] + "## Daily Motivation & Progress\n\n" + new_entry + (parts[1] if len(parts) > 1 else "")
        
        with open(readme_file, 'w') as f:
            f.write(updated_content)
        
        log(f"✅ Updated: {readme_file.absolute()}", "SUCCESS")
        return True
    except Exception as e:
        log(f"❌ Error updating README: {e}", "ERROR")
        return False

def git_add_file(filename):
    """Add file to git staging"""
    try:
        result = subprocess.run(['git', 'add', str(filename)], capture_output=True, text=True)
        if result.returncode == 0:
            log(f"✅ Added to git: {filename}")
            return True
        else:
            log(f"❌ Failed to add {filename}: {result.stderr}", "ERROR")
            return False
    except Exception as e:
        log(f"❌ Error adding file: {e}", "ERROR")
        return False

def git_commit(filename, message):
    """Make a git commit"""
    try:
        # First add the file
        if not git_add_file(filename):
            return False
        
        # Then commit
        result = subprocess.run(['git', 'commit', '-m', message], capture_output=True, text=True)
        
        if result.returncode == 0:
            log(f"✅ Committed: {message}", "SUCCESS")
            # Show what was committed
            result = subprocess.run(['git', 'log', '-1', '--oneline'], capture_output=True, text=True)
            log(f"   {result.stdout.strip()}")
            return True
        else:
            log(f"⚠️  Commit output: {result.stdout}", "WARN")
            log(f"⚠️  Commit stderr: {result.stderr}", "WARN")
            return False
    except Exception as e:
        log(f"❌ Error committing: {e}", "ERROR")
        return False

def git_push():
    """Push commits to remote"""
    log("=" * 60)
    log("PUSHING COMMITS TO REMOTE", "CHECK")
    log("=" * 60)
    
    try:
        result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
        
        if result.returncode == 0:
            log(f"✅ Successfully pushed to remote", "SUCCESS")
            log(f"Output: {result.stdout}")
            return True
        else:
            log(f"❌ Push failed", "ERROR")
            log(f"Output: {result.stdout}")
            log(f"Error: {result.stderr}")
            return False
    except Exception as e:
        log(f"❌ Error pushing: {e}", "ERROR")
        return False

def main():
    try:
        log("=" * 60)
        log("STARTING DSA AUTOMATION SCRIPT", "START")
        log("=" * 60)
        
        # Check git config first
        if not check_git_config():
            log("❌ Git config not set. Cannot proceed.", "ERROR")
            return 1
        
        # Check repo status
        check_repo_status()
        
        # Get current day number
        day_num = get_day_number()
        
        # Random number of commits (2-5)
        num_commits = random.randint(2, 5)
        log(f"Will create {num_commits} commits", "INFO")
        
        log("=" * 60)
        log("CREATING COMMITS", "CHECK")
        log("=" * 60)
        
        commits_made = 0
        
        for commit_idx in range(num_commits):
            try:
                log(f"--- Commit {commit_idx + 1}/{num_commits} ---", "INFO")
                
                # Random DSA problem
                problem = random.choice(DSA_PROBLEMS)
                log(f"Selected problem: {problem['title']}")
                
                # Create solution file
                solution_file = create_dsa_file(problem, f"{day_num}_{commit_idx + 1}")
                
                if solution_file is None:
                    log(f"⚠️  Skipping commit {commit_idx + 1}", "WARN")
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
                if git_commit(solution_file, commit_msg):
                    commits_made += 1
                
                # Random delay between commits
                if commit_idx < num_commits - 1:
                    import time
                    time.sleep(random.randint(1, 3))
            
            except Exception as e:
                log(f"❌ Error in commit {commit_idx + 1}: {e}", "ERROR")
                continue
        
        # Update README with motivation
        log("=" * 60)
        log("UPDATING MOTIVATION", "CHECK")
        log("=" * 60)
        
        try:
            motivation = random.choice(MOTIVATIONS)
            log(f"Motivation: {motivation}")
            update_readme(day_num, motivation)
            git_commit("README.md", f"Day {day_num}: {motivation}")
            commits_made += 1
        except Exception as e:
            log(f"❌ Error updating motivation: {e}", "ERROR")
        
        # Check status before push
        log("=" * 60)
        log("STATUS BEFORE PUSH", "CHECK")
        log("=" * 60)
        check_repo_status()
        
        # Push all commits
        git_push()
        
        log("=" * 60)
        log(f"SCRIPT COMPLETED - Made {commits_made} commits on Day {day_num}", "SUCCESS")
        log("=" * 60)
        return 0
    
    except Exception as e:
        log(f"❌ Fatal error: {e}", "ERROR")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
