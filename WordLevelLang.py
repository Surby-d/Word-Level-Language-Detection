from googletrans import Translator
import re, json
translator = Translator()
class Word_level_lang_detection:
    def __init__(self):
        self.output_string = list()
        
    def detection(self, text):
        target_lang = {'en':'eng', 'es':'spa', 'hi':'hin'}
        if str(text).isalpha():
            try:
                lobj = translator.detect(text)
                detected_language = target_lang[lobj.__dict__['lang']]
            except KeyError:
                detected_language = 'unknown'
            finally:
                return f"{text}_{detected_language}"
        else:
            return f"{text}_token"
        
    def output(self, input_list):
        for string in input_list:
            string_list = []
            s = list(re.sub(r"[!]", "", string).split(" "))
            for str in s:
                string_list.append(self.detection(str))
            
            self.output_string.append(" ".join(string_list))
                    
            
if __name__ == '__main__':
    detector_obj = Word_level_lang_detection()
    try:
        with open("input.json", "r") as input_data:
            data = json.load(input_data)['input_list']
            detector_obj.output(data)
    except FileNotFoundError:
        print("File does not exist")
    
    with open("output.json", "w") as output_file:
        entry = {}
        entry['Output_list'] = detector_obj.output_string
        json.dump(entry, output_file)
    


