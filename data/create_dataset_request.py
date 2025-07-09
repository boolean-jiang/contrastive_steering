import argparse
import os
import json
from tqdm import tqdm

from utils import CORRECT_PROMPT, INCORRECT_PROMPT, GSM8K_DESCRIPTION

# TODO: Build async openai method for generating samples 
def generate_question_queries(
    question: str,
    question_id: int,
    model: str = "o4-mini",
    temperature: float = 0.3,
    num_responses: int = 10, # Number of correct and incorrect samples each to generate - 2 * num_responses total responses
    dataset: str = "gsm8k",
):
    queries = [
        {
            "custom_id": f"{dataset}-{question_id}-correct-{index+1}",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": model,
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {
                        "role": "user", 
                        "content": CORRECT_PROMPT.substitute(dataset=dataset, dataset_description=GSM8K_DESCRIPTION, question=question)
                    }
                ]
            }
        }
        for index in range(num_responses)
    ] + [
        {
            "custom_id": f"{dataset}-{question_id}-incorrect-{index+1}",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": model,
                "temperature": temperature,
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {
                        "role": "user", 
                        "content": INCORRECT_PROMPT.substitute(dataset=dataset, dataset_description=GSM8K_DESCRIPTION, question=question)
                    }
                ]
            }
        }
        for index in range(num_responses)
    ]
    return queries


def main():
    # Set up argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, required=False, choices=["gsm8k"], # "MATH"],
                       default="gsm8k", help="Dataset to use. Permissible values: 'gsm8k' only for now")
    parser.add_argument("--num_samples", type=int, required=False, default=10,
                       help="Number of correct and incorrect samples to generate")
    parser.add_argument("--model", type=str, required=False, choices=["o1", "o3", "o4-mini"],
                       default="o4-mini", help="Model to use for generating samples")
    parser.add_argument("--temperature", type=float, required=False, default=0.3,
                       help="Temperature for the model")
    parser.add_argument("--output_file", type=str, required=False, 
                        default="data/dataset_request_{dataset}_{model}_temp{temperature}.jsonl",
                        help="Output file to save the dataset requests")
    args = parser.parse_args()

#     ######## TODO: check how to download the dataset from huggingface ########
#     # Download dataset from huggingface if not already present
#     if not os.path.exists(f"data/{args.dataset.lower()}"):
#         os.makedirs(f"data/{args.dataset.lower()}", exist_ok=True)
#         os.system(f"huggingface-cli download {args.dataset.lower()}")
#     with open(f"data/{args.dataset.lower()}/test.jsonl", "r") as f:
#         data = json.load(f) 
# ################################################################################

    # Set up dummy dataset for now
    data = ["Test question {i}: What is one plus the square of {i}?" for i in range(1, 1001)]

    # Assume data is procured and loaded as `data`
    with open(args.output_file.format(dataset=args.dataset, model=args.model, temperature=args.temperature), "w") as f:
        for i, question in tqdm(enumerate(data)):
            [
                f.write(json.dumps(query) + "\n") 
                for query in generate_question_queries(
                    question, 
                    i, 
                    args.model, 
                    args.temperature, 
                    args.num_responses, 
                    args.dataset
                )
            ]

if __name__ == "__main__":
    main()
