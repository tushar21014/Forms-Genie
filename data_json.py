import json
Answers = '''['[\n  {\n    "question": "What is SDLC",\n    "answer": "Software Development Life Cycle",\n    "type": "mcq"\n  },\n  {\n    "question": "What is AI",\n    "answer": "Artificial Intelligence",\n    "type": "mcq"\n  },\n  {\n    "question": "Define SDLC",\n    "answer": "SDLC is a process followed for a software project, within a software organization. It consists of a detailed plan describing how to develop, maintain, replace and alter or enhance specific software.",\n    "type": "short answer"\n  },\n  {\n    "question": "what do you mean by QFD",\n    "answer": "QFD is a process for translating customer requirements into design requirements.",\n    "type": "short answer"\n  }\n]\n']'''
# Answers = '''[\n  {\n    "question": "What is SDLC?",\n    "answer": "Software Development Life Cycle",\n    "type": "mcq"\n  },\n  {\n    "question": "What is AI?",\n    "answer": "Artificial Intelligence",\n    "type": "mcq"\n  },\n  {\n    "question": "Define SDLC",\n    "answer": "SDLC is a process followed for a software project, within a software organization. It consists of a detailed plan describing how to develop, maintain, replace and alter or enhance specific software.",\n    "type": "short answer"\n  },\n  {\n    "question": "What do you mean by QFD?",\n    "answer": "QFD is a quality function deployment. It is a systematic approach to translating customer requirements into product design.",\n    "type": "short answer"\n  }\n]'''
Answers = '''['  {\n    "question": "What is SDLC?",\n    "answer": "Software Development Life Cycle",\n    "type": "mcq"\n  },\n  {\n    "question": "What is AI?",\n    "answer": "Artificial Intelligence",\n    "type": "mcq"\n  },\n  {\n    "question": "Define SDLC",\n    "answer": "SDLC stands for Software Development Life Cycle. It is a process that defines the steps involved in developing software.",\n    "type": "short answer"\n  },\n  {\n    "question": "What do you mean by QFD?",\n    "answer": "QFD stands for Quality Function Deployment. It is a process that helps to ensure that the quality of a product or service meets the needs of the customer.",\n    "type": "short answer"\n  }\n]\n']'''
Answers = ['Sure, here are the answers to your questions:\n\n\n[\n  {\n    "question": "What is SDLC?",\n    "answer": "Software Development Life Cycle",\n    "type": "mcq"\n  },\n  {\n    "question": "What is AI?",\n    "answer": "Artificial Intelligence",\n    "type": "mcq"\n  },\n  {\n    "question": "Define SDLC",\n    "answer": "SDLC is a process that defines the steps involved in the development of software at each phase. It covers the detailed plan for building, deploying and maintaining the software.",\n    "type": "short answer"\n  },\n  {\n    "question": "what do you mean by QFD?",\n    "answer": "QFD is a systematic approach to translating customer requirements into design requirements.",\n    "type": "short answer"\n  }\n]\n']
Answers = ['[\n  {\n    "question": "What is SDLC",\n    "answer": "Software Development Life Cycle",\n    "type": "mcq"\n  },\n  {\n    "question": "What is AI",\n    "answer": "Artificial Intelligence",\n    "type": "mcq"\n  },\n  {\n    "question": "Define SDLC",\n    "answer": "SDLC stands for Software Development Life Cycle. It is a process that defines the phases involved in developing software.",\n    "type": "short answer"\n  },\n  {\n    "question": "What do you mean by QFD?",\n    "answer": "QFD stands for Quality Function Deployment. It is a process that helps organizations to identify and prioritize customer requirements.",\n    "type": "short answer"\n  }\n]\n']
json_data = Answers[0]
print(type(Answers))
# json_data = json_data.replace('Sure, here are the answers to your questions:\n\n\n', '')
print(json_data)
data_list = json.loads(json_data)
# questions_and_answers = [[item["question"], item["answer"]] for item in data_list]
print(data_list)

print(type(Answers))

# questions_and_answers = list(map(lambda item: [item["question"], item["answer"]], Answers))
# print(questions_and_answers)
# questions_and_answers = []
# Answers = str(Answers)
# data = json.loads(Answers)

# for item in data:
#     question = item["question"]
#     answer = item["answer"]
#     questions_and_answers.append([question, answer])

#     print(questions_and_answers)