from transformers import T5Tokenizer, T5ForConditionalGeneration

model = T5ForConditionalGeneration.from_pretrained("model_24")
tokenizer = T5Tokenizer.from_pretrained("t5-small")
text = 'The warning Weights from XXX not initialized from pretrained model means that the weights of XXX do not come pretrained with the rest of the model. It is up to you to train those weights with a downstream fine-tuning task.'
# text="Many people were drowned when the ship hit the big rock and went down the ocean."
input_ids = tokenizer.encode(text, return_tensors = 'pt')
generated_ids = model.generate(input_ids, num_beams = 2, max_length = 400, repetition_penalty = 2.5, length_penalty = 1.0, early_stopping = True)
preds = [tokenizer.decode(i, skip_special_tokens = True, clean_up_tokenization_spaces = True) for i in generated_ids]
# print(text)
print()
print(preds[0][2:])
