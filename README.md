# TextOCR for NIA-solution_for_social_issue
***
* 원본 소스: <https://github.com/JaidedAI/EasyOCR>
***

***
## 변경사항

##설치
- python 개발환경은 3.8.5입니다.
```python
conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
pip3 install lmdb pillow torchvision nltk natsort


```
## 사용법

```python
from image2text import ocrModelConfig
from image2text import image2text_origin

reader = ocrModelConfig.model(custom_model=False)
# custom_model = bool    -> 커스텀 모델의 사용 여부(default: False), 현재 기능 고도화 중

  ```

```python
from image2text import ocrModelConfig
from image2text import image2text_origin

reader = ocrModelConfig.model()
image2text_origin.convert(reader, input_dir='./target_pages/', json_output_dir='./OCRresult', paragraph=False,
                          spell_check=False)
# image_dir = 'str'            -> 변환할 복수의 이미지가 저장된 디렉토리, 변환할 단일 이미지의 경로(default: './target_pages/')
# json_output_dir = 'str'      -> 변환된 json 파일이 저장될 디렉토리(default: './OCRresult')
# paragraph = bool             -> 텍스트 단락 단위의 ocr 적용 여부(dafault=False)
# spell_check = bool           -> 추출된 텍스트 내용에 대한 맞춤법검사 적용여부
```

```python
from image2text import ocrModelConfig
from image2text import image2text_origin

reader = ocrModelConfig.model()
image2text_origin.read_text_area(reader, input_file='./target_pages/0001.jpg', spell_check=False)
# input_file = 'str'        -> 변환할 단일 이미지의 경로
# spell_check = bool        -> 추출된 텍스트 내용에 대한 맞춤법검사 적용여부
``` 

```python
from image2text import ocrModelConfig
from image2text import image2text_origin

reader = ocrModelConfig.model()
image2text_origin.conv2txt(reader, input_dir='./target_pages/0001.jpg', txt_output_dir='./OCRresultTXT',
                           spell_check=False))
# input_dir = 'str'        -> 변환할 다수의 이미지가 저장된 디렉토리 경로
# txt_output_dir = 'str'   -> 변환된 txt 파일이 저장될 디렉토리(default: './OCRresultTXT')
# spell_check = bool       -> 추출된 텍스트 내용에 대한 맞춤법검사 적용여부
```