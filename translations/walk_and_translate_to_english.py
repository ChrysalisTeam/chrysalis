

import os, sys, subprocess, shelve, requests

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


LOG_FILE = os.path.abspath('file_translator_result.log')

SAVE_FILE = os.path.abspath("file_translator_save.txt")


SHELF = shelve.open(os.path.abspath("file_translator.db"), flag='c', writeback=True)


if len(sys.argv) > 1:
    START_DIR = os.path.abspath(sys.argv[1])
else:
    START_DIR = THIS_DIR

TARGET_DIR = START_DIR.rstrip("/\\") + "_output"

    
def report_error(message):
    with open(LOG_FILE, 'a') as f:
        f.write(message)
        
'''
def load_progress():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return f.read().splitlines()
    return []
    
def save_progress(paths):
    with open(SAVE_FILE, "w") as f:
        f.write("\n".join(paths))
  
progress = load_progress()   
'''   

_auth_key = "caf18680-cef9-ae21-2f57-02ba0666fe46"

def _do_translate_via_deepl_webservices(filename):
    basename = os.path.basename(filename)
    
    data = dict(
         auth_key=_auth_key,
         source_lang="FR",
         target_lang="EN",
         filename="myexample.txt",
    )
    files = {'file': open(filename,'rb')}
    
    response = requests.post("https://api.deepl.com/v2/document", data=data, files=files)

    if response.status_code != 200:
        raise RuntimeError("Error in Deepl API (code %s): %s" % (response.status_code, response.content))

    data = response.json()
    ''' example
            "document_id": "4D93510B386BA64DC32102B88C17F018",
            "document_key": "[documentKey]"
    
    '''
    print ("RECEIVED DEEPL TRANSLATION CALL RESPONSE", filename, data)
    return data


def _get_document_info(document_id, document_key):

    data = dict(
         auth_key=_auth_key,
         document_key=document_key,
    )
    
    response = requests.get("https://api.deepl.com/v2/document/%s" % document_id, data)
    data = response.json()
    print ("RECEIVED DEEPL DOCUMENT STATUS RESPONSE", filename, data)
    return data


def _retrieve_document(document_id, document_key):

    data = dict(
         auth_key=_auth_key,
         document_key=document_key,
    )
    
    response = requests.get("https://api.deepl.com/v2/document/%s/result" % document_id, data)
    data = response.content
    print ("RECEIVED DEEPL TRANSLATED DOCUMENT BODY", type(data))
    return data
    

try:
    for root, dirs, files in os.walk(START_DIR):
    
        root_repr = root.encode("ascii", "replace")
        
        print (">> Currently exploring", root_repr)
        
        if 'Trash' in root or "\\." in root or "/." in root or "$RECYCLE" in root:
            dirs[:] = []  # ABORT this branch of filesystem
            
        for filename in files:
        
            base, ext = os.path.splitext(filename)
            
            if ext not in ('.rst', ".yaml", ".yml", ".odt", ".docx"):
                continue
            
            full_filepath = os.path.join(root, filename)
            #full_filepath_repr = full_filepath.encode("ascii", "replace")
            
            if full_filepath in SHELF:
                
                identifiers = SHELF[full_filepath]
                
                if identifiers.get("result_bytes"):
                    print("> skipping already downloaded translation", full_filepath)
                    continue
                    
                print (">>>> Checking already uploaded content file", full_filepath, SHELF[full_filepath])
                
                data = _get_document_info(identifiers["document_id"], identifiers["document_key"])
                if data.get("status")== "done":
                    
                    document_bytes = _retrieve_document(identifiers["document_id"], identifiers["document_key"])
                   
                    target_file = full_filepath.replace(START_DIR, TARGET_DIR)
                    assert target_file != full_filepath, (target_file, full_filepath)
                    os.makedirs(os.path.dirname(target_file), exist_ok=True)
                    
                    with open(target_file, "wb") as f:
                        f.write(document_bytes)
                    
                    SHELF[full_filepath]["result_bytes"] = document_bytes
                    SHELF[full_filepath]["result"] = data
                    SHELF[full_filepath] = SHELF[full_filepath]  # Force rewrite...
                
            else:
                print (">>>> Converting content for file", full_filepath)
                
                result = _do_translate_via_deepl_webservices(full_filepath)
                SHELF[full_filepath] = result
                SHELF.sync()
                 
                """
                cmd = ZIP_EXECUTABLE % full_filepath
                print ("-->", cmd)
                proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                outs, errs = proc.communicate(timeout=3600)
                
                if proc.returncode != 0:
                    msg = "\n\nERROR: return code %s for zip test of %s!" % (proc.returncode, full_filepath)
                    msg += "\n\nOUTPUT:\n%s" % outs.decode("ascii", "ignore")
                    msg += "\n\nSTDERR:\n%s" % errs.decode("ascii", "ignore")
                    report_error(msg)
                """
                ###progress.append(full_filepath)

finally:
    #save_progress(progress)
    SHELF.close()