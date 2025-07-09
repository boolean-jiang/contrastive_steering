# TODO: 
# Define prompts here 
from string import Template

GSM8K_DESCRIPTION = """GSM8K consists of 8.5K high quality grade school math problems created by human problem writers. """
"""These problems take between 2 and 8 steps to solve, and solutions primarily involve performing a sequence of elementary """
"""calculations using basic arithmetic operations (+ - / *) to reach the final answer. A bright middle school student should be """
"""able to solve every problem."""

CORRECT_PROMPT = Template("""You will be given a question from the ${dataset} dataset. The description of the dataset is as follows: 

${dataset_description}

The question is as follows:

${question}

Please provide between 1-5 sentences of reasoning, and then provide the numerical answer to the question in your last sentence. """
"""Your entire response should be bracketed by <answer> and </answer>. 

You may only include one set of answer tags in your response.
""") 

INCORRECT_PROMPT = Template("""You will be given a question from the ${dataset} dataset. The description of the dataset is as follows: 

${dataset_description}

The question is as follows:

${question}

Your task is to answer this question INCORRECTLY, but in such a way that mimics how a human might make an arithmetic mistake. """
"""Begin your response with between 1-5 sentences of reasoning that is consistent with the INCORRECT answer (i.e. faulty reasoning). """
"""For example, the problem may be solved by subtracting 5 from 2. In this case, an appropriate response might be: "I performed five """
"""minus two which is seven", which is an error a human might carelessly make. Then, provide the INCORRECT numerical answer to the """
"""question in your last sentence.Your entire response should be bracketed by <answer> and </answer> - for example: """
"""<answer>I performed five minus two which is seven. The final answer is 7.</answer>

You may only include one set of answer tags in your response.
""") 