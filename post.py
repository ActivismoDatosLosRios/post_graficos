import requests
import json
import base64


def postChartToApi(title, image, tags):
    url = 'http://activismo.inf.uach.cl:8080/api/chart/'
    payload = {
        "title": title,
        "image": image,
        "tags": tags  # array del tipo ["tag1", "tag2", "tag3"]
    }
    headers = {'Content-Type': 'application/json'}

    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.text)


def encodeb64(img):
    converted = cv2.imencode('.png', img)[1].tostring()
    encode = base64.b64encode(converted)
    return 'data:image/png;base64,' + str(encode)[2: -1]
