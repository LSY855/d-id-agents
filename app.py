import streamlit as st
import streamlit.components.v1 as components

CLIENT_KEY = st.secrets["DID_CLIENT_KEY"]
AGENT_ID   = st.secrets["DID_AGENT_ID"]

st.title("D-ID AI Agent")

html = f"""
<link rel="preconnect" href="https://agent.d-id.com" crossorigin>
<div id="did-agent" style="width:80%;height:600px;margin:auto;background:#000;border-radius:12px;overflow:hidden;"></div>
<script type="module"
  src="https://agent.d-id.com/v2/index.js"
  data-mode="fab"            <!-- ★ 여기! fabio 아님 -->
  data-client-key="{CLIENT_KEY}"
  data-agent-id="{AGENT_ID}"
  data-name="did-agent"
  data-monitor="true"
  data-target-id="did-agent">
</script>
"""
components.html(html, height=650, scrolling=False)



