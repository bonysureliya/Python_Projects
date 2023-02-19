import os

commitMessage : str = input("Enter an Commit Message : ")
os.system(f'git add . && git commit -m "{commitMessage}" && git push origin main && git pull origin main')