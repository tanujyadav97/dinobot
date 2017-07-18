from use_classifier import isques
from query_respond import ques_responce,ans_responce
import sys

str=sys.argv[1]
str=str.lower()
if isques(str):
    reply=ques_responce(str)
else:
    reply=ans_responce(str)

print reply