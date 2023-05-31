from playwright.sync_api import sync_playwright
import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from bardapi import Bard
import re
from pathlib import Path
import multiprocessing
import json

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSew_3ese2znTNCx1dCZF4ufMRTNvQROgVYguYZb6Q_wwkzvWA/viewform'
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\tg210\OneDrive\Desktop\Codes\Sem 3\Designer\build\assets\frame0")



def when_clicked():
    if __name__ == '__main__':
        # p1.start()
        p2.start()
        # p1.join()
        p2.join()



def backend():
    def filtering(data_params, question_type):
        pattern = r'"([^"]*)"'
        main_words = re.findall(pattern, data_params)
        unique_list = list(set(main_words))
        filtered_list = [elem for elem in unique_list if not any(f'i{x}' in elem for x in range(1, 101))]
        # print("I am filtered list words" , filtered_list)
        split_list = [[item] for item in filtered_list]
        # print("i am main question with options list", split_list)
        split_list.append(question_type)

        questionsList.append(split_list)
        print(questionsList)

    questionsList = []
    Answers = []
    personalKeywords = ['name','phone','email']
    marking_ques_ans = []

    # Create an instance of the Bard class
    bard = Bard(token="XAjKrsM6FEgQgXtzOgAHB8ZmqaMeV_1xblynmyET9OsdJek8wC11pOE2OdVuXN_6WAZnOQ.")

    # Send a GET request to the form URL to retrieve the HTML content
    response = requests.get(form_url)
    html_content = response.text

    # Parse the HTML content using PyQuery
    doc = pq(html_content)

    # Find all the <div> elements
    div_elements = doc('div')

    # Extract the 'data-params' attribute from each <div> element and extract the text
    for i, div in enumerate(div_elements.items(), 1):
        data_params = div.attr('data-params')
        # print(data_params)
        if data_params:
            texts = data_params.split(',')
            # print("I am texts ", texts)

            if len(texts) > 1:
                for i in texts:
                    if i == "0":
                        filtering(data_params, 'short answer')
                        print("Short Answer")
                    if i == "1":
                        filtering(data_params, 'long answer')
                        print("Long Answer")
                    if i == "2":
                        filtering(data_params, 'mcq')
                        
                        # for innerquestions in MCQ:
                        #     print("I am inner question", innerquestions)
                        #     Ans = bard.get_answer("Answer the question only with the option name and no extra text  \n" + str(innerquestions))['content']
                        #     Answers.append("yeah its me "+  Ans)

                    if i == "3":
                        # filtering(data_params)
                        print("DropDown")
                    if i == "4":
                        # filtering(data_params)
                        print("Check Boxes")
                        

    # filtered_list = []
    # for qna in questionsList:
    #     if any(keyword in str(qna).lower() for keyword in personalKeywords):
    #         filtered_list.append([])
    #     else:
    #         filtered_list.append(qna)

    data_filtered = [qna for qna in questionsList if not any(keyword in str(qna).lower() for keyword in personalKeywords)]
    print("Final Question List " , data_filtered)

    Ans = bard.get_answer('Answer the question only with the option name and no extra text and answer in brief if a question does not contain option return it in a form [{"question": "question","answer": "Answer","type": "mcq"}] \n' + str(data_filtered))['content']
    # Ans = bard.get_answer('Answer the question only with the option name and no extra text and answer in brief if a question does not contain option return it in a form of list of strings like Question : question , answer : answer\n' + str(data_filtered))['content']
    Answers.append(Ans)
    print(Answers)

# Remove the unwanted line
    Answers[0] = Answers[0].replace("Sure, here are the answers to your questions:\n\n\n", "")
    Answers[0] = Answers[0].replace("Sure, here are your answers:\n\n\n", "")
    Answers[0] = Answers[0].replace("'Sure. Here are the answers to your questions:\n\n\n", "")
    Answers[0] = Answers[0].replace("'Sure. Here are the answers to your questions:\n\n```\n", "")
    Answers[0] = Answers[0].replace("'Here are the answers to your questions:\n\n\n", "")
    Answers[0] = Answers[0].replace("'Here are the answers to your questions:\n\n\n", "")
    Answers[0] = Answers[0].replace("'Sure. Here are your questions and answers:\n\n\n", "")
    Answers[0] = Answers[0].replace("'Sure, here are your answers:\n\n", "")
# Print the updated list
    print(type(Answers))
    print(Answers)
    # Answers= str(Answers)
    # print(type(Answers))
    # print(Answers)

    json_data = Answers[0]
    print(json_data)
    data_list = json.loads(json_data)
    print(data_list)
    
    marking_ques_ans = [[item['question'], item['answer']] for item in data_list]
    print(marking_ques_ans)

    # for ans in Answers:
    #     print("\n\n", ans)
    
def Parent(page):
    answersList = [['What is SDLC?', 'Software Development Life Cycle', 'mcq'], ['What is AI?', 'Artificial Intelligence', 'mcq'], ['Define SDLC', 'A structured process that enables the production of high-quality, low-cost software, in the shortest possible production time.', 'short answer'], ['What do you mean by QFD?', 'Quality Function Deployment', 'short answer']]
    response = requests.get(form_url)
    soup = BeautifulSoup(response.content, "html.parser")
    parent_div = soup.find_all("div", class_ = 'Qr7Oae')

    for i in parent_div:
        temp = (i.find("span").text)
        # temp_inp = i.find_all("input")
        print(temp)
        input_element = i.find('input')
   
        if(input_element):
            # print(input_element)
            input_type = input_element.get('type')
            print(input_type)
            for child in answersList:
                for subchild in child:
                    pass
                    if(subchild == 'short answer' and temp == child[0]):
                        print("I am a short answer" , child[0])
        else:
            print("Not found")

def frontend():
    
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()

        page.goto(form_url)

        page.wait_for_timeout(1000)

        signin_butt = page.wait_for_selector('.XfpsVe > div:nth-child(2) > span:nth-child(3) > span:nth-child(1)')
        signin_butt.click()


        page.wait_for_selector("#identifierId")

        input_element = page.query_selector('[name="identifier"]')
        name = "malhotaraj5@gmail.com"
        input_element.fill(name)

        nextButton = page.wait_for_selector(".VfPpkd-LgbsSe-OWXEXe-k8QpJ > div:nth-child(3)")
        nextButton.click()

        if nextButton:
            print("Found")
        else:
            print("Not found")


        page.wait_for_timeout(3000)
        page.wait_for_selector('[name="Passwd"]', state="visible")

        input_element2 = page.wait_for_selector('[name="Passwd"]')
        password = "brothers like me"
        input_element2.fill(password)

        nextButton2 = page.wait_for_selector(".VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(4)")
        nextButton2.click()

        Parent(page)

        page.wait_for_timeout(500000)
        browser.close()


p1 = multiprocessing.Process(target=backend)
p2 = multiprocessing.Process(target=frontend)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

if __name__ == '__main__':

    window = Tk()

    window.geometry("1366x768")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 768,
        width = 1366,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        341.0,
        384.0,
        image=image_image_1
    )

    canvas.create_text(
        720.0,
        238.0,
        anchor="nw",
        text="Please paste your URL here",
        fill="#000000",
        font=("Inter Bold", 36 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=when_clicked,
        relief="flat",
    )

    def on_Enter(event):
        button_1.config(bg='lightblue')
    def on_Leave(event):
        button_1.config(bg='SystemButtonFace')

    button_1.bind('<Enter>',on_Enter)
    button_1.bind('<Leave>',on_Leave)
    

    button_1.place(
        x=876.0,
        y=439.0,
        width=272.0,
        height=70.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        1017.0,
        355.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=782.0,
        y=323.0,
        width=470.0,
        height=56.0
    )

    window.resizable(False, False)
    window.mainloop()
