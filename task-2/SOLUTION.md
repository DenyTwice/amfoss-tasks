This task was pretty straightforward as well, though I did have to learn one or two new linux commands.

Firstly, I had to clone the TerminalHunt repo by using 

```
git clone https://github.com/gauthamk02/TerminalHunt.git
```
I then used

```
cd TerminalHunt
```
to navigate into the directory and then created another directory, **"solution"** with
```
mkdir solution
```
After finding the answers to the questions given, I used
```
cat > part1.txt
562
```
and hit _ctrl + d_ to create the textfile _part1.txt_ as well as enter the final answer into it.

I then navigated to folder 06 (with the _cd_ command mentioned previously) in TerminalHunt and copied the first file into my solution directory by running
```
cp 1.txt ../solution
```
I went back to the solution directory and ran
```
mv 1.txt part2.txt
```
to rename the file.

Next, I ran
```
git log
```
to view the commit history and find the next answer. Using the same steps as before, I copied and renamed the required file to my solution directory as part3.txt

To stage and commit my work, I used
```
git add .
git commit -m "Commit Message"
```
I then used
```
git checkout asia
find . -name athens.txt
```
to find the final piece of the puzzle.

After merging the branch _asia_ with
```
git checkout main
git marge asia
```
I copied and renamed the _athens.txt_ file into the solution directory.

To concatenate the different files into _password.txt_, I did
```
cat part1.txt part2.txt part3.txt part4.txt > password.txt
```
and then deleted the redundant files with
```
rm part1.txt part2.txt part3.txt part4.txt
```

Finally, I ran
```
git add .
git commit -m "Task 2 done"
git push origin main
```
to stage, commit and push my progess to the remote repo.


Screenshot of the Scroll:
![Screenshot](screenshot.png)
