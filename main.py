import pdf2final_list
import text2ppt

# import debugpy
# debugpy.listen(("localhost", 5678))

topics = pdf2final_list.get_topics_from_keywords("Ice Cream")

x=pdf2final_list.process(topics['Ice Cream'])
text2ppt.presentate(x)
