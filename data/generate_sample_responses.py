


def main():
    # Set up argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, required=True, choices=["gsm8k", "MATH"],
                       help="Dataset to use. Permissible values: 'gsm8k', 'MATH'")
    parser.add_argument("--num_samples", type=int, required=True,
                       help="Number of correct and incorrect samples to generate")
    args = parser.parse_args()

    ######## TODO: check how to download the dataset from huggingface ########
    # Download dataset from huggingface if not already present
    if not os.path.exists(f"data/{args.dataset.lower()}"):
        os.makedirs(f"data/{args.dataset.lower()}", exist_ok=True)
        os.system(f"huggingface-cli download {args.dataset.lower()}")
    with open(f"data/{args.dataset.lower()}/test.jsonl", "r") as f:
        data = json.load(f) 
################################################################################

if __name__ == "__main__":
    main()
