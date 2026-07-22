# Taiwanese Homophonic Toxicity Detection

An undergraduate research project (大專生專題) on detecting **phonetically-disguised toxic language** in Taiwanese internet Chinese — text that reads as harmless but sounds toxic when spoken aloud.

> 📄 Full write-up: [`docs/final_report.pdf`](docs/final_report.pdf) (Chinese, with English abstract)

## The Problem

Existing toxicity detectors (e.g. Perspective API) catch explicit insults, but Taiwanese online communities routinely evade them with **homophonic puns (諧音梗)**: the text looks neutral or even positive, but sounds like something offensive. For example:

| Text | Sounds like | Why semantic models miss it |
|---|---|---|
| 他真的很肚爛誒 | Taiwanese Hokkien for "annoyed/pissed off" | Reads as a normal, mildly odd sentence in Mandarin |
| 自鯊 | 自殺 (self-harm) | Common evasion of platform keyword filters |
| 這老師教學很有「精神」 | 精神病 (mental illness) | Reads as a compliment |

A model that only looks at word meaning (semantics) can't catch this — it needs to also "hear" the text.

## Approach

This project has two parts:

**1. Dataset construction via prompt engineering.** Since no existing corpus captures this phenomenon, ~23 seed examples were hand-collected from Taiwanese forums (PTT, Dcard) and used to bootstrap LLM-based data augmentation (ChatGPT + Gemini). A structured prompt (role + task definition + few-shot examples + explicit constraints + linguistic background) was iterated over several rounds — see `prompt/` and `prompt_test/`. This iteration mattered a lot: the share of generated samples that were *both* toxic *and* genuinely homophonic (as opposed to just generic negative text) went from **10% with a bare task description to 80%** with the full structured prompt.

**2. A phonetic-aware classifier.** Chinese characters, Taiwanese Hokkien readings, and English letters are all mapped into a shared Zhuyin → Tâi-lô romanization space, vectorized into a **pinyin embedding**, and fused (element-wise addition) with a pretrained language model's sequence embedding before a linear classification head. The idea: let the model use sound, not just meaning.

```
text ──┬─→ [semantic encoder: BERT / CKIP-BERT / RoBERTa] ─→ sequence embedding ─┐
       │                                                                         ├─→ fusion → classifier → toxic / not
       └─→ [phonetic mapping: Zhuyin → Tâi-lô → vector] ─→ pinyin embedding ─────┘
```

## Results

Adding the pinyin embedding improved every backbone tested, on a hand-labeled set of ~500 examples (400 train / 100 test, ~49/51 toxic split):

| Model | Precision | Recall | F1 |
|---|---|---|---|
| BERT (baseline) | .77 | .77 | .77 |
| BERT + pinyin embedding | .78 | .78 | .78 |
| CKIP-BERT | .79 | .78 | .78 |
| CKIP-BERT + pinyin embedding | .79 | .79 | .79 |
| RoBERTa | .79 | .79 | .79 |
| **RoBERTa + pinyin embedding** | **.81** | **.80** | **.80** |

RoBERTa + pinyin embedding performed best overall, likely because RoBERTa's stronger pretraining already gives it a better contextual base for the phonetic signal to build on.

## Repository Structure

```
├── data/                          # Cleaned, labeled datasets
│   ├── toxic_dataset.csv / toxic_dataset_cleaned.csv
│   ├── combined_pun_nonpun.csv
│   └── punes_list_clean.csv (+ _test split)
├── prompt/                        # Prompt engineering
│   ├── prep_prompt.txt            # Concept-teaching stage (few-shot priming)
│   ├── prompt.txt                 # Final structured generation prompt
│   └── generated_toxic_dataset.txt
├── prompt_test/                   # Prompt iteration rounds (1-5), ChatGPT vs. Gemini output
├── random_pick.py                 # Seed examples with annotated pun logic
├── toxic_dataset_cleaned.py       # Dataset cleaning script
├── baseline.ipynb                 # Semantic-only: BERT
├── baseline_ckip.ipynb            # Semantic-only: CKIP-BERT
├── baseline_roberta.ipynb         # Semantic-only: RoBERTa
├── toxic_classifier.ipynb         # + pinyin embedding: BERT
├── toxic_classifier_ckip.ipynb    # + pinyin embedding: CKIP-BERT
├── toxic_classifier_roberta.ipynb # + pinyin embedding: RoBERTa
├── toxic_classifier_normal_embedding.ipynb  # ablation: plain (non-phonetic) embedding
└── docs/final_report.pdf          # Full report (methodology, related work, limitations)
```

`baseline_*` notebooks are the semantic-only models; `toxic_classifier_*` notebooks add the pinyin embedding fusion described above. Notebooks were built to run on Google Colab.

## Setup

```bash
pip install -r requirements.txt
```

Then open any notebook in Jupyter or Colab. Each notebook is self-contained: data preprocessing → model definition → training → inference.

## Limitations

- Dataset is small (~500 labeled examples), so performance differences between models are not yet fully separable.
- Phonetic representation currently covers Mandarin, Hokkien, and English-letter puns via Tâi-lô romanization, but not numeric puns (e.g. 1314520) or emoji-based evasion.
- Corpus skews toward Mandarin/Hokkien puns; other language mixes are underrepresented.

See `docs/final_report.pdf` §5-6 for the full discussion and proposed next steps.
