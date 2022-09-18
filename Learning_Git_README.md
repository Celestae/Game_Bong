# GIT

main source : https://www.youtube.com/watch?v=RGOj5yH7evk&t=2583s

## What is Git and Git Hub

It's a version control system. It's a way to track our code changes. It's useful to understand what we did when, go track down bugs or go back to a previous version.

### Terms

**Directory** => Folder

**Terminal or Command Line** => Interface for Text Commands
- Navigate through folders
- Create, Update, Change folders
- Install and run programs

**CLI** => Command Line Interface
Interact with files. We can open or close them with a command line.

**cd** => Change Directory
Double clicking on a folder.
So we use cd/folder_we_want to get to it

**Code Editor** => Word processor to write code
VSCode
Text

**Repository** => Our project
The folder where my project is

**GitHub** => Website to host all our repositories

### Git Commands

**Clone** => Bring a repository hosted on Github into a folde ron our local machine

**add** => Track our files and changes in Git

**commit** => Saves files in Git

**push** => Ipload Git commits to a remote repo (GitHub)

**pull** =`Download changes from remote repo our local machine. 
Opposite of push

## Cloning a project

**command :** git clone

We need to pull up the link of the repository on GitHub.
![image](https://user-images.githubusercontent.com/76761076/190878775-3e5b5abe-9ffd-443d-9c45-da8ad13d90ef.png)

**command :** ls
It allows us to see which file are on the folder we are currently in. There's only game_bong in my folder right now.

![image](https://user-images.githubusercontent.com/76761076/190879002-3b391523-49a9-4845-9558-f0ebbd21cc51.png)

**command :** git status
It shows all the files that were updated, created or deleted; but haven't been saved to a commit yet.
One file has been modified; my game.bong
Sometimes, there are untracked files. Those are the files we created on our local machine, but Git doesn't know about them so we have to add them.

## Local Git Workflow / Github Workflow
**command :** git add . 
It will track all the files

**command :** git add [name of the file]
It wil track the file/folder selected. 

Now, my game file has been added and we can see it because it's green now. Now, it's ready to be commited.

![image](https://user-images.githubusercontent.com/76761076/190879021-74b0c32a-e43f-45b9-869d-62356dba2c72.png)

**command :** git commit -m "message(what and why)" -m
The first -m is the title
The second is the description box

**command :** git push (-u) origin master
-u = Next time, we can git push and it's gonna, by default, push it to the master

![image](https://user-images.githubusercontent.com/76761076/190883551-94b77554-c4f7-47fb-88eb-0921bee24fd1.png)





## Learning about Git Branching


We work on a master/main branch. It is the default one of our repository. All our code is there, all our commits are made there.
BUT
Git Branching could be seen as a tree, we can branch out of the main brain. Those are called Feature Branch.

The code on the main branch and the feature branch at first are the same, but as we make changes; those two codes will differ. If we revert back to the main branch, we won't see all the changes we made on the feature branch. 

The opposite is true. Let's say we create a Feature branch at commit 2, but on the main branch we still continue to change our code and make a 3rd commit. The feature branch created previously won't be affected by the new changes on the main branch.

It is useful to test new features that may break the code so we don't affect the main branch, if different people are working on the same repository/project or if we want to debug a part of the code (Hot Fix Branch). So we work there and work on our new feature so when it is good to go, we can merge it into the main branch.

command : git branch

It shows all the branch of our repository. The star (*) means that we are currently on the selected branch.

![image](https://user-images.githubusercontent.com/76761076/190883626-627c06dc-b899-4054-9ab2-d2f056cbe1c9.png)

command : git checkout
To switch between branches
*using Tab completion so it can autofill the branch we want. Sometimes, it can be too long to type or to remember.

![image](https://user-images.githubusercontent.com/76761076/190883745-b2bd7cc8-3ee5-4af7-8d6f-ab124f231e9f.png)


command : git checkout -b feature/add_score
To create new branches
The name has to be as descriptive as possible

![image](https://user-images.githubusercontent.com/76761076/190883691-3620750d-d7cf-42e1-a214-cea8dc7ca432.png)

![image](https://user-images.githubusercontent.com/76761076/190883711-de8dd2bd-b7f5-48ad-91cf-bdf80839c425.png)

We are now on the second branch, which is the feature we created.

![image](https://user-images.githubusercontent.com/76761076/190885204-44e0d063-3a0e-44c1-bd41-d777400915e7.png)
![image](https://user-images.githubusercontent.com/76761076/190885246-a225bd41-41a7-4a1a-bd7c-25397bb6dc41.png)

Now, I saved the changes into Git, but only in the feature/add_score branch

command : git merge
Allow to merge the two branches locally

command : git diff [name of the branch you want to compare the current's one to]
Show the difference between the two versions of a code

![image](https://user-images.githubusercontent.com/76761076/190885536-54fe00a8-b102-496e-9f42-961b13edbe8a.png)

It shows which file has changed.
In red => changes
In grey => Things that were already there

![image](https://user-images.githubusercontent.com/76761076/190885650-c628670f-abf8-4974-8a26-86a998959e90.png)

We need to switch to the branch we want to push first before we make a push and they will ask us which branch we want to push.
They will tell us to do it as shown on the screenshot.

"git push --set-upstream origin feature/add_score"

## What is a pull request

We have a feature branch and we want its code to be push in the master branch. So we make a PR to the master branch.
Once we make a PR people can view, comment.

We can accept the push request we made on GitHub. Then make a pull request so our local machine's file and Git Hub's file match.

command : git pull

![image](https://user-images.githubusercontent.com/76761076/190886050-7c2c1364-7367-4d32-b63f-af1f07510690.png)


After the pull, we can safely delete the branch on GitHub or on our local machine using

command : git branch -d [name of the branch]

![image](https://user-images.githubusercontent.com/76761076/190886099-6d0b3369-3085-4b98-9c81-89cbcc6c32d3.png)

### Merging conflict













