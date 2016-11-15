Feedbacks :
---
* Try to upload the data also. Have a script that will download the data and save it into proper folders.
* A lot of the code is repeatative. Create a function instead.
* Add more comments to file or make it easy for the reader to understand what you actually trying to do.

```python
if len(sys.argv) < 2:         <- Use argparse instead. Lot safer.

f=open('Analysis1.txt','w+')  <- use `with open` instead.

dictQuestions={}
dictQuestions["user_id"] = i["owner"]["user_id"]
dictQuestions["title"] = i["title"]
listQuestions.append(dictQuestions)
and then
listQuestions[i]["silverCount"]=silverCount      <- Not a good coding style. Never modify your raw input unless really needed.

```
