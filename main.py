import os
import json
from xml.etree import ElementTree as ET
from glob import glob

SAVE_FILENAME = "dataset.jsonl"
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")
XML_DIR = os.path.join(DATASET_DIR, "wiki_corpus_2.01")
SAVE_FILE_PATH = os.path.join(BASE_DIR, SAVE_FILENAME)

def get_xml_list():
    return glob(os.path.join(XML_DIR, "*", "*.xml"))

def get_translations_from_xml(f):
    v = {
        "ja": [],
        "en-trans-v1": [],
        "en-trans-v2": [],
        "en-check": []
    }
    result = []
    for line in f:
        if not("<j>" in line or "<e type=" in line):
            continue
        element = ET.fromstring(line.strip())
        if element.tag == "j":
            v["ja"].append(element.text)
        elif element.get("type") == "check":
            v["en-check"].append(element.text)
        elif element.get("ver") == "1":
            v["en-trans-v1"].append(element.text)
        elif element.get("ver") == "2":
            v["en-trans-v2"].append(element.text)
    if len(v["ja"]) != len(v["en-check"]) \
        or len(v["ja"]) != len(v["en-trans-v1"]) \
        or len(v["ja"]) != len(v["en-trans-v2"]):
        raise ValueError("invalid xml. translate sentences is not same length")
    for i in range(len(v["ja"])):
        result.append({
            "ja": v["ja"][i],
            "en-trans-v1": v["en-trans-v1"][i],
            "en-trans-v2": v["en-trans-v2"][i],
            "en-check": v["en-check"][i],
        })
    return result

def add_jsonl_line(path, item):
    with open(path, "a") as f:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

def progress_iterator(target_list):
    l = len(target_list)
    for i in range(l):
        print(f"\r\033[K#progress: {str(int(i/l*100))}%", end="")
        yield target_list[i]
    print("")

if __name__ == "__main__":
    if os.path.exists(SAVE_FILE_PATH) \
        and input(f"remove {SAVE_FILENAME}?(y/N)") in ["y", "Y"]:
        os.remove(SAVE_FILE_PATH)
    path_list = get_xml_list()
    for path in progress_iterator(path_list):
        with open(path) as f:
            items = get_translations_from_xml(f)
            for item in items:
                add_jsonl_line(SAVE_FILE_PATH, item)