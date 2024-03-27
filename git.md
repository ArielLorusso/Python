# GIT 
   https://git-scm.com/downloads
   https://git-scm.com/doc
   https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F
   https://git-scm.com/book/en/v2/GitHub-Account-Setup-and-Configuration

Git is an Open Source , version control system  (VCS)
that is available for free under the GNU License
it allows developers to track changes to their code.

# GIT HELP

git help   lets use see the commands , each command has its manual 

```sh
$ git help
```

usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]
##  git commands 
   list of commands shown by `git help`

### START REPOSITORY 
   Start  a working area (see also: git help tutorial)
```sh
   clone   clone a repository into a new directory
   init    create an empty Git repository or reinitialize an existing one
   config    Set user name, email, system, etc... 
      git config --global user.email "you@example.com"   # set email
      git config --global user.name "Your Name"          # set name
      git config --global --list                         # see global config
      git config -l                                      # see every  config

```
  

### WORK   
Work on the current change (see also: `git help everyday`)
```sh
    add        Add file contents to the index
    mv         Move or rename a file, a directory, or a symlink
    restore    Restore working tree files
    rm         Remove files from the working tree and from the index
```

### EXAMINE 
Examine the history and state (see also: git help revisions)
```sh
    log        Show commit logs
    show       Show various types of objects
    bisect     Use binary search to find the commit that introduced a bug
    diff       Show changes between commits, commit and working tree, etc
    grep       Print lines matching a pattern
    status     Show the working tree status
```

### EDIT
Grow mark and tweak your common history
```sh
    commit     Record changes to the repository
    branch     List, create, or delete branches
    switch     Switch branches
    merge      Join two or more development histories together
    reset      Reset current HEAD to the specified state
    rebase     Reapply commits on top of another base tip
    tag        Create, list, delete or verify a tag object signed with GPG
```  

## WORKFLOW in a REMOTE REPO
collaborate in a workflow (see also: `git help workflows`)
```sh
   remote      Manage the set of repositories ("remotes") whose branches you track.
   push        Update remote refs along with associated objects

   fetch       Download objects and refs from another repository
   pull        Fetch remote  +  merge    with another repository or `local branch
```

# COMMIT options
```sh
$ git help commit
```
## Description :
   Create a `new commit` containing the current contents of the index and
   the given `log message` describing the `changes`. The new commit is a
   direct child of `HEAD`, usually the `tip` of the `current branch`, and the
   branch is updated to point to it (unless no branch is associated
   with the working tree, in which case `HEAD` is "detached" as described
   in git-checkout(1)).
       
##   commiting  in several ways:

   1. by using `git-add` (1) to incrementally "add" changes to the index
           before using the commit command (Note: even modified files must
           be "added");

   2. by using `git-rm`(1) to remove files from the working tree and the
           index, again before using the commit command;

   3. by `listing files` as arguments to the commit command (without
           --interactive or --patch switch), in which case the commit will
           ignore changes staged in the index, and instead record the
           current content of the listed files (which must already be known to Git);

   4. by using the `-a` switch with the commit command to automatically
           `"add" changes from all` known files

## OPTIONS
   `-m <msg>, --message=<msg>`
     Use the given <msg> as the commit message. If multiple -m
     options are given, their values are concatenated as separate
     paragraphs.

  `--author=<author>`
     Override the commit author. Specify an explicit author using the
     standard A U Thor <author@example.com> format. Otherwise
     <author> is assumed to be a pattern and is used to search for an
     existing commit by that author (i.e. rev-list --all -i
     --author=<author>); the commit author is then copied from the
     first such commit found.

   `--branch`
      Show the branch and tracking info even in short-format.
      
   `strip`
      Strip leading and trailing empty lines, trailing whitespace,
      commentary and collapse consecutive empty lines.
   `whitespace`
      Same as strip except #commentary is not removed.
   `verbatim`
      Do not change the message at all.

   `scissors`
      Same as whitespace except everything from (and including)
      the line found below is truncated, if the message is to be edited.
      "#" can be customized with core.commentChar.


# GIT EXAMPLE

   ```sh
   git init           #  makes a .git in CWD (current Working Directory)

   git add .           # EVERYTHING ( to stageing for commit )
      add filename    # Specific FILE

   git commit -m "changes desciption" # update repo

   git log              # see commit-hash, autor, date,description  LIST
   ```
   ```js
   commit `ce915de2d6600514ce827fdcfd608e7e5834e708` (HEAD -> master)
   Author: Ariel Lorusso <ariellorusso@gmail.com>
   Date:   Mon Mar 25 20:53:30 2024 -0300

      just a test 2

   commit be30eb33e4a864c5b34d3c2f1e82b6e8424b4a22
   Author: Ariel Lorusso <ariellorusso@gmail.com>
   Date:   Mon Mar 25 20:49:18 2024 -0300

      just a test will delette
   ```
   `ce915de2d6600514ce827fdcfd608e7e5834e708` this is the `commit-hash`
   will be required to work with that specific commit


   ```sh
   git checkout commit-hash # work on that commit
   git show     commit-hash # see file-changes that commit

   rm -rf .git        # Remove Repository (.git directory)


   git show --textconv : new_file   #
   git ls-tree -l HEAD -- /home/ariel/Desktop/C_and_C++/ #
   git cat-file -s 2ad3e3fbe1d5a2249ab821eb64f30c40327fd27c  #
   ```


# VS-Code

## FILE STATES  ()

`1st` icon of the activity bar is the `Explorer`
here we can see Open files and current Directory
`files` will have marks to alert its `status` 
```
   ( white) : Commited
   ( green) : Added by init command
 A ( green) : Added
 U ( green) : Untracked
 M (orange) : Modified
 D ( red  ) : Deleted
```

### SOURCE CONTROL
   1.Repository
   2.Branch
   3.Publish to GitHub
   4.Commit
   5.Refresh
   6.More ( Pull, Push, Clone, Checkout, Fetch)

## COMMIT ()

`3rd` icon of the activity bar is the explorer `Source Control`
here we will see notification with number of `uncommited files`

### Commits

1. Commit with the `blue button`
2. `Write a log` for the whole commit ()
3. click `Accept commit change` in the editor actions (same that splits view)

files can have both `staged changes` and `unstaged changes` 
unstaged changes wont be commited
user should make a new commit if they desire to keep those

### Staged changes
   all files added will save to commit

   Posible actions :
   1. Open
   2. Unstage chenges 

### Changes   
   (unstaged) all files hire wont be save to commit

   Posible Actions :
   1. Open
   2. Discard chenges
   3. Stage changes (will : `git add` )
   
   We can perform them `File-wise` or for `storage all changes`

```sh
this commit was made from VS-Code
This file has comments logging files commitded and not staged

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch master:
#
# Changes to be committed:
#	   new file:   test_file
#
# Changes not staged for commit:
#	   modified:   git.md
#	   deleted:    test file
#
```
## GitHub

1. `Click` on Source Control's  3rd icon `Publish to GitHub`
2. VS-Code will propt usto `login to giuhub`
3. make a `commit` as explained before
4. `Click` on Source Control's  3rd icon `Push commit`  (it changed)

`BEWARE step 3` we `DONT` want to make a `PULL` under any sircunstance
that will lead to our local repository being lost... we `should PUSH`

# GITHUB

## Wellcome "tutorial"

Quick setup — if you’ve done this kind of thing before
```sh
HTTPS  https://github.com/ArielLorusso/C_C-.git
SSH    git@github.com:ArielLorusso/C_C-.git
```
Get started by creating a new file  or uploading an existing file. 
We recommend every repository include a README, LICENSE, and .gitignore.

or create a new repository on the command line
```sh
echo "# C_Projecs" >> README.md
git  init
git  add README.md
git  commit -m "first commit"
git  branch -M main
git  remote add origin https://github.com/ArielLorusso/C_Projecs.git
git  push -u origin main
```
or push an existing repository from the command line
```sh
git remote add origin https://github.com/ArielLorusso/C_C-.git
git branch -M main
git push -u origin main
```
where `main` could be swap for any other `branch`
or import code from another repository

You can initialize this repository with code from a Subversion, Mercurial, or TFS project.

# GITHUB TOKEN

## Error when login in during a push

git push -u origin main

Username for 'https://github.com': ariellorusso
Password for 'https://ariellorusso@github.com': 
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for ' '

   https://stackoverflow.com/questions/68775869/message-support-for-password-authentication-was-removed

Create Personal Access Token on GitHub
From your GitHub account, go to 
   Settings → Developer Settings → Personal Access Token → Tokens (classic) 
   → Generate New Token (Give your password)
  `Fillup the form` → click Generate token  → `Copy the generated Token`  
  it will be something like ghp_sFhFsSHhTzMDreGRLjmks4Tzuzgthdvfsrta
                     or     github_pat_sFhFsSHhTzMDreGRLjmks4Tzuzgthdvfsrta


### For Linux, you need to configure the local GIT client with a username and email address,

```sh
$ git config --global user.name "your_github_username"
$ git config --global user.email "your_github_email"
$ git config -l
```
### Once GIT is configured, we can begin using it to access GitHub. Example:
```sh
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `YOUR-REPOSITORY`...
Username: <type your username>
Password: <type your password or personal access token (GitHub)
```

### Now cache the given record in your computer to remembers the token:
```sh
$ git config --global credential.helper cache
```
### If needed, anytime you can delete the cache record by:

```sh
$ git config --global --unset credential.helper
$ git config --system --unset credential.helper
```
### Now try to pull with -v to verify
```sh
$ git pull -v
```
### Linux/Debian (Clone as follows):
```sh
git clone https://<tokenhere>@github.com/<user>/<repo>.git
```



# BRANCH
git push -u `origin` branch

git fetch : Retrieves the latest changes from the `remote` repository 
git merge : After fetching the changes, Git merges the changes from the remote branch (typically the branch you're tracking) into your current local branch.

it log origin/<branch>


# REF 
a "ref" is a pointer to a specific commit in the repository's history. It can be a branch, a tag, a remote branch, or even a commit hash. Essentially, a ref allows you to refer to a specific state or snapshot of your project's history.




git help git-receive-pack
