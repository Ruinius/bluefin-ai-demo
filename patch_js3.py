with open('index.html', 'r') as f:
    content = f.read()

print("Epilogue container:", content.find('epilogue-container'))
print("content-closing-1:", content.find('content-closing-1'))
print("section-closing-1:", content.find('section-closing-1'))
print("pClosing1 calculation:", content.find('const pClosing1'))
print("msg1.style.opacity:", content.find('msg1.style.opacity = o;'))
