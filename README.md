
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


