export BERT_BASE_DIR=/Users⁩/MaiSha⁩/Documents⁩/chinese_L-12_H-768_A-12
export GLUE_DIR=/⁨Users⁩/⁨MaiSha⁩/⁨Documents/download_glue_data.py⁩
export TRAINED_CLASSIFIER=/Users⁩/MaiSha⁩/Documents⁩/output


python run_classifier.py \
  --task_name=MRPC \
  --do_predict=true \
  --data_dir=$GLUE_DIR/MRPC \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$TRAINED_CLASSIFIER \
  --max_seq_length=128 \
  --output_dir=/tmp/mrpc_output/