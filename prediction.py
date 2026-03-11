import pickle
import os
import re

USER_WEIGHT = 5

class Predict:
    def __init__(self, word):
        with open("model.pkl", "rb") as f:
            self.dictionary = pickle.load(f)

        # load user statistics (created/updated during usage)
        self.user_stats_file = "user_stats.pkl"
        if os.path.exists(self.user_stats_file):
            with open(self.user_stats_file, "rb") as f:
                self.user = pickle.load(f)
        else:
            self.user = {}
        # don't call predict here to avoid side effects

    def _normalize(self, w):
        """Lowercase and strip surrounding non-alphanumeric chars."""
        if not w:
            return ""
        w = w.lower()
        # remove leading/trailing non a-z0-9 characters
        return re.sub(r'^[^a-z0-9]+|[^a-z0-9]+$', '', w)

    def predict(self, word):
        word = self._normalize(word)

        train_next = self.dictionary.get(word, {})
        user_next = self.user.get(word, {})

        if not train_next and not user_next:
            return "No such word found", "No such word found"

        # combine counts, weighting user counts so personal preference can override training
        combined = {}
        for w, c in train_next.items():
            key = self._normalize(w)
            if not key:
                continue
            combined[key] = combined.get(key, 0) + c
        for w, c in user_next.items():
            key = self._normalize(w)
            if not key:
                continue
            combined[key] = combined.get(key, 0) + c * USER_WEIGHT

        sorted_words = sorted(
            combined.items(),
            key=lambda x: x[1],
            reverse=True
        )

        most_word = sorted_words[0][0] if len(sorted_words) > 0 else None
        second_word = sorted_words[1][0] if len(sorted_words) > 1 else None

        return most_word, second_word

    def update(self, prev_word, next_word):
        """Record a user-typed pair (prev_word -> next_word) and persist it."""
        prev = self._normalize(prev_word)
        nxt = self._normalize(next_word)
        if not prev or not nxt:
            return

        if prev not in self.user:
            self.user[prev] = {}
        if nxt not in self.user[prev]:
            self.user[prev][nxt] = 0
        self.user[prev][nxt] += 1

        with open(self.user_stats_file, "wb") as f:
            pickle.dump(self.user, f)