from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get_classifier_result/<version>", methods=['GET', 'POST'])
def return_classifier_result(version):
	if request.method == 'POST':
        if int(version) == 1:
            return jsonify(version=1, predict=request.get_json()['predict'])
        return jsonify(version=0, predict=request.get_json()['old_predict'])
    #TODO прочитать из полученного запроса json-контент
    #В случае, если version==1, то должен вернуться json с версией и полем predict из входящего jsonа {"version":1, "predict":<predict_value>}
    #В случае, если version==0, то должен вернуться json с версией и полем old_predict из входящего jsonа {"version":0, "predict":<old_predict_value>}

@app.route("/")
def hello():
    return """Серверу нужно отправить запрос  requests.post(url, data, headers)
     URL  вида url/get_classifier_result/<version>, где <version> - '1' - новая    или '0' - старая версия 
     Требуется отправить файл в формате json.
     {"predict" : i} - при <version> - '1', 
     {"old_predict": i} при <version> - '0'
     Ответом на запрос будет dict:
     {"version" : value, "predict" : value}
     На ['version'] возвращается 1 или 0, на ['predict'] отправленное значение 
     """

if __name__ == "__main__":
    app.run()
