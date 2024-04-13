Git commands


`git init`  => to initialise   directory to git repository .


`git add .`   => to add/stage all file and folder changes 


`git commit -m "message"` => to commit changes 


`git branch`  => to see all local branch


`git branch -a`  => to see all branch branches including remote branches


`git branch -m newBranchName` => to rename/move  current branch  


`git checkout -b newBranch`  =>  create and switch to a newBranch with current branch's files . Creating new branch from main branch would be a better approach


`git checkout branchName`  => take us to a local branch 


`git  git checkout -- <file_name>` => to undo just modified changes

`git  git checkout -- .` => to  just modified all changes




`git fetch --all` => fetch all branch from remote repository


`git switch branchName`  => let us checkout to a remote branch 
*Do a `git fetch  - –all` to get all remote branchs, then switch to a remote branch


`git branch -d  branchName` => to delete a branch 


`git push origin -d branchName`  => to delete a remote branch


`git stash`  => undo and save all  changes


`git stash list`   => stack-order of stashed file changes


`git stash pop`   => get  stashed changes .  working from top of stash stack


`git stash drop`  => discard the changes from top of stash stack








`git remote add origin <url>` => to add remote repository link


`git remote set-url origin <url>` => to set new remote repository link


`git remote -v` => to check remote repository link



`git pull origin branchName`  => pull latest changes from a remote repository


`git push origin branchName`  => push  changes to a remote repository





`git checkout -b branchName origin/branchName`  => to copy  a remote branch to local . Basically it creates a new local branch with the name of branchName and copy all remote branch's data to newly created local branch

`git log` => will display commits history

`git log --abbrev-commit` => This option displays shorter versions of the commit hashes.


`git reset` =>  "caution" this will undo all your changes 

`git reset HEAD~1`   => it will bring us back to 1 commit behind , leaving all changes uncommitted .



make as many commit as possible
always create a feature branch from an updated main branch
