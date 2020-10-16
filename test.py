# coding:utf-8
import json
import os, sys
import time
import json
from flask import Flask, request

app = Flask(__name__)

BASE_URL = '/api/'
VUE_BASE_URL = "D:\programming\environment\\nginx-1.12.2\\nginx-1.12.2\html\lz_blog"
# 接收get请求
@app.route(BASE_URL + 'getAritle', methods=['GET'])
def test_get():
	filename = VUE_BASE_URL + "\data\word_data.json"
	dataFile = open(filename, 'rb')
	jsonFile = json.load(dataFile)
	dataFile.close()
	# 返回json
	result_json = json.dumps(jsonFile )
	return jsonFile 
    
    
# 接收post请求
@app.route(BASE_URL + 'addfile', methods=['POST'])
def test_post():
	# 解析请求参数
	data = request.get_data()
	json_data = json.loads(data.decode("utf-8"))
	name = json_data['name']
	importantText = json_data['importantText']
	content = json_data['htmlContent']
	res = writeFile(name, content)
	updateArticleData(name, importantText, res)
	return name

def updateArticleData(name, importantText, res):
	filename = VUE_BASE_URL + "\data\word_data.json"
	dataFile = open(filename, 'rb')
	jsonFile = json.load(dataFile)
	dataFile.close()

	jsonFile['articleData'].append({"title": name, "desc": importantText, "content": res['filename'], "create_time": res['create_time'], "update_time": res['create_time']})
	# new_dict = json.loads(json_str)
	with open(filename,"w") as f:
		# json.dump(jsonFile,f)
		f.write(json.dumps(jsonFile))
		print("加载入文件完成...")


def writeFile( name, content ):
    filecontent = content
    now = time.localtime()
    prename = VUE_BASE_URL + "\\file\\"
    filename = name + str(now[0]) + str(now[1]) + str(now[2]) + "_" + str(now[3]) + str(now[4]) + str(now[5]) + ".html"
    file = open(prename + filename, 'w')
    file.write(filecontent)
    file.close()
    create_time = str(now[0]) + '-' + str(now[1]) + '-' + str(now[2]) + "  " + str(now[3]) + ':' + str(now[4]) + ':' + str(now[5])
    res = {'filename': filename, 'create_time': create_time}
    return res

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
    # path = "file"
    # os.mkdir( path )
    # writeFile()
	# app.run(debug=True)
