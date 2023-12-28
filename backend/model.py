import numpy as np
import pandas as pd
import os
import re

class Resume:

    def __init__(self, text, filepath):
        filepath = os.path.dirname(__file__)
        self.filepath = os.path.join(dir, 'backend/uploads/')
        self.text = text
        return
    
    def process_resume(self):
        def clean(text):
            text = re.sub(r"\b(\d{3})[-.]?(\d{3})[-.]?(\d{4})\b", "", text) # Removes Phone Number
            text = re.sub(r"\b(\d{10})\b", "", text) # Removes Phone Number P2
            text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "", text) # Removes Email
            text = re.sub("http[s]?\://\S+","",text) # Removes Links
            text = re.sub(r"(\r)|(\n)", text) # Removes escape characters
            return text
        return clean(self)