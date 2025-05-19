import os
import sys
import shutil
import requests
from cfonts import render
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.panel import Panel

# Initialize console
console = Console()

# Banner Rendering
def display_banner():
    columns, _ = shutil.get_terminal_size()
    border = "═" * (columns - 2)
    title = render('VORTEX', colors=['red', 'yellow'], align='center')
    
    print(f"\033[1;31m╔{border}╗")
    print(title)
    print(f"\033[1;36m           🕵️‍♂️ JACKING TOOLS   |   🛠️ Developer: @PRAYAGRAJJ   | 🌐 @VORTEXCODEZ")
    print(f"\033[1;31m╚{border}╝\n")

# Display feature table
def display_feature_table():
    table = Table(title="🔥 VIP Control Panel", style="bold green", expand=True)
    table.add_column("🔢 No.", justify="center", style="bold cyan", no_wrap=True)
    table.add_column("⚡ Feature Name", style="bold yellow")
    table.add_column("🟢 Status", justify="center", style="bold green")

    options = [
        ("1️⃣", "🌄  BIZZ BHOKALL", "✅ Active"),
        ("2️⃣", "🌄  GOD 2K12-13", "✅ Active"),
        ("3️⃣", "📜  GMAIL (META)", "✅ Active"),
        ("4️⃣", "🐃  OLD TOOL", "✅ Active"),
        ("5️⃣", "🤟  PERMANENT FILE (RANDOM)", "✅ Active"),
    ]

    for num, feature, status in options:
        table.add_row(num, feature, status)
    
    console.print(table)

# Dictionary of script URLs
script_links = {
    1: "https://raw.githubusercontent.com/jaikshaikh/Vortexcodes/refs/heads/main/bizzvip.py",
    2: "https://raw.githubusercontent.com/jaikshaikh/Vortexcodes/refs/heads/main/2013_obf.py",
    3: "https://raw.githubusercontent.com/jaikshaikh/Vortexcodes/refs/heads/main/newhunter_obf.py",
    4: "https://raw.githubusercontent.com/jaikshaikh/Vortexcodes/refs/heads/main/VIP%20old.py",
    5: "https://raw.githubusercontent.com/jaikshaikh/Vortexcodes/refs/heads/main/freeee.py",
}

# Fetch and execute selected script
def fetch_and_execute(choice):
    url = script_links.get(choice)
    if not url:
        console.print("❌ [red]Invalid choice! Please select a valid option.[/red]")
        return

    try:
        with Progress() as progress:
            task = progress.add_task("[yellow]Fetching script...", total=100)
            response = requests.get(url)
            progress.update(task, advance=100)

        if response.status_code == 200:
            exec(response.text, globals())
            if "VORTEX" in globals():
                console.print("\n✅ [green]Executing script...[/green]")
                VORTEX()
            else:
                console.print("⚠️ [yellow]VORTEX() function not found in script.[/yellow]")
        else:
            console.print(f"❌ [red]Failed to fetch script (HTTP {response.status_code})[/red]")
    except Exception as e:
        console.print(f"❌ [red]Error occurred while executing the script:[/red] {e}")

# Main Execution
def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    display_banner()
    display_feature_table()

    try:
        user_input = console.input("\n[bold cyan]Enter a number (1-5) to select a script:[/bold cyan] ")
        choice = int(user_input)
        os.system('clear' if os.name == 'posix' else 'cls')
        display_banner()
        fetch_and_execute(choice)
    except ValueError:
        console.print("❌ [red]Invalid input! Please enter a number between 1 and 5.[/red]")

if __name__ == "__main__":
    main()
