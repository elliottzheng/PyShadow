import json

def store(filename,data):
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(data))


#######     执行    ######## 
if __name__ =="__main__":
   
    #要修改的文件名
    listfile_name="id_list.json"
    front=['us','jp','sg','ssr']
    rear=['a','b','c']    
    data=json.load(open(listfile_name))
    id_list=data["configs"]
    ###
    for country in front:
        for index in rear:
            id_list.append({"ip":"ip"+country+index,'port':'port'+country+index,'password':"pw"+country+index})
    ###
    store(listfile_name,data)
    
