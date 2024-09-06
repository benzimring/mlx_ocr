# mlx_ocr

## Install
1. Download the [model](https://huggingface.co/Norm/nougat-latex-base)
   ```shell
   git lfs install
   git clone https://huggingface.co/Norm/nougat-latex-base
   ```
2. if you use a virtual env (recommended), activate it, then:
   ```shell
   pip cache purge
   pip install --upgrade pip setuptools wheel
   pip install .
   ```
3. `mlx_ocr --help`

## Cleanup
```shell
# if using venv run the following, otherwise idk
pip cache purge
deactivate
rm -rf ./.venv
```