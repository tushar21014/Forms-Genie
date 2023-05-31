mainlist = [['What is SDLC?', 'Software Development Life Cycle', 'mcq'], ['What is AI?', 'Artificial Intelligence', 'mcq'], ['Define SDLC', 'Software Development Life Cycle is a process that produces software with the highest quality and lowest cost in the shortest time possible.', 'short answer'], ['what do you mean by QFD?', 'Quality Function Deployment is a systematic approach to translating customer requirements into design requirements.', 'short answer']]

for child in mainlist:
    for subchild in child:
        if(subchild == 'short answer'):
            print("I am a short answer" , child[0])