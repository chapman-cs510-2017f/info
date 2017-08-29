# Getting Started Guide

## Introduction

There is a lot of material covered at the beginning of this course that may seem unfamiliar, or scary. In the sage words of Douglas Adams, **Don't panic.**

<img src="https://octodex.github.com/images/femalecodertocat.png" width="25%" />

The aim of this course is to introduce you to industry-standard tools and practices, so that you will be prepared to deliver professional-grade work to colleagues. 

## Account Setup

Our class will be centered around three cloud-based pieces of technology: 
 1. [CoCalc](https://cocalc.org), a linux server in the cloud with free software installed for you to use.
 1. [GitHub](https://github.com), a central hub for sharing code that has become standard in the open-source community. 
As such, you will need to make accounts in both places and make them communicate to each other.
 1. [Slack](https://scststudents.slack.com), a professional communication platform now standard in industry.

 - **Task 1:** Use your Chapman email to create a GitHub account, a CoCalc account, and a Slack account. Use your full, real name when making the accounts so that you can be easily found. The instructor will invite you to the course GitHub Organization, the CoCalc course, and the Slack organization using your student email, so look for the invite emails.
 - **Task 2:** (Optional) If you like, you can link your CoCalc account to your GitHub to simplify logging in. In your CoCalc account, go to the Settings tab at the top of the screen (with the gear icon), and click on the GitHub logo (the *octocat* mascot logo :octocat:).
 - **Task 3:** Join the `#cs510-2017f` channel for the course in Slack. Note that there are a variety of other Slack channels of potential interest, such as `#physics` or `#math` or `#cpsc` or `#jobopportunities` or `#gamedev` or `#chapman-robotics`, etc.
 
## CoCalc Project Setup

If all is well, you should see a course **project** in your main CoCalc window. Clicking on it will log into an *Ubuntu Linux* cloud computer that will run your class project. When your accounts and projects have all been created successfully, the instructor will add *internet access* to each one manually. Prior to this step, your project will be able to create files and run code normally, but will not be able to connect to external websites such as GitHub.

The interface for navigating folders, creating, and editing files is relatively self-explanatory. Questions can be handled in class, if the Help documentation does not already answer your question.

## Setting up the Linux Terminal (a.k.a. Bash Shell) and SSH

After you verify that your project has internet access (you can check the project Settings tab), we can connect to GitHub via **s**ecure **sh**ell keys (ssh keys). To do this, first open a Linux Terminal. CoCalc has the odd feature of creating a new file for each terminal instance, so it is recommended to create a primary terminal in the main directory of your project that you will use. To do this, type the word "terminal" in the search box (upper left corner of the Files tab of your project). It should report "No files found" and show a panel of possible file types you want to create with that name. Choose the button ">_ Terminal" to create a new Linux Terminal running the Bash Shell.  It should look something like this:

```
                ┌────────────────────────────────────────────┐
┌───────────────┤ Welcome to the CoCalc Terminal Environment ├─────────────────┐
│               └────────────────────────────────────────────┘                 │
│ Software: sage R ipython gap gp git latexmk isympy java julia octave python3 │
│ vim emacs nano joe gcc clang ocaml pdflatex xetex node convert mc htop atop …│
│                                                    ┌─────────────────────────┤
│ Anaconda Python [continuum.io]:  anaconda3         │ Usage: type command and │
│                ... and exit it:  exit-anaconda     │ then hit the return key │
│                                                    └─────────────────────────┤
│ Learn about the Linux terminal:     http://ryanstutorials.net/linuxtutorial/ │
│ Experiencing any problems or is something missing?   email help@sagemath.com │
└──────────────────────────────────────────────────────────────────────────────┘
 
~$  
```

This login screen for the terminal gives a nice summary of all the useful software installed in your linux computer in the cloud, and suggests a good tutorial for how to use the bash shell.  (You can also find many more resources in this `info` repository in the course GitHub Organization. For a quick introduction, see the [Linux/Bash Overview Slides](http://slides.com/profdressel/linux-bash-overview).)

To connect to GitHub, we first need to create `ssh` keys for your linux computer. To do this, type the command `ssh-keygen` into the terminal, and hit `Enter` four times. It should look similar to what is below. (Note, the *prompt* characters `~$` simply let you know that you may type a command, and that you are in your `~` directory, known as "home" and equivalent to `/home/user`.)
```
 ~$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa):
Created directory '/home/user/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/user/.ssh/id_rsa.
Your public key has been saved in /home/user/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:9f4vJzDrftWXdG8Jo60UsqEd0yDd4mq3orslN9Ju/UQ user@project-1c8479d1-dc82-4b59-be53-b8f4bfb0b917
The key's randomart image is:
+---[RSA 2048]----+
|        . .      |
|       . + .     |
|        o =      |
|         B + o ..|
|        S *E= + *|
|      .+ +.+o. o*|
|     o.=o o.o+ o.|
|      *o.o....+ .|
|     +=.. .+o..=.|
+----[SHA256]-----+
~$
```
This command has generated keys in the folder `~/.ssh/` (which is "hidden" since it starts with a `.`). 

You can now add to your "public key" to your GitHub account so that it knows who you are when you try to connect. To do this, run the command `cat ~/.ssh/id_rsa.pub` in the terminal, to produce something like the following:
```
~$ cat ~/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDiZS980QbZ1T+GYJky8QbKDngbH9UxPNKOencPT8rtk6PgBuk7DQrNladts32isd49LpHDgbFJhV/UqY9JvTn9xPXEaGRcgJurbbuE6YKWmKQ5Xl6rl3nLrK+zv4/VL+v4p0wRit/JFbjqSHBE
ni/TcO6dty3EaXH3o8eU/FCk+8kimoQqTnj/P8U/EHDySP0RvAC1k9LxrwKY22Az0J9kiZW7Mb6QJIZqu2mlVSpXQKcpiTEBUfOyWj9WyMiCPhtD0j/500CCAwwlQ2gNH8b3UGZpvxzlkT+wurvKknNGFKej/APpk/ehxbNzrni1oBFzCq/PVItq
gaJMG9B6HgvH user@project-1c8479d1-dc82-4b59-be53-b8f4bfb0b917
~$
```
The string beginning with `ssh-rsa` and ending with (in this case) `917` is your "public RSA key".  Highlight this string with the mouse and copy it (with the right-click menu). Go into your GitHub Account Settings (upper right corner menu on GitHub), then go to the settings tab "SSH and GPG Keys". Click on the button "New SSH Key" in the upper right, and paste your RSA key into the field labeled "Key". In the field labeled "Title", give your key a descriptive name so you know which key it is, for example, "CoCalc CS510 Key". Then click the confirmation button "Add SSH Key".

To confirm that your key works, go back to your Bash Terminal in CoCalc, and type the command `ssh git@github.com`. This tries to log into GitHub via secure shell (ssh) using the account name `git` at the address `github.com`. You should see something like the following:
```
~$ ssh git@github.com
PTY allocation request failed on channel 0
Hi YOUR_GITHUB_USERNAME_HERE! You've successfully authenticated, but GitHub does not provide shell access.
Connection to github.com closed.
~$
```
The important statement is `You've successfully authenticated`. This means that GitHub understands your key properly, and you can communicate between your linux computer in the cloud, and the GitHub server in the cloud via `ssh`.  If you refresh your "SSH and GPG Keys" settings page in GitHub, you will now see your key has a green light next to it to indicate that the connection has been successfully confirmed.

## Cloning the Information Repository

As a check for the connection to GitHub and a demonstration that it works, using the Linux Terminal **m**a**k**e a new **dir**ectory to store `git` repositories using `mkdir`.
```
 ~$ mkdir ~/CS510/
 ~$
```
**C**hange into that **d**irectory using `cd` and **l**i**s**t its contents with `ls`.
```
 ~$ cd CS510
 ~/CS510$ ls
 ~/CS510$
```
The prompt should simply return since the directory is initially empty.

Go to your GitHub account in a different tab/window and find the information repository main page. In the upper right corner, you should see a green "Clone or Download" button. Click the button and it will open up a sub-panel with a clone link. There are two possible links, HTTPS or SSH. Make sure you choose SSH. Click on the copy button to copy the repository clone link to your clipboard.

Return to your terminal and use `git clone` to clone the information repository to your directory "CS510". It should look something like:
```
 ~/CS510$ git clone git@github.com:chapman-cs510-2017f/info.git
Cloning into 'info'...
remote: Counting objects: 20, done.
remote: Compressing objects: 100% (19/19), done.
remote: Total 20 (delta 6), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (20/20), 131.57 KiB | 0 bytes/s, done.
Resolving deltas: 100% (6/6), done.
Checking connectivity... done.
~/CS510$ ls
info
~/CS510$
``` 
Now the list command `ls` shows that there is a new directory `info` that has been cloned from GitHub. You can confirm that it exists outside the terminal by going to the Files tab in your project and browsing around. The cloned files are now local inside your cloud computer, and can be viewed directly.

The above procedure will be how you clone all classwork and homework repositories for the class. For more information about how GitHub works, see the [Git and GitHub Overview Slides](http://slides.com/profdressel/git-overview).
