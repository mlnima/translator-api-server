from transformers import M2M100Tokenizer, M2M100ForConditionalGeneration
import os


class TranslationModel:
    def __init__(self):
        model_name = "facebook/m2m100_418M"
        self.tokenizer = M2M100Tokenizer.from_pretrained(model_name)
        self.model = M2M100ForConditionalGeneration.from_pretrained(model_name, cache_dir="./models")

    def translate_text(self, text, target_language):
        encoded_text = self.tokenizer(text, return_tensors="pt")
        generated_tokens = self.model.generate(**encoded_text,
                                               forced_bos_token_id=self.tokenizer.get_lang_id(target_language))
        return self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
