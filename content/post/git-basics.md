---
title: Git basics
toc: true
id: 1084
categories:
  - Version Control
date: "2015-04-28T13:50:15+00:00"
---

*   [http://think-like-a-git.net/](http://think-like-a-git.net/)
*   [http://marklodato.github.io/visual-git-guide/index-en.html](http://marklodato.github.io/visual-git-guide/index-en.html)
*   [https://www.atlassian.com/git/tutorials/](https://www.atlassian.com/git/tutorials/)

### local repository

#### checkout

##### checkout &lt;branch&gt;

> switch branch


```java
git checkout dev
```

![checkout-branch](/media/checkout-branch.png)

##### checkout &lt;commit&gt; [files]

> &lt;commit&gt; is HEAD by default. The current branch doesn't change, without moving the HEAD pointer location.
> 
> 
> copy the &lt;commit&gt; tree to index tree and working tree.


```java
git checkout HEAD
git checkout HEAD^
git checkout HEAD~3 1.txt
git checkout a47c3
```

![chckout-files](/media/chckout-files.png)

#### reset

##### reset &lt;commit&gt; [files]

> move the HEAD, and copying &lt;commit&gt; tree to index or working tree.
> 
> 
> three mode:
> 
> 
> --soft: no copy. move HEAD
> 
> 
> --mixed: copy to index only. move HEAD   = reverse `git add`
> 
> 
> --hard: copy to index and working tree. move HEAD
&nbsp;


```java
git reset HEAD^3
git reset HEAD 1.txt  = reset -- 1.txt
git reset HEAD^ 1.txt
```

![reset-commit](/media/reset-commit.png)

#### diff

##### git diff

working &lt;=&gt; index

##### git diff --cache

index &lt;=&gt; HEAD

##### git diff HEAD

working &lt;=&gt; HEAD

##### git diff HEAD^^

working &lt;=&gt; HEAD^^

##### git diff da985 b325c

da985 &lt;=&gt; b325c

##### git diff &lt;branch&gt;

working &lt;=&gt; &lt;branch&gt; HEAD

![git-diff](/media/git-diff.png)

#### merge

##### fast-forward merge

![ff-merge](/media/ff-merge.png)

##### 3-way merge

![3-way-merge](/media/3-way-merge.png)

#### cherry-pick and rebase

![cherry-pick](/media/cherry-pick.png)

![rebase](/media/rebase.png)

### remote repository

#### remote



```java
remote
remote -v

remote add &lt;remote_repo_name&gt; &lt;url&gt;
git remote add origin git@github.com:richdyang/1.git
```


#### push



```java
push -u &lt;remote_repo_name&gt; &lt;branch&gt;
push
```


#### pull



```java
git pull
```

&nbsp;

&nbsp;
