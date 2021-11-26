# TextOCR 성능 검증을 위한 PerformanceTester
***
* 원본 소스: <https://github.com/clovaai/deep-text-recognition-benchmark>
***


## 사용법
### 1. 프로그램 실행을 위해 필요한 라이브러리를 설치합니다.
Pycharm의 Terminal에 아래의 내용을 입력합니다. 

    pip install -r requirements.txt

### 2. 평가에 사용될 이미지 데이터와 그에 대한 정답값을 <test_dataset> 폴더에서 확인합니다.
test_dataset/class -> 36,305개의 텍스트 이미지 파일 

test_dataset/gt.txt -> <test_dataset/class>에 저장된 이미지 파일에 대한 정답값

### 3. <test_dataset>의 파일을 검증을 위한 lmdb형식으로 변환합니다.

3-1. Pycharm의 Terminal에 아래의 내용을 입력합니다. 
        
    python create_lmdb_dataset.py --inputPath ./test_dataset/class/ --gtFile ./test_dataset/gt.txt --outputPath ./test_lmdb

3-1. lmdb형식으로 변환된 파일은 <test_lmdb> 폴더에 저장됩니다.

<test_lmdb> 폴더 안에는 data.mdb 와 lobk.mdb 총 2개의 파일이 저장되어 있습니다.

### 4. 변환된 lmdb 파일로 평가할 모델의 성능을 검사합니다.

4-1.Pycharm의 Terminal에 아래의 내용을 입력합니다. 
        
    python test.py --eval_data "./test_lmdb" --Transformation None --FeatureExtraction VGG --SequenceModeling BiLSTM --Prediction CTC --input_channel 1 --output_channel 256 --hidden_size 256 --saved_model "./model/best_accuracy.pth"

4-2. Terminal에서 평가 진행상황을 확인 할 수 있습니다.

    예)
         --------------------------------------------------------------------------------
          Ground Truth              | Prediction                | Confidence Score & T/F
         --------------------------------------------------------------------------------
          그녀의 노래는 정말 감동적이다          | 그녀의 노래는 정말 감동적이다          | 0.7454        True
         --------------------------------------------------------------------------------

4-3. 평가를 마치게 되면 Terminal에 해당 모델의 성능이 백분율로 반환됩니다.

    예)
         --------------------------------------------------------------------------------
          Ground Truth              | Prediction                | Confidence Score & T/F
         --------------------------------------------------------------------------------
          우리는 배고파서 거의 정신을 잃을 정도이다   | 우리는 네고과서 거의 정신운 싫을 정도다    | 0.0504       False
         --------------------------------------------------------------------------------
         성능:  73.561

### 5. 모델의 평가된 성능을 <result> 폴더에서 확인합니다.
<result/model_best_accuracy.pth> 폴더 안에는 log_evaluation.txt 와 log_testdata_detail.txt 총 2개의 파일이 저장되어 있습니다.

5-1. <log_evaluation.txt>에서 모델의 성능을 확인할 수 있습니다.

         예) log_evaluation.txt

         dataset_root:    ./test_lmdb	 dataset: /
         sub-directory:	/.	 num samples: 27775
         성능: 73.561     <<< 모델의 예측값과 정답값이 일치한 정도에 대한 백분율

5-2. <log_testdata_detail.txt>에서 이미지 파일에 대한 정답값, 모델의 예측값, 정답여부를 확인 할 수 있습니다.

         예)
         ------------------------------------------------------------------------------
         Ground Truth              | Prediction                | Confidence Score & T/F
         ------------------------------------------------------------------------------
         행해지                       | 행해지                       | 0.9998	True
         ------------------------------------------------------------------------------