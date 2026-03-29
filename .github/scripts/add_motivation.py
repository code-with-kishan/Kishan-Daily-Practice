#!/usr/bin/env python3
import os
from datetime import datetime
import random

# List of motivational quotes
QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The future depends on what you do today. - Mahatma Gandhi",
    "Success is not final, failure is not fatal. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "It is during our darkest moments that we must focus to see the light. - Aristotle",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "Life is 10% what happens to you and 90% how you react to it. - Charles R. Swindoll",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
    "Do something today that your future self will thank you for. - Sean Patrick Flanery",
    "Great things never come from comfort zones. - Unknown",
    "Dream it. Believe it. Build it. - Unknown",
    "Success doesn't just find you. You have to go out and get it. - Unknown",
    "The harder you work for something, the greater you'll feel when you achieve it. - Unknown",
    "Dream bigger. Do bigger. - Unknown",
    "Don't stop when you're tired. Stop when you're done. - Unknown",
    "Wake up with determination. Go to bed with satisfaction. - Unknown",
    "Do what you have to do, to do what you want to do. - Unknown",
    "Success is the sum of small efforts repeated day in and day out. - Robert Collier",
    "Your limitation—it's only your imagination. - Unknown",
    "Push yourself, because no one else is going to do it for you. - Unknown",
    "Sometimes we're tested not to show our weaknesses, but to discover our strengths. - Unknown",
    "The key to success is to focus on goals, not obstacles. - Unknown",
    "Dream as if you'll live forever. Live as if you'll die today. - James Dean",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
    "If you are working on something that you really care about, you don't have to be pushed. The vision pulls you. - Steve Jobs",
    "You don't need to see the whole staircase, just take the first step. - Martin Luther King Jr.",
    "Everything you want is on the other side of fear. - Unknown",
    "Believe in yourself. You are braver than you believe, stronger than you seem, and smarter than you think. - A.A. Milne",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Unknown",
]

def get_random_quote():
    """Get a random motivational quote"""
    return random.choice(QUOTES)

def read_readme():
    """Read the current README.md file"""
    if os.path.exists("README.md"):
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    return ""

def add_motivation_to_readme():
    """Add today's motivational quote to the README"""
    quote = get_random_quote()
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Format the motivation entry
    motivation_entry = f"\n\n### 💪 Daily Motivation ({today})\n> {quote}\n"
    
    # Read current README
    readme_content = read_readme()
    
    # If README doesn't have a motivation section, create one at the top
    if "## Daily Motivation" not in readme_content:
        readme_content = f"## Daily Motivation\n{motivation_entry}\n" + readme_content
    else:
        # Find the Daily Motivation section and add the new entry after the header
        lines = readme_content.split("\n")
        insert_index = 0
        for i, line in enumerate(lines):
            if "## Daily Motivation" in line:
                insert_index = i + 1
                break
        
        lines.insert(insert_index, motivation_entry)
        readme_content = "\n".join(lines)
    
    # Write back to README
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print(f"✅ Added motivation for {today}")
    print(f"Quote: {quote}")

if __name__ == "__main__":
    add_motivation_to_readme()