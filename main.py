import tkinter as tk
from prediction import Predict


class Main():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing AI")

        #the prediction module
        self.predictor = Predict("")   

        #current word being predicting
        self.prediction = ""           
        self.predict_start = None   

        #length of content being predicted (for easy deletion if user keeps typing instead of accepting)  
        self.prediction_len = 0        
        self.suppress_next_release = False 

        #track last word for user-updates
        self.last_word = None          

        self.text = tk.Text(self.root, font=("Consolas", 14), wrap="word")
        self.text.pack(expand=True, fill="both")

        #grey tag for the next word prediction
        self.text.tag_config("predict", foreground="light grey")

        # binding keyboard actoin with methods actions
        self.text.bind("<KeyRelease>", self.on_key_release)
        self.text.bind("<Tab>", self.accept_prediction)

        self.root.mainloop()

    def clear_prediction(self):
        """clear the predicting word"""
        if self.prediction and self.predict_start:
            start = self.predict_start
            end = f"{start} + {self.prediction_len} chars"
            try:
                existing = self.text.get(start, end)
                if existing == self.prediction:
                    self.text.delete(start, end)
            except tk.TclError:
                pass

        self.text.tag_remove("predict", "1.0", "end")
        self.prediction = ""
        self.predict_start = None
        self.prediction_len = 0

    def on_key_release(self, event):
        if self.suppress_next_release:
            self.suppress_next_release = False
            return

        if self.text.index("insert") != self.text.index("end-1c"):
 
            self.clear_prediction()
            return


        if event.keysym in ("BackSpace", "Delete", "Left", "Right", "Up", "Down", "Home", "End"):
            self.clear_prediction()
            return


        if event.char and event.char.isalnum():
            self.clear_prediction()
            return


        if event.keysym == "Tab":
            return

        trigger_chars = [" ", ".", ",", "!", "?", ";", ":"]
        if not event.char or event.char not in trigger_chars:
            return

        self.clear_prediction()

        content = self.text.get("1.0", "end-1c")
        words = content.split()
        if not words:
            return

        # If the user has just completed a pair like "hello world ", record it:
        if len(words) >= 2:
            prev_word = words[-2]
            curr_word = words[-1]
            try:
                self.predictor.update(prev_word, curr_word)
            except Exception:
                # keep UI stable if update fails
                pass

        last_word = words[-1]
        self.last_word = last_word    # remember for accept_prediction updates
   
        most, second_most = self.predictor.predict(last_word)

        candidate = (most or "").strip() or (second_most or "").strip()
        if not candidate:
            return

        self.predict_start = self.text.index("end-1c")
        self.text.insert("end", candidate, "predict")
        self.prediction = candidate
        self.prediction_len = len(candidate)

    def accept_prediction(self, event):
        """Click tab to accept the grey word"""
        if not self.prediction or not self.predict_start:
            return "break" 

        p = self.prediction
        start = self.predict_start
        end = f"{start} + {self.prediction_len} chars"

        try:
            existing = self.text.get(start, end)
        except tk.TclError:
            existing = ""

        if existing == p:
            self.text.delete(start, end)
            self.text.insert(start, p)
            new_insert = f"{start} + {len(p)} chars"
            try:
                self.text.mark_set("insert", new_insert)
            except tk.TclError:
                self.text.mark_set("insert", "end-1c")
        else:
            self.text.insert("end", p)
            self.text.mark_set("insert", "end-1c")

        # record user's acceptance as preference for previous word to this word
        try:
            if self.last_word:
                self.predictor.update(self.last_word, p)
        except Exception:
            pass

        self.prediction = ""
        self.predict_start = None
        self.prediction_len = 0
        self.text.tag_remove("predict", "1.0", "end")
        self.suppress_next_release = True

        return "break"  


if __name__ == "__main__":
    main = Main()