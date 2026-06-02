##  - 2026-05-24
### [Bug Fixes]
* **Backspace Validation**: Fixed an issue where pressing `Backspace` would mistakenly trigger the acceptance of the grey predicted word. The text lifecycle has been corrected so that any deletion key (`Backspace`/`Delete`) now properly rejects and dismisses the current prediction as intended.

---

## - 2026-05-31
### [New Features]
* **Sentence-Boundary Separation**: Upgraded the training algorithm to split the corpus strictly by paragraph or line breaks (`\n`) before mapping. This prevents the system from wrongly recording and linking unrelated words between the end of one sentence and the beginning of the next.

### [Updates]
* **Conversational Corpus**: Replaced the baseline training text with a highly casual, everyday English speech dataset to make predictions feel much more natural for daily conversations.

---
## - 2026-06-01
### [New Features]
* **Standalone Executable Deployment**: Added support for cross-platform independent distribution. Windows users can now run the tool natively using a pre-compiled `.exe` file without installing Python or configuring local dependencies.

### [Updates]
* **Background Process Integration (--noconsole)**: Configured the production executable to run as a silent background process. The persistent terminal/CMD window has been completely eliminated, providing a seamless and non-intrusive desktop user experience.
* **Workspace Clean-up Optimization**: Refactored the build pipeline to decouple source code from intermediate compilation artifacts. Build caches (`build/` directories and `.spec` configuration files) are now strictly isolated from production binaries to maintain a clean repository footprint.
