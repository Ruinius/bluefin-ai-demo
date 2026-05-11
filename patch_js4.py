with open('index.html', 'r') as f:
    content = f.read()

# I see what's wrong.
# If scrollY < offsetTop progress = 0; if scrollY > offsetTop + offsetHeight progress = 1.
# offsetTop is 11160. So scrollY needs to be BETWEEN 11160 and 11160+720 to have progress between 0 and 1.
# But wait, when I set ScrollY to 10800, pClosing2 was 1, and pClosing1 was 1?
# No, wait.
# offsetTop of 1 is 9720. 10080 > 9720, so progress = (10080 - 9720) / 720 = 360/720 = 0.5.
# But pClosing1 output was 1. Why?
