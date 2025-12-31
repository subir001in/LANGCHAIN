import os
##FUNCTION TO LOAD API KEY FROM A FILE
def load_api_key_from_file(path: str) -> str | None:
    '''
    FUNCTION TO LOAD API KEY FROM A FILE
    '''
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            # try to find token starting with sk-
            for part in content.split():
                print(part)
                if part.startswith("sk-"):
                    return part
            return content or None
    except FileNotFoundError:
        return None