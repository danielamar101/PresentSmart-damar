from openai import OpenAI
import os
import json

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY")
)

def gpt_summarise(system,text, mode="text"):
    # print(text)
    completion = client.chat.completions.create(
                model="gpt-3.5-turbo", 
                messages = [{"role": "system", "content" : system},
                {"role": "user", "content" : text}],
                response_format={ "type": mode }
                )
    
    return(completion.choices[0].message.content)

def gpt_topics_from_keyword(system,text, mode="text"):
    # print(text)
    completion = client.chat.completions.create(
                model="gpt-3.5-turbo", 
                messages = [{"role": "system", "content" : system},
                {"role": "user", "content" : text}],
                response_format={ "type": mode }
                )
    
    return(completion.choices[0].message.content)

sys_prompt = """
Given a topic, you return information on the topic (elaborate and in depth. make it lengthy) in ten points. 
Strictly follow the syntax (Note the only two top level keys are Topic and Summary):
{
    'Topic' : <topic sentence>, 
    'Summary': [summary sentence 1,
                summary sentence 2,
                summary sentence 3,
                summary sentence 4,
                summary sentence 5,
                summary sentence 6,
                summary sentence 7,
                summary sentence 8,
                summary sentence 9,
                summary sentence 10']
}

Each Summary sentence should give complete in-depth knowledge of the topic. 
You must return a valid json object that follows the given syntax.
"""

topic_prompt = """
Given a keyword, you return 4 topics related to that keyword. The keyword must exist within each topic at any point. Make sure each topic is succinct and only contains one topic.
Strictly follow the syntax (Note the only top level key is the keyword):
{
    '<keyword>': [topic 1,
                topic 2,
                topic 3,
                topic 4,]
}

Each topic should be distinct and cover a wide breath of the keyword. 
You must return a valid json object that follows the given syntax.
"""

def process(topic_list):
    for topic in topic_list:
        text=gpt_summarise(sys_prompt,topic,'json_object')
        response = json.loads(text)
        
        print("Response:")
        print(response)

    return response

def get_topics_from_keywords(keyword):

    text=gpt_topics_from_keyword(topic_prompt,keyword,'json_object')
    response = json.loads(text)
        
    print("Response:")
    print(response)

    return response
