# Commands to remember
Katherine Keith

### Terminal 
`option + [arrow keys]` moves forward backward words 

## LDA, topic models  
[Gensim wrapper of Mallet](https://radimrehurek.com/gensim/models/wrappers/ldamallet.html). 

[Helpful tutorial using this software.](https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/) 

## VS Code
### Other VS Code shortcuts
1. Collapse all functions, `COMMAND + K COMMAND + 0`

### Formatting 
1. Set-up `black` https://devblogs.microsoft.com/python/python-in-visual-studio-code-may-2018-release/
2. Run `Shift + Option + F` while a .py file is open to format it via black. 

### Other short-cuts/tricks in VS Code 
- Rename refactoring (across all files in a project) `highlight variable name + F2`
- Using VS Code with a remote server (ssh) https://code.visualstudio.com/docs/remote/ssh
- VS Code sometimes issues with jupyter notebook. Sometimes this command works `conda install -n env1 ipykernel --update-deps --force-reinstall` and then restart VS Code.

## Sklearn 

### Grid search, cross validation 
```
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss, make_scorer


parameters = {'C': [1.0/2.0**reg for reg in np.arange(-12, 12)]}
lr = LogisticRegression(penalty='l1')
grid_search = GridSearchCV(lr, parameters, cv=10, refit=True, 
                           scoring=make_scorer(log_loss, greater_is_better=True))
grid_search.fit(X, y)
best_model = grid_search.best_estimator_
print(best_model)
print('Training mean accuracy=', best_model.score(X, y))
```

## Latex

### Columns 
```
\begin{columns}
\column{0.45\textwidth}
\column{0.45\textwidth}
\end{columns}
```

### Latex with Sublime 

Using Latex in sublime instructions: http://individual.utoronto.ca/dobronyi/latexsublime.html

#### Sublime snippets
Snippets are short-cut code that can speed up editing. To create a new snippet, within sublime `Tools -> Developer -> New Snippet...`. Here is a template snippet that I made 
```
<snippet>
    <content><![CDATA[\begin{equation*}
    $0
\end{equation*}]]></content>
    <tabTrigger>eqs</tabTrigger>
    <scope>text.tex.latex</scope>
    <description>Equation Star</description>
</snippet>
```
I saved this with the name `EquationStar.sublime-snippet` in the default location. Then, within a latex document write `eqs` and tab and you should get the starred equation enivornment. 

### Use for comments 
```
\usepackage{color}
\newcommand{\kkcomment}[1]{\textcolor{red}{[#1 -KAK]}}
```
### Reduce space between bullets 
```
\usepackage{enumitem}

\begin{itemize}\begin{itemize}[leftmargin=*,noitemsep]
\itemsep0em
```

### Figures 

```
\usepackage{graphicx}
\begin{figure}[t]
\centering
\includegraphics[width=0.5\textwidth]{fig}
\caption{ XXX \label{XXX}}
\end{figure}
```

### Tables 

```
\usepackage{booktabs}
\usepackage{graphicx}
\begin{table}[t]
  \centering
  \resizebox{0.98\linewidth}{!}{ %makes it fit within the margin limits
      \begin{tabular}{lll}
      \toprule
      Relation         & Yes   & No    \\
      \toprule
      Institution      & 27045 & 15579 \\
      Place of birth   & 6992  & 2574 
  \end{tabular}
  }
  \caption{XXX  \label{t:XXX}}
\end{table}
```
### Making tables pretty 
Add ragged right 
```
\usepackage{array}

#later on 
\begin{tabular}{c  >{\raggedright\arraybackslash}p{3cm}}
```

## Pytest 
Test a single function 
```
python -m pytest script.py -k "function name"
```

## Joblib 
From Sergey 2022-02-09
```
from joblib import Parallel, delayed
res = Parallel(n_jobs=40, prefer="threads", verbose=5, require="sharedmem")(
    delayed(update_contractions_with_more_precision)(venue_pair, score) for venue_pair, score in contractions.items()
)
```
Then whatever your function is goes into (delayed), contractions can be anything

## Python

### Importing one module into another
This snippet of code can often be helpful
```
sys.path.insert(0, os.getcwd() + "/synthetic_confound_treat_function")
```

### Coloring text in Python 
```
def print_colored_terms(text, term_list, color="Tomato"):
    import re
    for term in term_list: 
        #for command line print
        #text = re.sub(term, '\033[34m{0}\033[30m'.format(term), text)
        
        #for HTML print within Jupyter Notebooks 
        text = re.sub(term, '<span style="color:{1};">{0}<span style="color:black">'.format(term, color), text)
    return text
```

### Python->R: Write array to csv to load into R
```
def write_array_to_csv(array_of_interest, fout): 
    """
    array_of_interest : np.array
    
    fout : str, what you want to call the file 
    """
    with open(fout, 'w') as w: 
        w.write(','.join([str(x) for x in array_of_interest.tolist()]))
        w.write('\n')
    print('wrote to ->', fout, 'len=', len(array_of_interest))
```
Then in R you can read in via 
```
x <- read.csv(file = 'FILE.csv', header = FALSE)
```

### Python logging module 

Logging that prints to console and to log file 

Top of the file: 
```
from datetime import date
import logging 
logger = logging.getLogger(__name__)
```

In main call: 
```
def logging_set_up(): 
	logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s — %(funcName)s:%(lineno)d — %(message)s")
	today = date.today()
	log_dir = "logs/"
	if not os.path.exists(log_dir): os.mkdir(log_dir)
	log_file = log_dir + str(today)+ "-"+ str(os.path.basename(__file__)) +".log"
	file_handler = logging.FileHandler(log_file) 
	logger.addHandler(file_handler)
	print('saving log file to: ', log_file)
```

Then later in the script you can call: 
```
logger.debug("text here") 
logger.info('saved to->' + str(fname))
logger.warn("more text") 
```

### Install pip package with a conda environment
```
~/anaconda3/envs/events2/bin/pip install PACKAGENAME
```

### Quick number of lines in a file 
```
num_lines = sum(1 for line in open('myfile.txt'))
```

### Python strings 
```
print("{0:<1} {1:<3}".format("blah1", "blah2")
```
left-align `<` 
center `^`
right-align  `>`

### Print precision in numpy 
```
np.format_float_positional(0.5, precision=2)
```
Output will be `0.50`.

### Exceptions
Basic expection method that exists the program 
```
raise Exception('write your message here')
```

## Pandas 

### pandas select rows that have a column match 
```
new_df = old_df.loc[old_df['colm_name'] == 1]
```
### pandas left outer join 
```
df_join = pd.merge(df_left, df_right, left_on='left_id', right_on='right_id', how='left')
```

### Boilerplate 
```
if __name__ == '__main__':
  main()
```

### Argparse 
```
parser = argparse.ArgumentParser()
parser.add_argument("input", help=".json file", type=str)
parser.add_argument('--foobar', action='store_true') #optional argument that if flag is made, stores as true
args = parser.parse_args()
```

### Making folders 
```
if not os.path.exists(folder): os.mkdir(folder)
```

### Dictionaries 
```
#sorts by largest value (Python2)  
sorted(d.items(), key=lambda (k, v): -v)

#sorting by descending value for Python3
sorted(d.items(), key=lambda kv: -kv[1])

#default dict of a default dict 
defaultdict(lambda : defaultdict(int))

#To check if a key is in a dictionary, the fastest way is  
if d.get(k) != None 
```

### Matplotlib 
On a server 
```
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
```
With a Jupyter notebook
```
import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
```
Simple plot 
```
plt.plot(stats['loss_history'])
plt.xlabel('iteration')
plt.ylabel('training loss')
plt.title('Training Loss history')
plt.tight_layout()
plt.savefig('../../HW03-report/q2d', bbox_inches='tight')
plt.show()
```
Clearning plots (for example, when iterating through a loop): 
```
plt.clf()
plt.close()
```

### Parsing HTML tables with BeautifulSoup, save to csv  
Use the browser "inspect" 
```
import urllib, requests, json, time
from bs4 import BeautifulSoup

page_url = "INSERT_DESIRED_URL_HERE"
page = requests.get(page_url)
soup = BeautifulSoup(page.text, 'html.parser') 

fout = 'TEXT_HERE'
ww = open(fout, 'w')
for row in soup.find_all('tr'):
    row.find_all('td')
    cols = row.find_all('td')
    cols = ''.join([ele.text.strip()+',' for ele in cols])+'\n'
    ww.write(cols)
```
Better way to find a certain class or id 
```
soup.findAll("div", {"class": "tweet"})
```

### Other 
Write to standard error when loading big files
```
sys.stderr.write(".")
```

## ssh
How to create ssh keys: https://superuser.com/questions/8077/how-do-i-set-up-ssh-so-i-dont-have-to-type-my-password

## Jupyter notebook 

```
#covert jupyter to .py file 
jupyter nbconvert --to script 1idvl.ipynb
```
### Jupyter notebook as slides! 
https://medium.com/@mjspeck/presenting-code-using-jupyter-notebook-slides-a8a3c3b59d67

1. `View → Cell Toolbar → Slideshow`
2. `jupyter nbconvert SCRIPTNAME.ipynb --to slides --post serve`


### Open jupyter notebook from remote server locally
1. On remote, `~/anaconda3/bin/jupyter notebook --port=9999`
2. On local, `ssh -NL ${PORT}:localhost:${PORT} kkeith@hobbes.cs.umass.edu` where you specify `PORT=9999` or whatever the port is on your remote. 
3. Manually open in a browser `http://localhost:9999/tree`
4. Password `jupyternotebook`

### Add images to Jupyter notebook
Change the cell type to markdown and then use 
```
<img src="graphs/Libertarian.PNG" alt="Drawing" style="width: 500px;">
```

### Using virtualenv within a jupyter notebook 

```
$PROJ=projectname
$ ~/anaconda3/bin/python -m venv $PROJ
$ source $PROJ/bin/activate
(projectname) $ $PROJ/bin/pip install ipykernel
(projectname) $ $PROJ/bin/ipython kernel install --user --name=projectname
```

Make sure that it is in the kernelspec list 
```
jupyter kernelspec list
```

Kernel -> Change kernel 

### Auto-reloading Jupyter Notebook 
```
%load_ext autoreload
%autoreload 2
```

### Using both Python and R within a single Jupyter notebook
 
1. Make sure you are using Python3 with anaconda. 
2. Make sure you have the latest version of R and install an R kernel. Within the R console run (instructions from here https://irkernel.github.io/installation/): 
```
install.packages('IRkernel')
IRkernel::installspec()
```
3. Follow the instructions to download SoS here: https://vatlab.github.io/sos-docs/running.html#content
```
pip install sos
pip install sos-notebook
pip install sos-r
python -m sos_notebook.install
```
4. Then follow the SoS examples and you should be able to run R and Python within the same Jupyter notebook. Trading data back and forth! 
https://vatlab.github.io/blog/post/sos-notebook/

Here is an example that I use often: list of dicts -> pandas dataframe (python) -> R dataframe using SoS 
<img src="imgs/sos.JPG" alt="Drawing" style="width: 500px;">

### Bugs with R kernel in Jupyter Notebook (2021-09-30)
I needed to update the version of R used remotely (hobbes) in Jupyter Notebook. I kept running into this annoying error: 
```
jupyter-client has to be installed but “jupyter kernelspec --version” exited with code 127
```
What fixed the error was changing my `.zshrc` file to include the anaconda path `export PATH="home/kkeith/anaconda3/bin:$PATH"`. 

Then I ran the following in the (updated R version) R console: 
```
install.packages('IRkernel')
IRkernel::installspec(name = 'ir41', displayname = 'R 4.1') #to distingush from the other R
```
This worked! 

## Linux/Unix 

### Vim 
Install supertab so you can tab complete in vim 
1. git clone the source directly https://vimawesome.com/plugin/supertab, use the "Pathogen" directions
2. Add the following to your .vimrc `:so ~/.vim/bundle/supertab/plugin/supertab.vim`

### Symbolic link
```
ln -s ORIGNIAL SYMLINK
```

### bash script
Make the date 
```
START=`date '+%m-%d-%H:%M'`
```

### sending emails with bash
```
mail -s "<<SUBJECT OF EMAIL>>" kkeith@cs.umass.edu < ${file_email_body}
```

### .bashrc
```
#Makes folders colored 
export LS_OPTIONS='--color=auto'
eval "$(dircolors -b)"
alias ls='ls $LS_OPTIONS'
```

### Sed 
Example: Change the expressions "<strong>" and "</strong>" to a space " "
```
sed 's/<strong>/ /g; s/<\/strong>/ /g' INPUTFILE > OUTPUTFILE
```

### Awk 
```
#prints the third column 
awk '{ print $3 }’ yourfile.txt
```

### Parallel 
```
INDIR=/home/kkeith/dir/
GOLD=file.json
CORES=6
ls -1 $INDIR/* | parallel -v --dryrun "python pythonfile.py {}  $GOLD"
ls -1 $INDIR/* | parallel --eta -j$CORES "python getsentment.py {} $GOLD”
```

Multiple inputs
```
cat fileinput | parallel --colsep '\t' myprogram {1} {2} {1}_vs_{2}.result
```
In a for loop 
```
for day in $seq(1 20); do echo "${day}"; done | parallel -v --dryrun "python blah.py {}"
```


### Using a GUI on a remote server
https://www.macissues.com/2014/10/13/how-to-mount-a-remote-system-as-a-drive-using-ssh-in-os-x/
```
sshfs kkeith@hobbes.cs.umass.edu:/home/kkeith/ ~/mount/
umount -f ~/mount/
```

## Git / Github

### Compare two different commits in Github 
From: https://docs.github.com/en/github/committing-changes-to-your-project/comparing-commits#comparing-commits
```
https://github.com/kakeith/REPO-NAME/compare/c3a414e..faf7c6f
```
where `c3a414e` and `faf7c6f` are shortened seven-character SHA codes.

### Create branches and pull requests
This is how I follow the "feature branches" workflow 

1. (Locally) Make sure you are on the master branch and pull any remote updates before you create a new branch
```
git checkout master
git pull origin master
```

1. (Locally) Create a new branch 
```
git checkout -b my-new-feature-branch
```
and when you call `git branch` you should see 
```
  master
* my-new-feature-branch
```

1. After making changes to the files on that branch add and commit them 
```
git add .
git commit -m "message"
```

1. Then push the branch to Github
```
git push origin my-new-feature-branch
```

1. On Github, create a pull request for the branch, merge, and delete the branch. 

1. (Locally) Pull and delete the branch you had 
```
git checkout master
git pull origin master
git branch -d my-new-feature-branch
```
Note: This is a very simple workflow when you're not worried about getting out of sync with others. To improve the workflow follow directions like these: https://gist.github.com/blackfalcon/8428401

#### Branches from remote 
You must create a local branch to add to a remote branch 
```
git pull 
git checkout -b <local-branch> <remote-repository>/<remote-branch>
```
Example: 
```
git checkout -b outcome-corr-migrate remotes/origin/outcome-corr-migrate
```


### Searching
Search within a particular folder on github.com
```
path:FOLDERNAME/ KEYWORD
```

### Remove large files 
Removing a large file that you committed several commits ago but now can't push. (A lot of the filter-branch suggestions don't work for me in many cases) 

E.g. you have an error message: 
```
remote: error: File pytorch.zip is 510.96 MB; this exceeds GitHub Enterprise's file size limit of 100.00 MB
```

2021-10-07 Update, this worked for me 
Follow/modify these instructions https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository#using-the-bfg
1. `wget https://repo1.maven.org/maven2/com/madgag/bfg/1.14.0/bfg-1.14.0.jar` or whatever is here https://rtyley.github.io/bfg-repo-cleaner/
2. in your `.zshrc` add `alias bfg='java -jar bfg-1.14.0.jar`
3. 
```
bfg --delete-files BIG_FILE_NAME GITHUB_REPO_PATH
git reflog expire --expire=now --all && git gc --prune=now --aggressive
git commit -m 'remove large files'
git push
```
 

### Lazy git: add commit push in one function 
Save this in your .bashrc or equivalent 
```
function lgit(){
    #lazy git 
    #last argument is the commit message
    #all args before the last are the files you want to commit 

    #example::
    # lazygit 'blah.py' 'blah2.py' 'this is a test message'
    # --> commits files blah.py blah2.py 
    # --> writes commit mesage 'this is a test message'
    array=($@)
    len=${#array[@]}
    git add "${array[@]:0:$len-1}"
    git commit -m "${array[$len]}"
    git push
}
```

### Git ignore 
Create a git igore like this one: https://paulvanderlaken.com/2020/05/12/create-perfect-gitignore-file-for-project/
Then 
```
git config --global core.excludesFile ~/.gitignore
```

## Python package distribution (PyPi) 
Best instructions to follow: https://packaging.python.org/tutorials/packaging-projects/

First, aim to upload to test.pypi.org so that you're not using the real thing. 
 
1. Create a `setup.py` file that follows the instructions above. 
2. `python3 setup.py sdist bdist_wheel`
3. Then you can run `pip install .` to install locally and run a python interpreter to make sure all your modules load correctly. 
4. Create a test.pypi account and then upload to test.pypi with `python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*` 
5. With a virtualenv, you can then download the pip package you just uploaded `python3 -m pip install --index-url https://test.pypi.org/simple/ PACKAGE_NAME` (where `PACKAGE_NAME` matches what you put in your `setup.py`. 

Then upload to the real PyPi once you're satistified with the tests.

1. `twine upload dist/*`. 
2. Make sure it uploaded correctly with `pip install [PACKAGE-NAME]` and `https://pypi.org/project/PACKAGE-NAME/`. 

## Reddit Python API (PRAW) 
1. Create an account on Reddit. 
2. Follow these instructions https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example. You are a script type app. You will create an app on the Reddit site and then get a clientID and client secret.
3. Then you can query via substituting in the relative credentials  
```
import praw
reddit = praw.Reddit(
    username = my_username, 
    password = my_password, 
    client_id=my_client_id,
    client_secret=my_client_secret,
    user_agent='blah')
```

# Sublime on the command line 
Follow these insructions: https://ashleynolan.co.uk/blog/launching-sublime-from-the-terminal
In addition, I had to add to my `.bash_profile`: 
`alias subl=~/bin/subl` (or might also be `alias subl=~/bin/sublime`). 

# Twitter, Twint
Get Tweets w/o the api 
```
https://github.com/twintproject/twint
```

# Connecting iPad to Mac to use as a screen
Using Duet https://www.duetdisplay.com/ (have to buy the iPad app but the Mac download should be free) 

# iTerm2 (command line) 
Make it so that opening a new tab in the same folder
https://futurestud.io/tutorials/iterm-duplicate-a-tab-by-opening-a-new-tab-in-the-same-folder
```
CMD + SHIFT + t
```
