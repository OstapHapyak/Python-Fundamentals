"""
Команди для роботи з GIT

git init
git config --global user.name "Your name"
git config --global user.email "Your@email.com"
git config --global core.editor notepad.exe
git config --list
git remote -v  (check remote repo)
git status
git add file_name
git add . or git add * (the same)
git commit
git commit -m "Message about commit"
git commit -a -m "Message about commit"  (to do commit with add)
git log  (to see list of commits)
git checkout commit_ID
git checkout main  (return to last commit)
git branch
git branch branch_name
git branch -d branch_name  (delete the branch)
git branch -m branch_name  (rename the branch)
git checkout branch_name
git rm file_name  (remove files from the working tree and from the index)
git diff  (to see what is modified but unstaged in repo)
git diff HEAD  (to see difference between committed working repo and current stage of the repo - workspace)
git diff --staged / cached  (to see a list of staged changes)
git diff file.py  (to see changes in the file)
git merge branch name (to do merge to the current branch from another one)
git pull origin main
git push origin main

"""

