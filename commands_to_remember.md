# Commands to remember
Katherine Keith 

## Latex 

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
\begin{table}[t]
  \centering
      \begin{tabular}{lll}
      \toprule
      Relation         & Yes   & No    \\
      \toprule
      Institution      & 27045 & 15579 \\
      Place of birth   & 6992  & 2574 
  \end{tabular}
  \caption{XXX  \label{t:XXX}}
\end{table}
```


## Python

### Boilerplate 
```
if __name__ == '__main__':
  main()
```

### Argparse 
```
parser = argparse.ArgumentParser()
parser.add_argument("input", help=".json file", type=str)
args = parser.parse_args()
```

### Dictionaries 
```
#sorts by largest value 
sorted(d.items(), key=lambda (k, v): -v)

#default dict of a default dict 
defaultdict(lambda : defaultdict(int))
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
### Other 
Write to standard error when loading big files
```
sys.stderr.write(".")
```

## Jupyter notebook 

```
#covert jupyter to .py file 
jupyter nbconvert --to script 1idvl.ipynb
```

### Using virtualenv within a jupyter notebook 

http://help.pythonanywhere.com/pages/IPythonNotebookVirtualenvs
In a Jupyter notebook 

Kernel -> Change kernel 

### Auto-reloading Jupyter Notebook 
```
%load_ext autoreload
%autoreload 2
```

## Linux/Unix 

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

### Using a GUI on a remote server
https://www.macissues.com/2014/10/13/how-to-mount-a-remote-system-as-a-drive-using-ssh-in-os-x/
```
sshfs kkeith@hobbes.cs.umass.edu:/home/kkeith/ ~/mount/
umount -f ~/mount/
```
