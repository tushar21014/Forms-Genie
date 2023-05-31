Answers = ['Sure. Here are the answers to your questions:\n\n```\n[\n  {\n    "question": "What is SDLC?",\n    "answer": "Software Development Life Cycle",\n    "type": "mcq"\n  },\n  {\n    "question": "What is AI?",\n    "answer": "Artificial Intelligence",\n    "type": "mcq"\n  },\n  {\n    "question": "What do you mean by precipitation?",\n    "answer": "Water falling from the sky in the form of rain, snow, sleet, or hail",\n    "type": "short answer"\n  },\n  {\n    "question": "What do you mean by QFD?",\n    "answer": "Quality Function Deployment",\n    "type": "short answer"\n  }\n]\n```']
start_index = Answers[0].find('[')
end_index = Answers[0].rfind(']')

Answers = Answers[0][start_index:end_index+1]

print(Answers)
