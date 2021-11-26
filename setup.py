from setuptools import setup, find_packages

with open('requirements.txt', encoding="utf-8-sig") as f:
    requirements = f.readlines()

setup(
    name             = 'NIA-image2text',
    version          = '1.4.0',
    description      = 'End-to-End Multi-Lingual Optical Character Recognition (OCR) Solution',
    author           = 'SangJun Kim',
    author_email     = 'weareyoyo12@naver.com',
    url              = 'https://github.com/SANGJUN12-KIM/NIA_textOCR.git',
    download_url     = '',
    install_requires = requirements,
    packages         = find_packages(),
    keywords         = ['image2text', 'ocr'],
    python_requires  = '>=3',
    package_data     = {'easyocr': ['user_network/custom.pth','user_network/custom.py', 'user_network/custom.yaml'],
                        'PnuNlp': ['./_PnuNlp_Py.so']},
    include_package_data=True,
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ]
)