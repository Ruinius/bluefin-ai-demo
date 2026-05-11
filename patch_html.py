with open('index.html', 'r') as f:
    content = f.read()

html_to_add = """
    <!-- Fixed Epilogue Container for Part 7 -->
    <div id="epilogue-container" style="position: fixed; top: 0; left: 0; width: 100%; height: 100vh; display: flex; align-items: center; justify-content: center; z-index: 20; pointer-events: none;">
        <div id="content-closing-1" class="text-hero" style="text-align: center; position: absolute; opacity: 0; width: 80%; max-width: 900px; color: var(--text-primary);">
            A business-first AI agent
        </div>
        <div id="content-closing-2" class="text-hero" style="text-align: center; position: absolute; opacity: 0; width: 80%; max-width: 900px; color: var(--text-primary);">
            Cost conscious with the right AI model for every task
        </div>
        <div id="content-closing-3" class="text-hero" style="text-align: center; position: absolute; opacity: 0; width: 80%; max-width: 900px; color: var(--text-primary);">
            On-prem and hyper-secure deployments available
        </div>
    </div>
"""

# Find a good place to insert this HTML. Let's place it right before <!-- Scroll Sections Containers -->
insert_pos = content.find('    <!-- Scroll Sections Containers -->')

if insert_pos != -1:
    new_content = content[:insert_pos] + html_to_add + "\n" + content[insert_pos:]
    with open('index.html', 'w') as f:
        f.write(new_content)
    print("HTML containers added.")
else:
    print("Could not find insertion point.")
