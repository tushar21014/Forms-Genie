from playwright.sync_api import sync_playwright
import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from bardapi import Bard
import re
from pathlib import Path
import multiprocessing
import json
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,StringVar
import threading

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\tg210\OneDrive\Desktop\Codes\Sem 3\Designer\build\assets\frame0")
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSew_3ese2znTNCx1dCZF4ufMRTNvQROgVYguYZb6Q_wwkzvWA/viewform?usp=sf_link"
universal_answerlist = []


def backend(q,event):

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
    marking_ques_ans = []
    Answers = []
    personalKeywords = ['name','phone','email']

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

    # data_filtered = []
    # for qna in questionsList:
    #     contains_personal_keyword = any(keyword in str(qna).lower() for keyword in personalKeywords)
    #     if contains_personal_keyword:
    #         # Find the index of the personal keyword in personalKeywords
    #         keyword_index = next((i for i, keyword in enumerate(personalKeywords) if keyword in str(qna).lower()), None)
    #         if keyword_index is not None:
    #             replacement_value = replacement_values[keyword_index]
    #             updated_qna = [replacement_value if keyword in str(elem).lower() else elem for elem, keyword in zip(qna, personalKeywords)]
    #             data_filtered.append(updated_qna)
    #     else:
    #         data_filtered.append(qna)

    # print("I am filtered data" , data_filtered)

    Ans = bard.get_answer('Answer the question only with the option name and no extra text and answer in brief if a question does not contain option return it in a form [{"question": "question","answer": "Answer","type": "type"}] and make sure you dont add ``` these signs' + str(data_filtered))['content']
    # Ans = bard.get_answer('Answer the question only with the option name and no extra text and answer in brief if a question does not contain option return it in a form of list of strings like Question : question , answer : answer\n' + str(data_filtered))['content']
    Answers.append(Ans)
    print(Answers)

# Remove the unwanted line
    start_index = Answers[0].find('[')
    end_index = Answers[0].rfind(']')

    Answers = Answers[0][start_index:end_index+1]

# Print the updated list
    print(type(Answers))
    print(Answers)

    # json_data = Answers[0]
    # print("I am json data " , json_data)
    data_list = json.loads(Answers)
    print("i am data list " , data_list)
    
    marking_ques_ans = [[item['question'], item['answer'], item['type']]  for item in data_list]

    print("I am marking questionss \n" , marking_ques_ans)

    for i in marking_ques_ans:
        q.put(i)

    event.set()
    print("Event is set ")

        
    

def ParentClass(page,q,event):
    event.wait()
    # print("waits is over")
    # page.wait_for_timeout(5000)
    Answers = []
    while not q.empty():
        item = q.get()
        print(item)
        Answers.append(item)
    
    print("\n I am Answers", Answers)
    print("My wait is over \n")

    response = requests.get(form_url)
    soup = BeautifulSoup(response.content, "html.parser")
    parent_div = soup.find_all("div", class_ = 'Qr7Oae')
    i = 1
    l = 1
    k = len(soup.find_all("div", class_ = 'Qr7Oae'))
    
    if l < k:
        for i in parent_div:
            page_ques = (i.find("span").text)
            parent_input_class = page.wait_for_selector(f'div.Qr7Oae:nth-child({l})')
            # mcq_input_class = i.wait_for_selector("div", class_ = "Od2TWd hYsg7c")
            # print(mcq_input_class)
            l += 1
            input_element = parent_input_class.query_selector('input')
            # print(parent_input_class)
            # temp_inp = i.find_all("input")
            print(page_ques)
            # input_element = i.find('input', class_ = "whsOnd zHQkBf")
            # input_element = i.wait_for_selector('input')
    
            if(input_element):
                input_type = input_element.get_attribute('type')
                print(input_type)
                for child in Answers:
                    user_question = child[0]
                    # print("I am question",question)
                    answer = child[1]
                    answer_type = child[2]
                    # print("I am question",answer_type)
                    print("I am temp", page_ques)
                    print("I am ques" , user_question)

                    if answer_type == "short answer":
                        if user_question == page_ques:
                            # input_element.fill(answer)
                            # input_element['value'] = answer
                            print("Filled input element with answer:", answer)
                            input_element.fill(answer)
                            Answers.pop(0)
                        else:
                            print("Questions don't match")
                    elif answer_type == 'mcq':
                        if user_question == page_ques:
                            print("MCQ found")
                            page.get_by_label(answer).check()
                            Answers.pop(0)
                            break

            else:
                print("Input element not found")


    

    # while i <= div_count:
    #     radioButtonsChild = 0
    #     temp = page.wait_for_selector(f'div.Qr7Oae:nth-child({i})')
    #     input_element = temp.query_selector('input')
    #     if input_element:
    #         input_value = input_element.get_attribute('value')
    #         input_type = input_element.get_attribute('type')
    #         # input_role = input_element.get_attribute('role')
    #         print(f"Found <input> element at position {i}. Value: {input_value}. Input Type {input_type}.")
    #         # print(universal_answerlist)
    #         if (input_type == "text"):
    #             for child in Answers:
    #                 for subchild in child:
    #                     if(subchild == 'short answer'):
    #                         print("I am a short answer" , child[1])
    #                         input_element.fill(child[l])
    #             # input_element.fill(Answers[l])
    #             l+=1
    #         if(input_type == 'hidden'):
    #             pass
    #             radioButtons = soup.find_all("div",class_ = 'lLfZXe fnxRtf cNDBpf')
    #             radioButtonsChild = soup.find_all("div", class_ = 'nWQGrd zwllIb')
    #             # radioButtonsChildCount = len(radioButtonsChild)
    #             radioButtonsChildCount = len(soup.find_all("div", class_='nWQGrd zwllIb'))
    #             print(radioButtonsChildCount)
    #             # mcq_question = page.query_selector(f'div.Qr7Oae:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)')
    #             if(radioButtonsChild):
    #                 print("Got it")
    #             else:
    #                 print("Not Got it")

                    
    #     else:
    #         print(f"No <input> element found at position {i}")
    #     i += 1


def frontend(q,event):
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

        # if nextButton:
        #     print("Found")
        # else:
        #     print("Not found")


        page.wait_for_timeout(5000)
        page.wait_for_selector('[name="Passwd"]', state="visible")

        input_element2 = page.wait_for_selector('[name="Passwd"]')
        password = "brothers like me"
        input_element2.fill(password)

        page.wait_for_timeout(5)
        nextButton2 = page.wait_for_selector(".VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(4)")
        nextButton2.click()

        temp = page.wait_for_selector('div.Qr7Oae:nth-child(1)')
        
        if(temp):
            print("Mil gye")
        else:
            print("Nhi Mil gye")

        ParentClass(page,q,event)


        page.wait_for_timeout(50000)
        browser.close()

event = multiprocessing.Event()
q = multiprocessing.Queue()
p1 = multiprocessing.Process(target=backend, args=(q,event))
p2 = multiprocessing.Process(target=frontend, args=(q,event))

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def when_clicked(): 
    # print("Entered value:", value)
    p1.start()
    # print(value)
    p2.start()
    p1.join()
    p2.join()



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

    temporary_var = StringVar()

    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable= temporary_var
    )
    entry_1.place(
        x=782.0,
        y=323.0,
        width=470.0,
        height=56.0
    )



    window.resizable(False, False)
    window.mainloop()
