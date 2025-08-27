# lbl-spack-pkgs

Custom spack packages mostly for LBL HPCS usage. Currently, there is one 
package repository called `llm_packages`.

To use this package repository:

``` bash
spack repo add --name llm_packages https://github.com/saroj-lbl/lbl-spack-pkgs.git
```

which will add the following to your `~/.spack/repos.yaml` or to your environments `spack.yaml`

``` yaml
repos:
  llm_packages:
    git: https://github.com/saroj-lbl/lbl-spack-pkgs.git
```