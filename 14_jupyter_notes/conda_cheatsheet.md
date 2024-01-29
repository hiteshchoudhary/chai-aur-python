# conda cheatsheet

## Create a new environment
```bash
conda create --name myenv python=3.6
```

## Activate an environment

```bash
conda activate myenv
```

## Deactivate an environment

```bash
conda deactivate
```

## Delete an environment

```bash
conda remove --name myenv --all
```

## Install a package

```bash
conda install --name myenv numpy
```

## List all packages installed in an environment

```bash
conda list --name myenv
```

## List all environments

```bash
conda info --envs
```



