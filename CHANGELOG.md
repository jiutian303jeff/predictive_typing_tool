## [1.1.0] - 2026-05-24
### [Bug Fixes]
* **Backspace Validation**: Fixed an issue where pressing `Backspace` would mistakenly trigger the acceptance of the grey predicted word. The text lifecycle has been corrected so that any deletion key (`Backspace`/`Delete`) now properly rejects and dismisses the current prediction as intended.

---

## [2.0.0] - 2026-05-31
### [New Features]
* **Sentence-Boundary Separation**: Upgraded the training algorithm to split the corpus strictly by paragraph or line breaks (`\n`) before mapping. This prevents the system from wrongly recording and linking unrelated words between the end of one sentence and the beginning of the next.

### [Updates]
* **Conversational Corpus**: Replaced the baseline training text with a highly casual, everyday English speech dataset to make predictions feel much more natural for daily conversations.


