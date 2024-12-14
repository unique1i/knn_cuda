import os
from setuptools import setup, find_packages

version = {}
with open("knn_cuda/version.py") as fp:
    exec(fp.read(), version)

with open('requirements.txt') as f:
    required = f.read().splitlines()

os.environ["TORCH_CUDA_ARCH_LIST"] = "5.0;6.0;6.1;6.2;7.0;7.5;8.0;8.6;8.9;9.0"
setup(
    name='KNN_CUDA',
    version=__version__,
    description='pytorch version knn support cuda.',
    author='Shuaipeng Li',
    author_email='sli@mail.bnu.edu.cn',
    packages=find_packages(),
    package_data={
        'knn_cuda': ["csrc/cuda/knn.cu", "csrc/cuda/knn.cpp"]
    },  
    install_requires=required
)

