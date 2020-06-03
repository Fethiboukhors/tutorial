file_contents = "If (this was your first time running the above/" \
                " cell containing the installs and imports, you will/" \
                " need save this notebook now. Then under the File menu above, /" \
                "select Close and Halt. When the notebook has completely shut down, reopen it. /" \
                "This is the only way the necessary changes will take affect."

uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~,/'''

for char in file_contents:
    if char in punctuations:
        file_contents = file_contents.replace(char,"")
file_contents = file_contents.lower()
file_contents = file_contents.split()
for char in list(file_contents):
    if char in uninteresting_words:
        file_contents.remove(char)
frequency = {}
for item in file_contents:
   if (item in frequency):
      frequency[item] += 1
   else:
      frequency[item] = 1

file_contents = frequency
print(file_contents)