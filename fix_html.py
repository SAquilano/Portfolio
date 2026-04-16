with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

DailySetup_End_Line = -1
for i, line in enumerate(lines):
    if "alt=\"DailySetup website preview image\"" in line:
        DailySetup_End_Line = i + 3 # covers </div> </div> </div> wrapping the image
        break

Footer_Start_Line = -1
for i, line in enumerate(lines):
    if "<!-- main ends here -->" in line:
        Footer_Start_Line = i - 1 # <main> ending
        break

# We know the duplicated skills section starts at "<!-- about section ends  -->" (line 460 currently).
# And the old template projects start after the duplicated projects-section-div.
# Actually, the user asked to comment out the old projects.
# The old projects start at <div data-aos="fade-up" class="project-box-wrapper"> just before "atomic asher".
# Let's extract the old projects block between the duplicated <div class="project-boxes-div"> and the end of the section.

dup_projects_start = -1
for i in range(DailySetup_End_Line, Footer_Start_Line):
    if '<div class="project-boxes-div">' in lines[i]:
        dup_projects_start = i + 1
        break

import re
old_projects_content = "".join(lines[dup_projects_start:Footer_Start_Line-3])
old_projects_content = re.sub(r'<!--.*?-->', '', old_projects_content, flags=re.DOTALL) # strip inner comments

new_content = "".join(lines[:DailySetup_End_Line])
new_content += "\n          <!-- ALTE PROJEKTE VOM TEMPLATE\n" + old_projects_content + "          -->\n"
new_content += "        </div>\n      </div>\n    </section>\n"
new_content += "".join(lines[Footer_Start_Line:]) # from </main> onwards

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Fixed index.html structure.")

