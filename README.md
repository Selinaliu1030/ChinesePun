# ChineseBERT Pun Detection Model

This project implements a ChineseBERT-based model for detecting puns in Chinese text. It includes pretraining/fine-tuning and inference capabilities.

## Project Structure

```
ChinesePun/
├── data/                      # Training data
│   └── sample_training_data.csv
├── models/                    # Trained models will be saved here
├── scripts/                   # Helper scripts
│   ├── train.sh
│   └── inference.sh
├── data_loader.py            # Data loading utilities
├── pretrain.py               # Training script
├── inference.py              # Inference script
├── requirements.txt          # Python dependencies
└── README.md
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare Training Data

Your training data should be in CSV or JSON format:

**CSV Format:**
```csv
text,label
这是一个有趣的双关语,1
这是普通的句子,0
```

**JSON Format:**
```json
[
  {"text": "这是一个有趣的双关语", "label": 1},
  {"text": "这是普通的句子", "label": 0}
]
```

- `text`: The Chinese text to analyze
- `label`: 1 for pun, 0 for no pun

## Usage

### Training

1. **Basic Training:**
```bash
python pretrain.py --data_path ./data/sample_training_data.csv
```

2. **Custom Configuration:**
```bash
python pretrain.py \
    --data_path ./data/training_data.csv \
    --output_dir ./models \
    --batch_size 32 \
    --num_epochs 5 \
    --learning_rate 3e-5 \
    --max_length 256
```

3. **Using the training script:**
```bash
bash scripts/train.sh
```

#### Training Arguments:
- `--data_path`: Path to training data (CSV or JSON) [required]
- `--model_name`: Pretrained model name (default: 'hfl/chinese-bert-wwm-ext')
- `--batch_size`: Batch size for training (default: 16)
- `--num_epochs`: Number of training epochs (default: 3)
- `--learning_rate`: Learning rate (default: 2e-5)
- `--max_length`: Maximum sequence length (default: 128)
- `--train_ratio`: Train/validation split ratio (default: 0.8)
- `--output_dir`: Directory to save models (default: './models')
- `--text_column`: Column name for text in CSV (default: 'text')
- `--label_column`: Column name for label in CSV (default: 'label')

### Inference

1. **Single Text:**
```bash
python inference.py \
    --model_path ./models/best_model \
    --text "这是一个有趣的双关语"
```

2. **From File (one text per line):**
```bash
python inference.py \
    --model_path ./models/best_model \
    --input_file ./data/test_texts.txt \
    --output_file ./results.json
```

3. **From JSON File:**
```bash
python inference.py \
    --model_path ./models/best_model \
    --json_input ./data/test_data.json \
    --output_file ./results.json
```

#### Inference Arguments:
- `--model_path`: Path to trained model directory [required]
- `--text`: Single text to analyze
- `--input_file`: File with texts (one per line)
- `--json_input`: JSON file with texts
- `--output_file`: File to save results (optional)

### Output Format

Inference returns results in the following format:

```json
{
  "text": "这是一个有趣的双关语",
  "has_pun": true,
  "confidence": 0.95,
  "pun_probability": 0.95,
  "no_pun_probability": 0.05
}
```

## Models

### Available Pretrained Models:
- `hfl/chinese-bert-wwm-ext` (default): Chinese BERT with Whole Word Masking
- `hfl/chinese-roberta-wwm-ext`: Chinese RoBERTa with Whole Word Masking
- `bert-base-chinese`: Official BERT Chinese Model

## Python API

You can also use the model programmatically:

```python
from inference import PunDetector

# Initialize detector
detector = PunDetector('./models/best_model')

# Single prediction
result = detector.predict("这是一个有趣的双关语")
print(f"Has pun: {result['has_pun']}")
print(f"Confidence: {result['confidence']}")

# Batch prediction
results = detector.predict_batch([
    "这是一个有趣的双关语",
    "这是普通的句子"
])
```

## Training Tips

1. **Data Quality**: Ensure your training data is well-labeled and diverse
2. **Data Size**: For best results, use at least 500-1000 labeled examples
3. **Batch Size**: Use larger batch sizes if GPU memory allows (32, 64)
4. **Learning Rate**: For fine-tuning BERT, 2e-5 to 5e-5 is typically good
5. **Epochs**: 3-5 epochs is usually sufficient for fine-tuning

## Performance Optimization

- Use GPU for faster training: `torch.cuda.is_available()`
- Reduce `max_length` if memory is limited
- Use mixed precision training for faster computation
- Increase `batch_size` for better GPU utilization

## Troubleshooting

1. **Out of Memory**: Reduce `batch_size` or `max_length`
2. **Low Accuracy**: Check data quality and increase training data size
3. **Slow Training**: Use GPU and increase `batch_size`
4. **Model Not Found**: Ensure model path is correct and model files are present

## References

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Chinese BERT Models](https://github.com/ymcui/Chinese-BERT-wwm)
- [PyTorch Documentation](https://pytorch.org/docs/)

## License

MIT License

## Contact

For issues or questions, please open an issue on GitHub.
