## 📢 Recent Updates

### 2026-06-01
* **Standalone EXE Support**: Released a pre-compiled Windows executable (`.exe`). Users can now run the tool instantly without installing Python or any dependencies.
* **Background Mode Optimization**: Configured the executable to run silently in the background, completely removing the persistent CMD/terminal window for a cleaner user experience.

### 2026-05-31
* **Sentence-Boundary Separation**: Upgraded training algorithm to isolate sentences by `\n`, completely preventing cross-sentence word contamination.
* **Conversational Corpus**: Replaced the baseline text with a highly natural, casual English dataset for better everyday predictions.

*For full version history and bug fixes, check out our detailed [CHANGELOG.md](./CHANGELOG.md).*
---

#### Predictive AI typing tool
## Quick Start

1. Download all files
2. Click main.exe to run


## How to Use

1. Start typing in the text area.
2. After you type a space or punctuation mark, a predicted next word will appear in **grey**.
3. Press **Tab** to accept the prediction and continue typing.
4. Press **Backspace**, **Delete**, or move the cursor to dismiss the prediction.

---

## Features

- Real-time next-word prediction triggered by spaces and punctuation
- Predictions displayed in grey for visual distinction
- **Tab** to accept; any editing key dismisses the suggestion
- Learns from your writing — accepted and typed word pairs are saved and weighted more heavily than the base training data
- Modular design: prediction logic is fully separated from the GUI

---

## Project Structure

```
typing_ai/
├── main.py               # GUI entry point (Tkinter)
├── main.exe               # Click to run
├── prediction.py         # Prediction logic (loads model, returns candidates)
├── type_ai.py            # Builds word-frequency dictionary from training text
├── ai_model.py           # Run once to generate model.pkl from training_content.txt
├── training_content.txt  # Training corpus (can be customized — see below)
├── model.pkl             # Serialized n-gram model (auto-generated)
├── user_stats.pkl        # Saved user writing patterns (auto-generated, not in default code)
└── README.md             # This file
```

---

## Customizing the Training Data

The prediction model is built from `training_content.txt`.  
To use your own training data:

1. Replace the content in `training_content.txt` with your preferred text corpus.
2. Delete the existing `model.pkl`.
3. Re-run:
```bash
python ai_model.py
```

The new `model.pkl` will reflect your custom corpus.

---

## How Prediction Works

- The model is an **n-gram frequency table**: for each word, it stores how often each other word follows it in the training corpus.
- When you finish typing a word, the tool looks up the most and second-most frequent following words and displays the top candidate.
- User preferences are stored separately in `user_stats.pkl` and are weighted **5× more** than the base training data, so your personal writing style gradually takes priority over the default model.

---

## Dependencies

Python 3.x — standard library only (`tkinter`, `pickle`, `os`, `re`)  
No external packages required.

---

## Known Limitations

- Predictions only trigger at the end of the document (cursor must be at the end).
- The model predicts one word at a time; multi-word suggestions are not supported yet.
- Prediction quality depends on how closely the training corpus matches your writing style. Customizing `training_content.txt` is recommended for best results.
