from deepface import DeepFace
import json


def try_ex_dec(fn):
    def wrapped(*args, **kwargs):
        try:
            fn(*args, **kwargs)
        except Exception as e:
            print("ошибка:", e)

    return wrapped


@try_ex_dec
def face_verify(img_1, img_2):
    result_dict = DeepFace.verify(img1_path=img_1, img2_path=img_2)

    # to json
    with open('data.json', 'w') as f:
        json.dump(result_dict, f, indent=4, ensure_ascii=False)

    if result_dict['verified'] == True:
        print('Welcome')
    else:
        print('stop')

    print(result_dict)
    return result_dict


@try_ex_dec
def face_recognition(img, db):
    result = DeepFace.find(img_path=img, db_path=db)

    # # to json
    # with open('data.json', 'w') as f:
    #     json.dump(result_dict, f, indent=4, ensure_ascii=False)

    print(result)
    return result


@try_ex_dec
def face_analyze(img):
    result_dict = DeepFace.analyze(img_path=img, actions=['age', 'gender', 'race', 'emotions'])

    # to json
    with open('face_analyze.json', 'w') as f:
        json.dump(result_dict, f, indent=4, ensure_ascii=False)

    print(result_dict)
    return result_dict


if __name__ == '__main__':
    # face_verify(img_1='faces/sasha (1).jpg', img_2='faces/sasha (8).jpg')
    # face_recognition(img='faces/sasha (1).jpg', db='faces')
    face_analyze(img='faces/sasha (1).jpg')
