from distutils.core import setup 
from version import __version__ 
url = "https://github.com/iremdgnc/Raf" 
version = __version__

setup(name="Raf", 
      version=version, # versiyonu
      description="Operations are carried out according to the user's request."
      long_description="From the drop-down menu, the user selects the desired operation."
      author="iremdgnc", # yazar
      url="https://github.com/iremdgnc/Raf", # linki
      license='MIT', # lisansi
      # download_url=url+"/archive/"+version+".tar.gz", # Tagging konusunda daha sonra deginecegiz
      author_email="sddkacil.1@gmail.com", # e-posta
      classifiers=[
          'Development Status :: 0.1.1 - Development/Developmental Release',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ], # bu kisim indeksler tarafindan siniflandirmak amaciyla kullanilir.
      packages=["."] # sunulan paketlerin listesi find_packages komutuyla otomatize edilebilir.
      )
