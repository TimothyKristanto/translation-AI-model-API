from easynmt import EasyNMT

model = EasyNMT("opus-mt")

def translate(sentence, tgt_lang, src_lang=None):
    return model.translate(sentence, target_lang=tgt_lang, source_lang=src_lang)