# Terminal Hunt
This task was pretty straightforward as well, though I did have to relearn one or two linux commands.

Firstly, I had to clone the **TerminalHunt** repo by using 

```bash
git clone https://github.com/gauthamk02/TerminalHunt.git
```
I then used

```bash
cd TerminalHunt
```
to navigate into the directory and then created another directory, **"solution"** with
```bash
mkdir solution
```
After finding the answers to the questions given, I used
```bash
cat > part1.txt
562
```
and hit _ctrl + d_ to create the textfile **part1.txt** as well as enter the final answer into it.

I then navigated to **folder 06** (with the _cd_ command mentioned previously) in **TerminalHunt** and copied the first file into my **solution** directory by running
```bash
cp 1.txt ../solution
```
I went back to the **solution** directory and ran
```bash
mv 1.txt part2.txt
```
to rename the file.

Next, I ran
```bash
git log
```
to view the commit history and find the next answer. Using the same steps as before, I copied and renamed the required file to my solution directory as **part3.txt**.

To stage and commit my work, I used
```bash
git add .
git commit -m "3 parts done"
```
I then used
```bash
git checkout asia
find . -name athens.txt
```
to find the final piece of the puzzle.

After merging the branch _asia_ with
```bash
git checkout main
git marge asia
```
I copied and renamed the **athens.txt** file into the solution directory.

To concatenate the different files into **password.txt**, I did
```bash
cat part1.txt part2.txt part3.txt part4.txt > password.txt
```
and then deleted the redundant files with
```bash
rm part1.txt part2.txt part3.txt part4.txt
```

Finally, I ran
```bash
git add .
git commit -m "Task 2 done"
git push origin main
```
to stage, commit and push my progess to the remote repo.


Screenshot of the Scroll:
![Screenshot](screenshot.png)
