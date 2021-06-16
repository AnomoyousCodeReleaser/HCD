from setuptools import setup, find_packages


setup(name='HCD',
      version='1.0.0',
      description='Online Pseudo Label Generation by Hierarchical Cluster Dynamics for Adaptive Person Re-identification',
      install_requires=[
          'numpy', 'torch', 'torchvision',
          'six', 'h5py', 'Pillow', 'scipy',
          'scikit-learn', 'metric-learn', 'faiss-gpu==1.6.3'],
      packages=find_packages(),
      )
