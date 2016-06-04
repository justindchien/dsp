# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > pwd = print working directory
sudo = become super user root
exit = exit the shell
apropos = find what manual page is appropriate
find = find files
xargs = execute arguments
mv = move a file or directory
cp = copy a file or directory
rmdir = remove directory
cd = change directory
mkdir = make directory

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
'ls' = list directory
'ls -a' = list all files
'ls -l' = list with long format
'ls -lh' = list long format with readable file size
'ls -lah' = list all files using long format with readable file size
'ls -t' = sort by time and date
'ls -Glp' = list long format and directories but exclude group information

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
'ls -d' = displays only directories
'ls -F' = flags filenames
'ls -r' = displays files in reverse order
'ls -u' = displays files by the file access time
'ls -1' = displays each entry on a line


---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > 'xargs' executes arguments, especially useful in combination with other commands. For example, to find and remove all jpg files in the current directory, 

$ find . -name "*.jpg" | xargs rm

 

