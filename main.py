from deepface import DeepFace
import json

def try_ex_dec(fn):
    def wrapped(*args, **kwargs):
        try:
            fn(*args, **kwargs)
        except Exception as e:
            print("error:", e)
    return wrapped

@try_ex_dec
def face_verify(img_1, img_2):
    result_dict = DeepFace.verify(img1_path=img_1, img2_path=img_2)

    with open('data.json', 'w') as f:
        json.dump(result_dict, f, indent=4, ensure_ascii=False)

    print(result_dict)
    return result_dict

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    face_verify(img_1='faces/sasha (1).jpg', img_2='faces/sasha (8).jpg')
