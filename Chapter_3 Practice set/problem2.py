letter = '''Dear <|Name|>,
You are selected !
<|Date|>
            '''

print(letter.replace("<|Name|>", "Sumit") .replace("<|Date|>", "04 May 2025"))