# mlx_ocr

## Install
1. Download the [model](https://huggingface.co/Norm/nougat-latex-base)
   ```shell
   git lfs install
   git clone https://huggingface.co/Norm/nougat-latex-base
   ```
2. Install `imagemagick`
   ```shell
   brew install imagemagick
   export MAGICK_HOME=$(brew --prefix imagemagick)
   export PATH=$MAGICK_HOME/bin:$PATH
   export DYLD_LIBRARY_PATH=$MAGICK_HOME/lib:$DYLD_LIBRARY_PATH
   ```
3. if you use a virtual env (recommended), activate it, then:
   ```shell
   pip cache purge
   pip install --upgrade pip setuptools wheel
   pip install .
   ```
4. `mlx_ocr --help`

## Cleanup
```shell
brew uninstall imagemagick
brew autoremove
brew cleanup --prune=all

# if using venv run the following, otherwise idk
pip cache purge
deactivate
rm -rf ./.venv
```