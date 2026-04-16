import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<div class="project-boxes-div">'
end_marker = '</div>\n      </div>\n    </section>'

start_idx = html.find(start_marker) + len(start_marker)
end_idx = html.find(end_marker)

old_projects_block = html[start_idx:end_idx]

# Remove existing html comments to prevent nested comment errors
old_projects_block = re.sub(r'<!--.*?-->', '', old_projects_block, flags=re.DOTALL)

new_project_html = """
          <div data-aos="fade-up" class="project-box-wrapper">
            <div class="project-box project-box2" id="project-box2">
              <div class="info-div">
                <img src="Projekt-Logos/logo.svg" alt="DailySetup.io favicon" class="faviconforProject" />
                <article class="ProjectHeading">DailySetup.io</article>
                <p class="ProjectDescription">
                  DailySetup: Verbessere deine Trading-Fähigkeiten durch gezieltes Training und tägliche Markt-Szenarien.
                </p>
                <div class="project-buttons">
                  <a href="https://dailysetup.io" target="_blank" class="cta"
                    aria-label="Besuche DailySetup Live">
                    <span>Live-Ansicht</span>
                    <svg viewBox="0 0 13 10" height="10px" width="15px">
                      <path d="M1,5 L11,5"></path>
                      <polyline points="8 1 12 5 8 9"></polyline>
                    </svg>
                  </a>
                </div>
              </div>
              <div class="image-div">
                <img src="Projekt-Screenshots/Bildschirmfoto 2026-04-16 um 17.05.50.png" alt="DailySetup website preview image" />
              </div>
            </div>
          </div>
"""

new_html = html[:start_idx] + "\n          <!-- ALTE PROJEKTE VOM TEMPLATE\n" + old_projects_block + "\n          -->\n" + new_project_html + "\n        " + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated index.html successfully.")
