#  Cloud + AI Journey (52 weeks)

Welcome to my Cloud + AI Engineer learning journey   

This repository documents my progress as I transition from a mechanical background into **Cloud, AI, and Machine Learning engineering**.  

---

## What’s Inside
- `Hello.py` → my first Python program (Day 1)  
- Weekly commits as I progress through my **52-week Cloud + AI Engineer plan**  
- Projects will include:
  - Python automation scripts  
  - AWS cloud deployments  
  - Machine learning experiments  
  - MLOps workflows  

---

## Goals
- Become proficient in **Python, Linux, Git, and AWS**  
- Earn **AWS Developer Associate** and **AWS ML Specialty** certifications  
- Build a portfolio of **end-to-end AI + cloud projects**  
- Land a role as a **Cloud AI Engineer**  

---

## Progress Tracker
- **Day 5:** Git Branching + PR practice
- **Week 1:** Python basics, Git setup → `hello.py`, cipher project, README updates  
- **Week 2:** Python data structures → CSV cleaner, file organizer, API fetcher
- **Week 3:** Extra Python & Git practice (branching, PRs, script improvements)
- **Week 4:** Linux & shell basics → `linux_basics.md` cheat sheet  
- **Week 5:** Git fluency → PR opened & merged, Git 101 notes 

I’ll update this repo regularly with new projects, notes, and code as I learn.  

---

## Weekly Summaries

### Week 1 Summary

#### git Wins
- Set up development environment: installed Python 3.13, Git, VS Code  
- Created first repo: `Cloud_AI_Journey` (moved out of OneDrive into `C:\Dev`)  
- Installed essential VS Code extensions (Python, Jupyter, GitLens, etc.)  
- Wrote and committed first Python script (`Hello.py`)  
- Created and polished `README.md`  
- Posted about the start of my journey on LinkedIn  

####  Misses
- No major misses — first week was mostly setup and environment  

####  Blockers
- None — just learning the Git/GitHub workflow  

####  Plan for Week 2
- Begin creating small Python scripts (file renamer, CSV parser, API fetcher)  
- Practice daily commits and GitHub pushes  
- Start logging blockers/fixes as they come up  

### Week 2 Summary

####  Wins
- Created and committed 3 Python scripts (file renamer, CSV parser, Pokémon API fetcher)  
- Got more confident with Git basics (add, commit, push, commit history)  
- Added inline comments and docstrings → portfolio-ready code  
- Solved real blockers (syntax errors, indentation issues, permission errors, repo clutter)  
- Pulled live data from PokéAPI 🎉  

####  Misses
- Lost ~10 days due to hardware setup + holiday  
- Extra time fixing repo clutter  

####  Blockers
- Windows permissions blocking file deletion (fixed with `takeown` + PowerShell admin)  
- Python indentation + syntax errors (`else:` issue)  
- Repo clutter from cloning inside itself  

### Week 3 Summary

#### Wins
- Built an end-to-end Pokémon data pipeline:
  - `csv_to_pokemon.py` → reads names from CSV, calls PokéAPI, writes `pokemon_data.csv`
  - Error logging to `pokemon_errors.csv` (missed/typo’d names)
  - `pokemon_type_analyzer.py` → counts types from output CSV
- Learned key Python tools/patterns:
  - `requests` + `.json()` for APIs
  - `csv` for reading/writing files
  - `collections.Counter` for quick tallies
  - `ast.literal_eval` to safely parse list strings (e.g., "['grass','poison']")
- Git confidence boost: branched, resolved conflicts, and pushed cleanly

#### Misses
- A few rebase/merge tangles that slowed momentum
- Spent time on local experiments not meant for GitHub (by design, but time-consuming)

#### Blockers
- Merge conflict in `csv_to_pokemon.py` (resolved by choosing simpler error-logging version)
- Indentation/syntax hiccups (missing colons, wrong indent levels)
- “Writer not defined” / write-while-read issues (fixed by separating read & write phases)

#### Plan for Week 4
- Start Linux & shell basics (Windows Terminal/PowerShell + WSL if needed)
  - Files/dirs: `ls`, `pwd`, `cd`, `mkdir`, `rm`, `cp`, `mv`
  - Viewing/searching: `cat`, `less`, `head`, `tail -f`, `grep`
  - Permissions & exec: `chmod`, `whoami`
  - History & chaining: `history`, `|`, `>`, `>>`
- Create a **linux_basics.md** cheat sheet in the repo:
  - Each command with 1–2 line explanation + example
- Practice mini tasks:
  - Parse a log file with `grep` + `wc -l`
  - Batch-rename files with a one-liner
  - Write a tiny shell script (`.sh`) and run it
- Keep daily micro-commits (notes + small exercises)

### Week 4 Summary

#### Wins
- Installed and configured Ubuntu through WSL on Windows.
- Practiced foundational Linux commands:
  - Navigation: `ls`, `pwd`, `cd`, `mkdir`, `rm`
  - File management: `touch`, `echo`, `cat`, `rm`
  - Permissions and execution: `chmod` (symbolic + numeric modes)
- Learned to interpret permission strings (e.g., `-rwxr--r--`) and their numeric equivalents (`744`).
- Took detailed notes and screenshots while testing each command.

#### Misses
- Only completed one focused Linux session due to limited time.
- Didn’t yet reach ownership, `sudo`, or process management commands.

#### Blockers
- Minor confusion switching between PowerShell and WSL terminal environments.
- Time limitations across the week (reduced total learning hours).

#### Plan for Week 5
- Continue Linux Fundamentals (Part 2) + start Intro to Shell Scripting
- Ownership and access control: `chown`, `sudo`, `groups`, `whoami`
- Process management: `ps`, `top`, `kill`, `bg`, `fg`, `sleep`
- Redirection and piping review: `>`, `>>`, `|`, `grep`, `wc`, `sort`
- Write and execute a simple `.sh` shell script to automate a task
- Create a `linux_basics.md` cheat sheet summarizing all commands learned so far
- Commit cheat sheet and script to GitHub with clear commit messages

### Week 5 Summary

#### Wins
- Fully configured and re-installed Ubuntu WSL after earlier setup issues.
- Learned and practiced file ownership, permissions, and user/group management (`chmod`, `chown`, `usermod`, `groups`).
- Created and debugged multiple users (`sam`, `taylor`) and handled access-denied scenarios.
- Wrote and executed a full Bash script that:
  - Read user input
  - Used `date` command substitution (`%A`, `%B`, `%d`)
  - Added logic for weekends vs weekdays
  - Logged outputs with timestamps.
- Understood execution bits (`-rwxr-xr-x`) and variable expansion.
- Built strong intuition for Linux file structure, privileges, and command workflow.

#### Misses
- Minor delays from Ubuntu password reset and user access issues.
- Didn’t log daily notes in the tracking sheet (only GitHub summary).
- Haven’t yet combined Linux automation with external tools (next step).

#### Blockers
- Repeated “access denied” errors when adding `sam` to `dev_project` (resolved via correct group permissions).
- Confusion over directory context (`/home` vs `/home/taylor`) — now clarified.
- Small delays caused by environment reinstalls and resets.

#### Plan for Week 6
- Learn AWS CLI and Azure CLI basics (installation, configuration, test commands).
- Automate a simple cloud task using a shell script, e.g. list S3 buckets or Azure storage containers.
- Understand environment variables and credentials in shell scripting.
- Push your first automation script to GitHub with an explanatory README section.
- Continue reinforcing Linux habits: file redirection, logging, and error handling.

### Week 6 Summary

After taking an extra week to regroup and process everything from Week 5, I used this period to consolidate what I’d learned about Linux automation and apply that foundation to AWS CLI.  
The short gap helped me slow down, review my previous notes, and focus on understanding *why* commands work instead of just running them.  
This week marks my first real step into cloud automation — connecting local shell scripts to AWS.

---

#### Wins
- Installed and configured **AWS CLI v2** successfully on Ubuntu.  
- Created and verified an **IAM user** with Access Key and Secret Key; confirmed connection using `aws sts get-caller-identity`.  
- Set default region/output and linked AWS CLI to the `learn` profile (also exported it as default).  
- Enabled **billing alerts** and a **$1 monthly budget** for cost protection.  
- Practiced core commands:  
  - `aws s3 ls` → list S3 buckets  
  - `aws ec2 describe-instances` → confirm no EC2 instances  
  - `aws iam list-account-aliases` → verify account details  
- Wrote and executed a **shell automation script** that lists all S3 buckets, timestamps the output, and logs results in `~/aws_logs`.  
- Confirmed the script works end-to-end and keeps logs for repeatability.  
- Gained practical understanding of how AWS CLI communicates with IAM credentials and regions.  

---

#### Misses
- Momentum dipped during the catch-up week; needed extra time to review and process material.  
- Didn’t yet complete the extended mini-project (S3 inventory CSV).  
- AWS and Linux notes remain unorganized; plan to rewrite them physically before digitizing.  

---

#### Blockers
- Confusion between profiles and default credential context (resolved by exporting `AWS_PROFILE=learn`).  
- Minor command-line navigation issues when AWS CLI paged results into `less` (resolved with `q`).  
- Overwhelm from large new concepts — currently managing this with a structured catch-up week.  

---

### Plan for Week 7
- Finish the **S3 inventory mini-project** (CSV report + optional upload).  
- Consolidate handwritten notes into structured folders: `Python/`, `Linux/`, `AWS/`, etc.  
- Commit the organized notes and scripts to GitHub.  
- Re-run previous automation scripts to reinforce CLI confidence.  
- Begin exploring **EC2 basics** and understand instance lifecycle commands.  

---

#### Reflection
This two-week window reminded me that consistency matters more than speed.  
Pausing to understand each layer — Linux, automation, AWS CLI — is what will make later projects easier to scale.  
The goal for the next phase isn’t to rush ahead, but to deepen my comprehension and regain steady weekly momentum.


---

## Connect
- GitHub: [Taylor-on-Git](https://github.com/Taylor-on-Git)  
- LinkedIn: [Taylor](https://www.linkedin.com/in/taylor-gilmour-47259a320/)  

---

_More updates to follow. This repository will serve as proof of work — every week adds commits, projects, and documentation until I reach Cloud + AI Engineer readiness._
