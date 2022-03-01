
# nbRunner
Fast JupyterNotebook Runner

[![PyPI version](https://badge.fury.io/py/nbRunner.svg)](https://badge.fury.io/py/nbRunner)

Examples

```
$ nbRunner 
usage: nbRunner Notebook
nbRunner: error: the following arguments are required: Notebook


$ nbRunner examples/nounVerb.ipynb 
Default does the Default


$ nbRunner examples/nounVerb.ipynb  --help
usage: nbRunner [-h] [--who [WHO]] [--verb [VERB]]

optional arguments:
  -h, --help     show this help message and exit
  --who [WHO]
  --verb [VERB]


$ nbRunner examples/nounVerb.ipynb --who=Billy --verb=knocked
Billy knocked



```

```
$ time nbRunner examples/nounVerb.ipynb 
Default does the Default

real  0m1.637s
user  0m1.253s
sys 0m0.146s


$ time jupyter nbconvert --to notebook --execute examples/nounVerb.ipynb 
[NbConvertApp] Converting notebook examples/nounVerb.ipynb to notebook
[NbConvertApp] Writing 2014 bytes to examples/nounVerb.nbconvert.ipynb

real  0m2.227s
user  0m1.507s
sys 0m0.178s


$ time nbRunner examples/nounVerb.ipynb 
Default does the Default

real  0m1.922s
user  0m1.205s
sys 0m0.171s



$ time jupyter nbconvert --to notebook --execute examples/nounVerb.ipynb 
[NbConvertApp] Converting notebook examples/nounVerb.ipynb to notebook
[NbConvertApp] Writing 2014 bytes to examples/nounVerb.nbconvert.ipynb

real  0m2.072s
user  0m1.461s
sys 0m0.177s


```