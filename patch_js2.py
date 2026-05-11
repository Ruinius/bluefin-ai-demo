with open('index.html', 'r') as f:
    content = f.read()

# Remove our previous addition
js_to_add = """
            // Section 11-13 — Epilogue Closing Messages
            const pClosing1 = getProgress('section-closing-1');
            const pClosing2 = getProgress('section-closing-2');
            const pClosing3 = getProgress('section-closing-3');

            // Product UI Fade Out
            if (pClosing1 >= 0 || pPreview > 0.85) {
                // If we're past section 10 or into 11, fade out UI
                const uiOpacity = pClosing1 > 0 ? mapRange(pClosing1, 0.0, 0.2, 1, 0) : 1;

                const sidebar = document.getElementById('sidebar');
                if (sidebar) sidebar.style.opacity = pClosing1 > 0 ? uiOpacity : 1;

                const dashboard = document.getElementById('dashboard-container');
                if (dashboard) dashboard.style.opacity = pClosing1 > 0 ? uiOpacity : 1;

                const workspace = document.getElementById('workspace-container');
                if (workspace) workspace.style.opacity = pClosing1 > 0 ? uiOpacity : 1;

                const welcome = document.getElementById('welcome-container');
                if (welcome) welcome.style.opacity = pClosing1 > 0 ? uiOpacity : 1;

                // Hide cursor if it exists
                if (cursor && pClosing1 > 0) {
                    cursor.style.opacity = uiOpacity;
                }
            } else {
                 const sidebar = document.getElementById('sidebar');
                 if (sidebar) sidebar.style.opacity = 1;
                 const dashboard = document.getElementById('dashboard-container');
                 // Only reset if Dashboard was shown. Let's not interfere with earlier sections
                 // where dashboard might be hidden. Handled by other sections.
            }

            // Closing Message 1
            const msg1 = document.getElementById('content-closing-1');
            if (msg1) {
                if (pClosing1 > 0.1 && pClosing1 < 0.9) {
                    let o = 1;
                    if (pClosing1 < 0.3) o = mapRange(pClosing1, 0.1, 0.3, 0, 1);
                    else if (pClosing1 > 0.7) o = mapRange(pClosing1, 0.7, 0.9, 1, 0);
                    msg1.style.opacity = o;
                } else {
                    msg1.style.opacity = 0;
                }
            }

            // Closing Message 2
            const msg2 = document.getElementById('content-closing-2');
            if (msg2) {
                if (pClosing2 > 0.1 && pClosing2 < 0.9) {
                    let o = 1;
                    if (pClosing2 < 0.3) o = mapRange(pClosing2, 0.1, 0.3, 0, 1);
                    else if (pClosing2 > 0.7) o = mapRange(pClosing2, 0.7, 0.9, 1, 0);
                    msg2.style.opacity = o;
                } else {
                    msg2.style.opacity = 0;
                }
            }

            // Closing Message 3
            const msg3 = document.getElementById('content-closing-3');
            if (msg3) {
                if (pClosing3 > 0.1 && pClosing3 < 0.9) {
                    let o = 1;
                    if (pClosing3 < 0.3) o = mapRange(pClosing3, 0.1, 0.3, 0, 1);
                    else if (pClosing3 > 0.7) o = mapRange(pClosing3, 0.7, 0.9, 1, 0);
                    msg3.style.opacity = o;
                } else {
                    msg3.style.opacity = 0;
                }
            }
"""

content = content.replace(js_to_add, "")

# It should be inside applyAnimations()

# Find the end of applyAnimations
# The function ends around line 1675
# Let's just find "const msg6 = document.getElementById('agent-msg-6');" and go past its block
insert_pos = content.find("if (msg6) {")
if insert_pos != -1:
    end_of_block = content.find("}", content.find("}", insert_pos) + 1) + 1
    # Actually, applyAnimations() contains all these parts.
    # Let's insert at the very end of applyAnimations().
    # applyAnimations() ends with a `}` right before `window.addEventListener('scroll'...`

    end_pos = content.rfind("        }", 0, content.find("window.addEventListener('scroll', () => {"))
    if end_pos != -1:
        new_content = content[:end_pos] + js_to_add + "\n" + content[end_pos:]
        with open('index.html', 'w') as f:
            f.write(new_content)
        print("Moved JS inside applyAnimations().")
    else:
        print("Couldn't find end of applyAnimations.")
else:
    print("Couldn't find msg6")
