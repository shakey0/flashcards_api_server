class FlashcardSet:
    
    def __init__(self, id, name, emoji, previous_score, theme_color, user_id, flashcards=[]):
        self.id = id
        self.name = name
        self.emoji = emoji
        self.previous_score = previous_score
        self.theme_color = theme_color
        self.user_id = user_id
        self.flashcards = flashcards
        
    def __eq__(self, other):
        self.__dict__ == other.__dict__

    def __repr__(self):
        return f"<FlashcardSet {self.id} {self.name} {self.emoji} {self.previous_score} {self.theme_color} {self.user_id}>"
