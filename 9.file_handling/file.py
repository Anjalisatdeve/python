# kisi file ko access krn ho to
p = open(r'9.file_handling/demo.txt')
print(p.read())

# ye content demo file m add krega lekin jo pehele se demo file m likha honga vo sb remove hoke ye new content aayega
r=open("demo.txt",'w')
r.write("Hello this is me and i write content for demo file")

# bina content remove krke overwrite krne ke liye same file m we use
# append:
r=open("demo.txt",'a')
r.write("By this we overwrite content without privious data remove")
