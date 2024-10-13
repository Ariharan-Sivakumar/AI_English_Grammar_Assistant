from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline, AutoModelForQuestionAnswering
import errant

app = Flask(__name__)
CORS(app)

class Gramformer:
    def __init__(self, models=1, use_gpu=False):
        self.annotator = errant.load('en')
        self.device = "cuda:0" if use_gpu else "cpu"
        correction_model_tag = "prithivida/grammar_error_correcter_v1"
        self.model_loaded = False

        if models == 1:
            self.correction_tokenizer = AutoTokenizer.from_pretrained(correction_model_tag)
            self.correction_model = AutoModelForSeq2SeqLM.from_pretrained(correction_model_tag)
            self.correction_model = self.correction_model.to(self.device)
            self.model_loaded = True
            print("[Gramformer] Grammar error correct/highlight model loaded..")
        elif models == 2:
            print("TO BE IMPLEMENTED!!!")

    def correct(self, input_sentence, max_candidates=1):
        print(f"Input to correct: {input_sentence}") 
        if self.model_loaded:
            correction_prefix = "gec: "
            input_sentence = correction_prefix + input_sentence
            input_ids = self.correction_tokenizer.encode(input_sentence, return_tensors='pt')
            input_ids = input_ids.to(self.device)

            preds = self.correction_model.generate(
                input_ids,
                do_sample=True,
                max_length=128,
                num_beams=7,
                early_stopping=True,
                num_return_sequences=max_candidates)

            corrected = set()
            for pred in preds:
                corrected.add(self.correction_tokenizer.decode(pred, skip_special_tokens=True).strip())
            return corrected
        else:
            print("Model is not loaded")
            return None

gf = Gramformer(models=1, use_gpu=False)

# Load context from a file
with open('context.txt', 'r', encoding='utf-8') as file:
    context = file.read()

qa_tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
qa_model = AutoModelForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
qa_pipeline = pipeline('question-answering', model=qa_model, tokenizer=qa_tokenizer)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/correct', methods=['POST']) #link
def correct():
    data = request.json
    sentence = data['sentence']
    corrected_sentences = gf.correct(sentence, max_candidates=1)
    return jsonify(list(corrected_sentences))

@app.route('/answer', methods=['POST'])
def answer():
    data = request.json
    question = data['question']
    answer = qa_pipeline(question=question, context=context)
    return jsonify(answer)

#if __name__ == '__main__':
   # app.run(debug=True)
if __name__ == '__main__':
    app.run(port=5001, debug=True) 