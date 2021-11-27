#!/bin/bash

echo SVM Primal SGD
python3 SVM.py primal
echo ____________________________
echo SVM Dual
python3 SVM.py dual
echo ____________________________
echo SVM Kernel
python3 SVM.py kernal