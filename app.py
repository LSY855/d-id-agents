import streamlit as st, streamlit.components.v1 as components
CLIENT_KEY = st.secrets["DID_CLIENT_KEY"]; AGENT_ID = st.secrets["DID_AGENT_ID"]

html = f"""
<link rel="preconnect" href="https://agent.d-id.com" crossorigin>
<div id="did-agent-container" style="width:80%;height:600px;margin:auto;background:#000"></div>
<div id="status" style="text-align:center;margin-top:8px;color:#666">Loading…</div>
<script>
(function(){
  const s=document.createElement('script');
  s.type='module'; s.src='https://agent.d-id.com/v2/index.js';
  s.setAttribute('data-mode','fabio');
  s.setAttribute('data-client-key','{CLIENT_KEY}');
  s.setAttribute('data-agent-id','{AGENT_ID}');
  s.setAttribute('data-name','did-agent');
  s.setAttribute('data-monitor','true');
  s.setAttribute('data-target-id','did-agent-container');
  s.onload=()=>document.getElementById('status').style.display='none';
  s.onerror=()=>document.getElementById('status').innerText='❌ 로딩 실패 - 다른 브라우저/네트워크로 시도';
  (document.currentScript||document.body).parentNode.appendChild(s);
})();
</script>"""
components.html(html, height=650, scrolling=False)

