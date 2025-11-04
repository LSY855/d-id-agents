import streamlit as st
import streamlit.components.v1 as components

st.title("D-ID AI Agent")

html_code = """
<div id="did-agent-container" style="width: 80%; height: 600px;"></div>
<script type="module"
  src="https://agent.d-id.com/v2/index.js"
  data-mode="full"
  data-client-key="Z29vZ2xlLW9hdXRoMnwxMDgyMzI0NjExMTU5MzA4NDg3ODI6Q3ZMc2pWZXAya1lwa2FPcWVFZ1dl"
  data-agent-id="v2_agt_N4vkB046"
  data-name="did-agent"
  data-monitor="true"
  data-target-id="did-agent-container">
</script>
"""

components.html(html_code, height=650)



