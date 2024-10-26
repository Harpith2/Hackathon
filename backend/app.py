from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize the model with correct parameters
try:
    generator = pipeline(
        "text-generation",
        model="gpt2",
        temperature=0.8,
        top_k=50,
        do_sample=True,
        max_new_tokens=30  # Limit to concise outputs
    )
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    generator = None

@app.route('/generate_prompt', methods=['POST'])
def generate_prompt():
    try:
        if generator:
            base_prompt = "Generate a unique, specific memory recall question about a person's past event."

            # Generate a question using the model
            generated = generator(
                base_prompt,
                max_new_tokens=30,  # Keep it concise
                num_return_sequences=1,
                temperature=0.8,  # Adjusted temperature for creativity
                top_k=50,
                clean_up_tokenization_spaces=True
            )

            # Extract the generated text
            question = generated[0]['generated_text'].strip()

            # Post-process the generated question
            question = question.replace(base_prompt, '').strip()

            # Ensure it is a single question ending with a question mark
            question = question.split('\n')[0].strip()  # Take only the first line
            if not question.endswith('?'):
                question += '?'

            return jsonify({'prompt': question})
        else:
            return jsonify({'prompt': "Please recall a memory."})
    except Exception as e:
        print(f"Error during generation: {e}")
        return jsonify({'prompt': "Please recall a memory."})

if __name__ == '__main__':
    app.run(debug=True)
