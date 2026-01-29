#!/usr/local/bin/bash
#rm -rf index_files
#rm -rf docs
#rm -rf tikz-tex
quarto render --profile makepdf
quarto render --profile makehtml
cp -r ../arabic-tutorial-book/srchtml/fonts docs/
